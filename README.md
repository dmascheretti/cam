# CAM – Study Guide (Prof. Demir, A.Y. 2026-27)

Study notes for *Computer Aided Manufacturing* (Prof. A. G. Demir, Politecnico di Milano): lecture slides combined with the professor's explanations from the recordings.

The source of truth is [the study guide](https://claude.ai/artifact/WrGc96ueegSH8ZXZdT4FaB). This folder is the same content split by chapter, regenerated with `tools/build_guide.py`.

## Chapters

| Lecture | Topic | File |
| --- | --- | --- |
| L0.0 | Introduction to CAM | [L0.0-introduction-to-cam.md](chapters/L0.0-introduction-to-cam.md) |
| L1.1 | Manufacturing and automation – introduction | [L1.1-manufacturing-and-automation-introduction.md](chapters/L1.1-manufacturing-and-automation-introduction.md) |
| L1.2 | Transformation by solidification – casting | [L1.2-transformation-by-solidification-casting.md](chapters/L1.2-transformation-by-solidification-casting.md) |
| L1.3 | Transformation by fusion welding | [L1.3-transformation-by-fusion-welding.md](chapters/L1.3-transformation-by-fusion-welding.md) |
| L1.4 | Welding modelling and automation | [L1.4-welding-modelling-and-automation.md](chapters/L1.4-welding-modelling-and-automation.md) |
| L1.5 | Transformation by chip removal – turning and tool life | [L1.5-transformation-by-chip-removal-turning-and-tool-life.md](chapters/L1.5-transformation-by-chip-removal-turning-and-tool-life.md) |
| L1.6 | Milling, drilling and process control in machining | [L1.6-milling-drilling-and-process-control-in-machining.md](chapters/L1.6-milling-drilling-and-process-control-in-machining.md) |
| L1.7 | Transformation by deformation: forming processes | [L1.7-transformation-by-deformation-forming-processes.md](chapters/L1.7-transformation-by-deformation-forming-processes.md) |
| L1.8 | Sheet-metal forming control and automation | [L1.8-sheet-metal-forming-control-and-automation.md](chapters/L1.8-sheet-metal-forming-control-and-automation.md) |
| L1.9 | Cost estimation in manufacturing | [L1.9-cost-estimation-in-manufacturing.md](chapters/L1.9-cost-estimation-in-manufacturing.md) |
| L2.1 | CNC machine tools | [L2.1-cnc-machine-tools.md](chapters/L2.1-cnc-machine-tools.md) |
| L2.2 | Robotic manipulators for manufacturing | [L2.2-robotic-manipulators-for-manufacturing.md](chapters/L2.2-robotic-manipulators-for-manufacturing.md) |
| L3.1 | Smart manufacturing – introduction | [L3.1-smart-manufacturing-introduction.md](chapters/L3.1-smart-manufacturing-introduction.md) |
| L3.2 | Smart manufacturing – sensing and data mining | [L3.2-smart-manufacturing-sensing-and-data-mining.md](chapters/L3.2-smart-manufacturing-sensing-and-data-mining.md) |
| L3.3 | Statistical process monitoring – part 1: SPC fundamentals | [L3.3-statistical-process-monitoring-part-1-spc-fundamentals.md](chapters/L3.3-statistical-process-monitoring-part-1-spc-fundamentals.md) |
| L3.4 | Statistical process monitoring – part 2: in-process monitoring | [L3.4-statistical-process-monitoring-part-2-in-process-monitoring.md](chapters/L3.4-statistical-process-monitoring-part-2-in-process-monitoring.md) |
| L3.5 | Smart manufacturing – PCA and multivariate process monitoring | [L3.5-smart-manufacturing-pca-and-multivariate-process-monitoring.md](chapters/L3.5-smart-manufacturing-pca-and-multivariate-process-monitoring.md) |
| L3.6 | Smart manufacturing – AI-driven monitoring and automation | [L3.6-smart-manufacturing-ai-driven-monitoring-and-automation.md](chapters/L3.6-smart-manufacturing-ai-driven-monitoring-and-automation.md) |

Each chapter file has four parts: slides and the professor's exam-relevant explanations (with slide images), the professor's background comments, the practice exercises, and the likely oral questions for that chapter.

## Across chapters

- [Formula sheet and practice exercises](formula-sheet.md)
- [Likely oral questions with model answers](oral-questions.md)
- [Cross-topic links for the oral](cross-topic-links.md)
- [Background from the lectures](background.md)
- [Full guide as one file](full-guide.md) (everything above in one page, with images and formulas)
- [Raw export](source/guide-export.md) (the unprocessed export the files are built from)

## How to use this guide

The 30 cum laude comes from the oral (60%), and the oral rewards **linking topics**: every process is studied as *physics → model → disturbances → sensing → control*. Each lecture section below combines the slides with what Prof. Demir said in class. **Exam alert** marks points he stressed; **Class discussion** gives the answers to questions he asked the room.

| Part | Weight | Content (from L0.0 + what he said) |
| --- | --- | --- |
| Written | 40% | 1) numerical exercise on process modelling; 2) numerical exercise on quality monitoring / data analysis; 3) CAM software question. You bring your own laptop and submit software files. |
| Oral | 60% | Basic topics; open questions testing your ability to **link topics**; the whole CAM Lab + CAM Shop workflow. Allowed only after passing the written, **in the same session**. |
| CAM Shop (elective) | +0 to 3 points | Group of 6, four activities (milling + air bending), one report per week. Points are **added**, not averaged. |

**Exam alert — cum laude:** "You cannot get cum laude if you haven't done the project." The CAM Shop assignment is elective, but without it 30L is impossible.

**Exam alert (3 Nov) — written-exam rules:** a **formula sheet is provided**; you work on your own computer, but **no notes and no AI**, so practise with a calculator (Excel is allowed, "but we shouldn't see weird windows pop up on your screens").

Other things he said: attending only theory and lab is "not really good", since the oral covers everything. Five exam calls a year (2 winter, 2 summer, 1 September). Use your university e-mail, and ask for office appointments well before the exam, not on the Sunday before.

**What to study:** each chapter (L0.0 to L3.1) is the exam material: the slide content plus only the professor's comments that matter for the exam (marked **Prof**, **Class discussion** or **Exam alert**). The rest of what he said in class (stories, videos, lab demos, history) is in **Background from the lectures**, the last section at the end of the guide. Read it once and don't memorise it.

## Updating

1. Export the study guide as Markdown to `source/guide-export.md`.
2. Run `python3 tools/build_guide.py source/guide-export.md --pdf-dir <folder with the slide PDFs>`.
3. Commit the changed files.
