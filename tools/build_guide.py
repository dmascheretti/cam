#!/usr/bin/env python3
"""Build the per-chapter study-guide folder from a Markdown export of the
Claude Docs study guide (the guide stays the single source of truth).

Usage:
    python3 tools/build_guide.py source/guide-export.md [--pdf-dir DIR]

What it writes (paths relative to cam-study-guide/):
    README.md                    overview, how to use, chapter index
    chapters/<Lx.y-slug>.md      one file per lecture: slides + professor's
                                 exam-relevant comments + images, then the
                                 professor's background comments, the practice
                                 exercises and the oral questions of that chapter
    formula-sheet.md             the whole formula sheet + all exercises
    oral-questions.md            all likely oral questions
    cross-topic-links.md         the cross-topic table
    background.md                all background comments, by chapter
    full-guide.md                the whole guide in one file
    images/<Lx.y>/slide-NN.jpg   slide images (only rendered if --pdf-dir is
                                 given and the image is missing)

Only the Python standard library is used. Rendering images needs pdftoppm
(poppler-utils) and the original slide PDFs.
"""
import argparse
import glob
import os
import re
import subprocess

GUIDE_URL = "https://claude.ai/artifact/WrGc96ueegSH8ZXZdT4FaB"

# Which oral question (list, number) belongs to which chapter.
# List 1 = "Likely oral questions", list 2 = "More oral questions (L1.6–L1.9)".
ORAL_MAP = {
    (1, 1): "L1.1", (1, 2): "L1.1", (1, 3): "L1.1", (1, 4): "L1.1",
    (1, 5): "L1.1", (1, 6): "L1.2", (1, 7): "L1.2", (1, 8): "L1.3",
    (1, 9): "L1.3", (1, 10): "L1.4", (1, 11): "L1.4", (1, 12): "L1.4",
    (1, 13): "L1.4", (1, 14): "L1.5", (1, 15): "L1.5", (1, 16): "L0.0",
    (1, 17): "L0.0", (1, 18): "L1.1", (1, 19): "L0.0",
    (2, 1): "L1.6", (2, 2): "L1.6", (2, 3): "L1.6", (2, 4): "L1.6",
    (2, 5): "L1.8", (2, 6): "L1.8", (2, 7): "L1.8", (2, 8): "L1.8",
    (2, 9): "L1.7", (2, 10): "L1.7", (2, 11): "L1.9", (2, 12): "L1.9",
    (2, 13): "L1.9", (2, 14): "L2.1", (2, 15): "L2.2", (2, 16): "L1.7",
    (2, 17): "L2.2", (2, 18): "L3.1", (2, 19): "L3.1", (2, 20): "L1.9",
    (2, 21): "L3.2", (2, 22): "L3.3", (2, 23): "L3.3", (2, 24): "L3.3",
    (2, 25): "L3.4", (2, 26): "L3.4",
    (2, 27): "L3.5", (2, 28): "L3.5", (2, 29): "L3.5",
    (2, 30): "L3.6", (2, 31): "L3.6", (2, 32): "L3.6",
}

# Which practice exercise (letter of the formula-sheet subsection) belongs
# to which chapter(s).
EXERCISE_MAP = {
    "A": ["L1.2"], "B": ["L1.2"], "C": ["L1.3"], "D": ["L1.3"],
    "E": ["L1.5"], "F": ["L1.5"], "G": ["L1.5"], "H": ["L1.6"],
    "I": ["L1.6"], "J": ["L1.9", "L1.5"], "K": ["L1.7", "L1.8"],
    "L": ["L1.9"], "M": ["L1.9"],
    "N": ["L3.3"], "O": ["L3.5"],
}

IMAGE_RE = re.compile(
    r"^(\s*[*-]\s+)?&#91;image: (.*?\((L\d\.\d) slide (\d+)\))\\\]\s*$")
CHAPTER_RE = re.compile(r"^(L\d\.\d)\s")


def slugify(title):
    lecture, rest = title.split(" ", 1)
    s = rest.lower().replace("–", "-")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return lecture + "-" + s.strip("-")


def split_sections(lines, level):
    """Split lines on headings of exactly `level` (#, ##, ...).
    Returns (preamble, [(title, body_lines), ...])."""
    marker = "#" * level + " "
    preamble, sections = [], []
    current = None
    for line in lines:
        if line.startswith(marker):
            current = (line[len(marker):].strip(), [])
            sections.append(current)
        elif current is None:
            preamble.append(line)
        else:
            current[1].append(line)
    return preamble, sections


def image_path(lecture, slide):
    return "images/%s/slide-%02d.jpg" % (lecture, int(slide))


def convert_images(lines, prefix, needed):
    """Replace the export's image placeholders with Markdown images."""
    out = []
    for line in lines:
        m = IMAGE_RE.match(line)
        if m:
            bullet, alt, lecture, slide = m.groups()
            path = image_path(lecture, slide)
            needed.add((lecture, int(slide)))
            out.append("%s![%s](%s%s)" % (bullet or "", alt, prefix, path))
        else:
            out.append(line)
    return out


def convert_math(lines):
    """Turn the export's ```latex code blocks into ```math blocks, which
    GitHub renders as display math (MathJax). A block written on several
    lines with \\\\ line breaks is wrapped in a gathered environment, because
    display math only honours \\\\ inside an environment."""
    out = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "```latex":
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            body = lines[i + 1:j]
            if len(body) > 1 or any(l.rstrip().endswith("\\\\")
                                    for l in body):
                body = ["\\begin{gathered}"] + body + ["\\end{gathered}"]
            out += ["```math"] + body + ["```"]
            i = j + 1
        else:
            out.append(lines[i])
            i += 1
    return out


def shift_headings(lines, by):
    """Demote (by > 0) or promote (by < 0) every heading by `by` levels."""
    out = []
    for line in lines:
        m = re.match(r"^(#+) ", line)
        if m:
            level = max(1, len(m.group(1)) + by)
            line = "#" * level + line[len(m.group(1)):]
        out.append(line)
    return out


def trim(lines):
    while lines and not lines[0].strip():
        lines = lines[1:]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    return lines


def parse_oral(body):
    """Return {chapter: [question lines]} and the intro paragraph."""
    by_chapter = {}
    intro = []
    list_no = 1
    seen_list = False
    for line in body:
        if line.startswith("**More oral questions"):
            list_no = 2
            continue
        m = re.match(r"^(\d+)\. ", line)
        if m:
            seen_list = True
            chapter = ORAL_MAP.get((list_no, int(m.group(1))))
            if chapter:
                by_chapter.setdefault(chapter, []).append(
                    "- " + line[m.end():])
        elif not seen_list and line.strip():
            intro.append(line)
    return by_chapter, intro


def render_images(needed, root, pdf_dir):
    missing = []
    for lecture, slide in sorted(needed):
        target = os.path.join(root, image_path(lecture, slide))
        if os.path.exists(target):
            continue
        pdfs = glob.glob(os.path.join(pdf_dir, "*%s_*.pdf" % lecture))
        if not pdfs:
            missing.append((lecture, slide))
            continue
        os.makedirs(os.path.dirname(target), exist_ok=True)
        stem = target[:-len(".jpg")]
        subprocess.run(["pdftoppm", "-jpeg", "-jpegopt", "quality=85",
                        "-r", "110", "-f", str(slide), "-l", str(slide),
                        "-singlefile", pdfs[0], stem], check=True)
    return missing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("export", help="Markdown export of the study guide")
    ap.add_argument("--pdf-dir", help="folder with the slide PDFs")
    args = ap.parse_args()

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    lines = open(args.export, encoding="utf-8").read().splitlines()
    title_lines, sections = split_sections(lines, 2)
    title = next((l[2:].strip() for l in title_lines if l.startswith("# ")),
                 "CAM study guide")
    sec = {t: b for t, b in sections}

    def find(prefix):
        for t, b in sections:
            if t.startswith(prefix):
                return t, b
        raise SystemExit("section not found: " + prefix)

    _, how_to = find("How to use")
    _, cross = find("Cross-topic")
    _, formula = find("Formula sheet")
    _, oral = find("Likely oral questions")
    _, background = find("Background from the lectures")

    chapters = [(t, b) for t, b in sections if CHAPTER_RE.match(t)]
    _, bg_subs = split_sections(background, 3)
    bg_by_chapter = {t.split()[0]: b for t, b in bg_subs}
    formula_pre, formula_subs = split_sections(formula, 3)
    oral_by_chapter, oral_intro = parse_oral(oral)

    needed = set()
    os.makedirs(os.path.join(root, "chapters"), exist_ok=True)
    index_rows = []
    for t, body in chapters:
        lecture = t.split()[0]
        fname = slugify(t) + ".md"
        index_rows.append((lecture, t[len(lecture):].strip(), fname))
        out = ["# " + t, "",
               "> Part of the CAM study guide. Source of truth: "
               "[the study guide](%s). Generated by `tools/build_guide.py`; "
               "edit the guide, not this file." % GUIDE_URL, "",
               "## Slides and professor's explanations (exam material)", ""]
        out += trim(convert_images(body, "../", needed))
        bg = bg_by_chapter.get(lecture)
        out += ["", "## Professor background (less exam-critical)", ""]
        out += trim(bg) if bg else ["*No background comments for this "
                                    "chapter.*"]
        exercises = [(st, sb) for st, sb in formula_subs
                     if lecture in EXERCISE_MAP.get(st[:1], [])
                     and st[1:2] == "."]
        out += ["", "## Practice exercises", ""]
        if exercises:
            for st, sb in exercises:
                out += ["### " + st, ""] + trim(sb) + [""]
            out += ["All formulas: [formula sheet](../formula-sheet.md)."]
        else:
            out += ["*No dedicated exercise. All formulas: "
                    "[formula sheet](../formula-sheet.md).*"]
        out += ["", "## Likely oral questions", ""]
        qs = oral_by_chapter.get(lecture)
        out += qs if qs else ["*No dedicated question; see "
                              "[cross-topic links](../cross-topic-links.md)"
                              " and [all oral questions]"
                              "(../oral-questions.md).*"]
        with open(os.path.join(root, "chapters", fname), "w",
                  encoding="utf-8") as f:
            f.write("\n".join(convert_math(out)).rstrip() + "\n")

    def write(name, heading, body):
        with open(os.path.join(root, name), "w", encoding="utf-8") as f:
            f.write("\n".join(convert_math(["# " + heading, ""] + trim(body)))
                    + "\n")

    # The whole guide in one file, with images and math rendered by GitHub.
    with open(os.path.join(root, "full-guide.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(convert_math(convert_images(lines, "", needed)))
                .rstrip() + "\n")

    write("formula-sheet.md", "Formula sheet and practice exercises",
          shift_headings(formula, -1))
    write("oral-questions.md", "Likely oral questions with model answers",
          oral)
    write("cross-topic-links.md", "Cross-topic links for the oral", cross)
    write("background.md", "Background from the lectures (less "
          "exam-critical)", shift_headings(background, -1))

    readme = ["# " + title, "",
              "Study notes for *Computer Aided Manufacturing* (Prof. A. G. "
              "Demir, Politecnico di Milano): lecture slides combined with "
              "the professor's explanations from the recordings.", "",
              "The source of truth is [the study guide](%s). This folder is "
              "the same content split by chapter, regenerated with "
              "`tools/build_guide.py`." % GUIDE_URL, "",
              "## Chapters", "",
              "| Lecture | Topic | File |", "| --- | --- | --- |"]
    for lecture, topic, fname in index_rows:
        readme.append("| %s | %s | [%s](chapters/%s) |"
                      % (lecture, topic, fname, fname))
    readme += ["", "Each chapter file has four parts: slides and the "
               "professor's exam-relevant explanations (with slide images), "
               "the professor's background comments, the practice exercises, "
               "and the likely oral questions for that chapter.", "",
               "## Across chapters", "",
               "- [Formula sheet and practice exercises](formula-sheet.md)",
               "- [Likely oral questions with model answers]"
               "(oral-questions.md)",
               "- [Cross-topic links for the oral](cross-topic-links.md)",
               "- [Background from the lectures](background.md)",
               "- [Full guide as one file](full-guide.md) (everything above "
               "in one page, with images and formulas)",
               "- [Raw export](source/guide-export.md) (the unprocessed "
               "export the files are built from)", "",
               "## How to use this guide", ""]
    readme += shift_headings(trim(how_to), 1)
    readme += ["", "## Updating", "",
               "1. Export the study guide as Markdown to "
               "`source/guide-export.md`.",
               "2. Run `python3 tools/build_guide.py source/guide-export.md "
               "--pdf-dir <folder with the slide PDFs>`.",
               "3. Commit the changed files."]
    with open(os.path.join(root, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(readme) + "\n")

    missing = []
    if args.pdf_dir:
        missing = render_images(needed, root, args.pdf_dir)
    else:
        missing = [n for n in needed
                   if not os.path.exists(os.path.join(root, image_path(*n)))]
    print("chapters:", len(chapters), "images referenced:", len(needed),
          "missing:", len(missing))


if __name__ == "__main__":
    main()
