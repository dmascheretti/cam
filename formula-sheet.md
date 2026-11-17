# Formula sheet and practice exercises

The written test opens with a **numerical process-modelling exercise**. These are all the models in L1.2–L1.5, then worked exercises in the style of the slide examples. Exercises A–F are **my practice problems**, not from the course; check your numbers against them.

| Topic | Formula | Watch out |
| --- | --- | --- |
| Sprue velocity | v = √(2gh) | g = 981 cm/s² if lengths in cm |
| Continuity | Q = A·v; A₁v₁ = A₂v₂ | Sprue tapered towards the base |
| Mould filling time | T\_MF = V / Q = V / (A√(2gh)) | Theoretical **minimum** |
| Die-casting gate velocity | v\_g = C\_d√(2ΔP\_inj/ρ); v\_g = (A\_p/A\_g)·v\_p | Small gate gives high velocity |
| Die-casting fill time | t\_fill = V / (A\_g v\_g) = V / (A\_p v\_p) |  |
| Arc power / density | P = I·V; PD = ηP / (πdₛ²/4) | dₛ ≈ 10–20 mm |
| Laser power density | PD = A·P / (πdₛ²/4) | Keyhole above 10⁶ W/cm² |
| Weld heat balance | A·P = w·h·v·ρ\[cₚ(Tₘ−Tₐ)+Lₘ\] = w·h·v·E\_v | E\_v in J/mm³; ignores conduction losses, so a lower bound on P |
| Rosenthal point | T−T₀ = Q/(2πkR)·exp\[−v(x−R)/(2α)\], α = k/(ρcₚ) | No melting, no latent heat |
| Cooling, point | ∂T/∂t = 2πk(v/Q)(T−T₀)² | Faster at higher v, lower Q |
| Cooling, line | ∂T/∂t = 2πkρcₚ(vg/Q)²(T−T₀)³ | Cubic, very sensitive |
| Sensor for control | τ\_total < τ\_defect; f\_s > 2f\_process |  |
| Cutting speed | v = πD₀n/1000 \[m/min\] | D₀ in mm |
| Depth, time, MRR | aₚ = (D₀−D\_f)/2; tₘ = L/(f·n); MRR = v·f·aₚ | Convert v to mm/min for mm³/min |
| Roughness | Rₐ ≈ f²/(32r)·10³ \[µm\] | f mm/rev, r mm |
| Cutting force | F\_c = k\_c·f·aₚ, k\_c = k\_cs/h\_Dˣ, h\_D = f·sinκ\_r |  |
| Cutting power | P ≈ F\_c·v\_c | v in m/s gives W |
| Taylor | v·Tⁿ = C; n = ln(v₁/v₂)/ln(T₂/T₁) | Straight line on log–log |

## A. Sprue design (inverse of the slide example)

Same mould (h = 20 cm, V = 1560 cm³), but you want T\_MF = 2 s. Required base area? v = 198.1 cm/s as before, so A = V / (T·v) = 1560 / (2 · 198.1) = **3.94 cm²**. A shorter fill time needs a larger section (or a taller sprue).

## B. Die casting

Plunger area 20 cm² moving at 2 m/s, gate 1 cm², cavity 400 cm³. v\_g = (20/1)·2 = **40 m/s**. Q = 20·10⁻⁴ · 2 = 4·10⁻³ m³/s, so t\_fill = 400·10⁻⁶ / 4·10⁻³ = **0.1 s** (compare 3 s for gravity sand casting).

## C. Arc power density

MIG at I = 200 A, V = 25 V, efficiency η = 0.7, arc diameter 15 mm. P = 5000 W, absorbed 3500 W; area = π·15²/4 = 176.7 mm², so **PD ≈ 20 W/mm²**, the same order as the arc's tabulated 50 W/mm². Laser welding needs about 10⁴ W/mm².

## D. Laser heat balance

Steel (E\_v = 7.56 J/mm³), seam width 0.5 mm, penetration 3 mm, speed 2 m/min = 33.3 mm/s, absorptivity 0.8. Melted volume rate = 0.5 · 3 · 33.3 = 50 mm³/s, so absorbed power = 50 · 7.56 = 378 W and P = 378 / 0.8 ≈ **473 W** (minimum; real values are higher because of conduction losses). For aluminium (E\_v = 2.60), the same weld needs about 3× less energy per volume, but Al's low absorptivity works against it.

## E. Turning (parameters, roughness, force, power)

D₀ = 50 mm → D\_f = 46 mm, n = 1000 rpm, f = 0.2 mm/rev, L = 200 mm, nose radius r = 0.8 mm, κ\_r = 90°, k\_cs = 1800 N/mm², x = 0.25.

1. aₚ = (50 − 46)/2 = **2 mm**; v = π·50·1000/1000 = **157.1 m/min** (2.62 m/s).
2. tₘ = 200 / (0.2·1000) = **1 min**.
3. MRR = 157.1·10³ · 0.2 · 2 = **62,800 mm³/min** (≈ 62.8 cm³/min).
4. Rₐ = 0.2²/(32·0.8)·10³ = **1.56 µm**. Halving the feed gives 0.39 µm (÷4), but doubles tₘ.
5. h\_D = 0.2 mm; k\_c = 1800 / 0.2⁰·²⁵ = 1800 / 0.669 = 2692 N/mm²; F\_c = 2692 · 0.2 · 2 = **1077 N**.
6. P ≈ 1077 · 2.62 = **2.8 kW** at the spindle.

## F. Taylor tool life

Tests: 200 m/min gives T = 10 min; 150 m/min gives T = 40 min. n = ln(200/150) / ln(40/10) = 0.2877 / 1.3863 = **0.21**; C = 200 · 10⁰·²⁰⁷⁵ = **322.5 m/min**. At 180 m/min: T = (322.5/180)^(1/0.2075) = 1.792^4.82 ≈ **16.6 min**. A small speed reduction gives a big gain in life, because n < 1.

## G. Past exam: turning (summer 2021, solved in class 6 Oct)

Bar Ø80 mm, 300 mm long, 3-jaw chuck. **External** turning over 120 mm: a\_p = 1 mm, f = 0.4 mm/rev, v\_c = 250 m/min. **Internal** turning over 20 mm: a\_p = 0.5 mm, f = 0.1 mm/rev. k\_cs = 1995 MPa, x = 0.29, κ\_r = 95°, nose radius r = 0.4 mm. Lathe: 5 kW electric, 90% efficiency.

1. h\_D = 0.4·sin95° = 0.398 mm; k\_c = 1995 / 0.398^0.29 ≈ **2605 MPa**. (Thinner chips need higher pressure: "it is harder to cut material when it is thinner".)
2. A\_D = 0.4 × 1 = 0.4 mm², so F\_c ≈ **1.04 kN** (about 100 kg-force).
3. P\_c = 1042 × 250/60 ≈ **4.3 kW**. Available = 0.9 × 5 = **4.5 kW**, so **feasible**. If not: reduce a\_p (two passes), f or v\_c.
4. Final diameter = 80 − 2·1 = **78 mm**; n = 250·1000/(π·78) ≈ **1020 rpm**; v\_f = 0.4 × 1020 = **408 mm/min**. (In class he used the final diameter 78 mm here, while the L1.5 slide defines v at D₀. The difference is about 2.5%, but state which diameter you use.)
5. **Trap:** cutting length = 120 + **1 mm exit** (the tool must disengage past the part) = 121 mm, so t\_m = 121/408 min ≈ **17.8 s**.
6. Internal R\_a = 0.1²/(32·0.4)·10³ ≈ **0.78 µm**. (Feel: 0.1 µm = mirror; about 1 µm = dull; 10 µm = sandy to the touch.)

**Exam alert:** no software in the written test, only a **calculator**; draw the part first; don't round until the end; watch units (v\_f is in mm/**min**).

## H. Past exam: drilling (2021, solved in class 6 Oct)

Through hole Ø28 mm, depth 60 mm. v\_c = 290 m/min, f = 0.1 mm/rev, **k\_c = 2100 MPa given directly** (common for drilling, because of the thrust and the complexity; point angle 160° not needed). Machine 7.5 kW, 90%.

1. Per lip: base f/2 = 0.05 mm, height D/2 = 14 mm, so A\_D = **0.7 mm²**; F\_c = 2100 × 0.7 = **1470 N**.
2. Each lip's force acts at D/4 = 7 mm: T = 2 × 1470 × 7/1000 = **20.58 Nm**.
3. n = 290·1000/(π·28) ≈ **3297 rpm**; ω = 2πn/60 = **345.3 rad/s**.
4. P = 20.58 × 345.3 ≈ **7.1 kW** > available 6.75 kW, so **not feasible** ("well done, you found it before breaking anything").
5. **Fixes (class discussion):** reduce v\_c; reduce f; drill a **smaller pilot hole** and then enlarge it. Every fix **increases time**: "it's not an unbounded optimisation". Lowering v\_c at the same f (mm/rev) doesn't change the material per revolution, only n, so the same material takes longer.
6. Drilling easily needs more power than turning, because the whole hole volume becomes chip.

## I. Past exam: face milling (summer 2021, solved in class 7 Oct)

Steel square 300 × 300 mm, roughing allowance (axial depth) **a\_p = 4 mm**. Face mill D = 80 mm, Z = 8, κ\_r = 90°, k\_cs = 1600 MPa, x = 0.197, f\_z = 0.15 mm, v\_c = 250 m/min. Machine 15 kW, 80%. Zig-zag path: **25% of the tool overhangs** one side; start and finish **5% of D** away from the part; **5 passes** with step-over = **75% of D** (so a\_e = 0.75D = 60 mm).

1. **Engagement angles** (draw it!): φ₁ = arcsin((0.5D − 0.25D)/0.5D) = arcsin(0.5) = **30°**; φ₂ = **90°** (the tool can't cut past its axis line). Total φ = 120° = **2.094 rad**. The maximum possible in face milling is 180°.
2. Tooth pitch = 2π/8 = 0.785 rad, so **z = 2.094/0.785 = 2.67** teeth on average, which is > 2, so use the **average chip thickness** method.
3. h\_D,av = (f\_z/φ)·(2a\_e/D) = (0.15/2.094)·(2·60/80) = **0.107 mm**; A\_D,av = 0.107 × 4 = **0.43 mm²**.
4. k\_c(h\_av) = 1600 × 0.107^(−0.197) ≈ **2480 MPa**. "It's not the average pressure: it's the pressure **at** the average chip thickness." F\_c,av ≈ **1.06 kN** per tooth.
5. T = z · F · D/2 = 2.67 × 1064 × 40/1000 = **113.6 Nm**; ω = v\_c/(D/2) = (250·1000/60)/40 = **104.2 rad/s**; P = **11.8 kW**.
6. Available = 0.8 × 15 = **12 kW**, so **feasible**. (In practice peaks can exceed the average, but short peaks are usually fine; you could compute the exact peak numerically.)
7. **Path length:** each pass = 0.05D + L + D + 0.05D = L + 1.1D = 388 mm, times 5 passes, plus 4 step-overs × 0.75D = 240 mm, so about **2180 mm**. n = 250·1000/(π·80) ≈ 995 rpm; v\_f = Z·f\_z·n ≈ **1194 mm/min**, so t ≈ **110 s** (almost 2 min).

**Class discussion — why this zig-zag with entry and exit margins? ("this type of discussion is what we do during the oral exam")** Five passes because the mill is narrower than the part. Enter and exit **in the plane, from outside the part**, rather than plunging, for **precision**: you're sure everything is cut, and forces and power ramp up smoothly (zero chip → stationary → zero), so vibration risk is lower. An arc entry is possible but engages more of the tool at once. Downside: **longer time**, since all moves near the part are at feed speed. If roughing and finishing were separate, you could rough fast and finish delicately. **Size the machine on the stationary (maximum) condition**, not the entry or exit.

**Prof — where k\_cs and x come from:** they come with the **tool**, which is chosen for the workpiece material (tools for Al, steel, Ti…), along with recommended ranges of f\_z and v\_c. "They don't fall from the sky."

**Exam alert — decimals:** keep decimals with a physical meaning. In mm, the 3rd decimal is a **micrometre**, the 6th a nanometre, the 9th a picometre ("the distance between atoms"). Three decimals are enough; excess digits "are just a bit embarrassing".

## J. Turning + minimum-cost tool life (solved in class 14 Oct)

Steel bar Ø100 × 300 mm, 3-jaw chuck + **tailstock**. Turn to Ø94 over 180 mm in roughing + finishing; **roughing a\_p = 2.5 mm** (Ø100 → 95). k\_cs = 1610 MPa, x = 0.29, κ\_r = 45°, f = 0.15 mm/rev, v\_c = 260 m/min. Economics: tool change T\_t = 160 s, cutting edge C\_e = €1, machine cost rate C\_r = €180/h, Taylor n = 0.122, C = 250.

1. h\_D = 0.15·sin45° = 0.106 mm; k\_c = 1610/0.106^0.29 ≈ **3090 MPa** (about 3000).
2. A\_D = 0.15 × 2.5 = **0.375 mm²**; F\_c ≈ **1.16 kN**; P = F·v = 1157 × 260/60 ≈ **5.0 kW**.
3. **Minimum-cost tool life:** T\_min = (1/n − 1)(T\_t + C\_e/C\_r). In consistent units: C\_r = 180/60 = **€3/min**, so C\_e/C\_r = 0.33 min; T\_t = 2.67 min; T\_min = (8.20 − 1) × 3.0 ≈ **21.6 min (about 22 min)**.
4. **Cutting speed for minimum cost:** from Taylor, v = C/Tⁿ = 250/21.6^0.122 ≈ **172 m/min**. That is lower than the 260 m/min used for roughing, consistent with v\_min < v\_max. (In class he stopped at the formula; the final number here is my calculation.)

**Watch units:** put time in minutes (or seconds) everywhere: T\_t, C\_e/C\_r and Taylor's C.

## K. Forming exercises (solved in class 3 Nov)

1. **Flow stress:** K = 550 MPa, n = 0.22, final true strain ε = 0.85. Y\_f = Kεⁿ ≈ **530 MPa**; average Ȳ\_f = Kεⁿ/(1+n) ≈ **435 MPa**. (Strain hardening is given, so it's a cold process.)
2. **From a tensile test:** K = 850 MPa, n = 0.30, gauge length 100 → 157 mm. ε = ln(157/100) = **0.451**; Y\_f ≈ **669 MPa**; Ȳ\_f ≈ **515 MPa**.
3. **Find K and n from two points** (0.35, 217 MPa) and (0.68, 259 MPa): n = ln(σ₂/σ₁)/ln(ε₂/ε₁) ≈ **0.27**; K = σ₁/ε₁ⁿ ≈ **290 MPa** (K is the stress at ε = 1). **Prof:** with an automated tensile test you have many sampled points, so fit by **least squares on log–log axes**: slope = n, value at ε = 1 = K.
4. **Blank size for a bend:** t = 5 mm cold-rolled steel, R = 8.5 mm, bend angle 140° (the part is bent to 40°). R/t = 1.7 < 2, so K\_ba = 0.33. A\_b = 2π(α/360)(R + K\_ba·t) ≈ **24.8 mm**. The straight legs are the drawing dimensions minus (R + t): (85 − 13.5) + (46.5 − 13.5) = 104.5 mm. Blank length ≈ **129.3 mm**. Why bother: the inside compresses and the outside stretches, so a blank cut to the developed outline would come out too long.
5. **Fraction that doesn't yield in a bend:** t = 1 mm, bend radius 120 mm, Y′ = 210 MPa, E′ = 224 GPa. ε\_y = Y′/E′ ≈ 9.4·10⁻⁴; elastic core half-thickness z\_e = ε\_y·r ≈ **0.1125 mm**, so 2·0.1125 = 0.225 mm = **22.5% of the thickness stays elastic**. Thin sheet + large radius = a big elastic core = springback.
6. **Tool radius to compensate springback:** t = 1.2 mm, Y′ = 300 MPa, E′ = 224 GPa, wanted final radius r′ = 250 mm. From 1/r − 1/r′ = 3Y′/(tE′): **r ≈ 136 mm** (no strain hardening, neutral axis at mid-plane). It comes from M\_p = wYt²/4 and the elastic recovery ΔM = (wE′t³/12)(1/r − 1/r′).

## L. Cost: casting vs additive manufacturing (solved in class 3 Nov)

Part 0.7 kg, material €50/kg. Casting: f = 0.40, C\_t = €8,000, Ṅ = 2.5 parts/h, C\_c = €100k. AM: f = 0.10, C\_t = €16,000 (consumables), Ṅ = 5 parts/h, C\_c = €500k. Both: C\_oh = €30/h, L = 0.3, t\_wo = 5 years, so hours = 24·365·5·0.3 = 13,140 h.

- Casting: C = 0.7·50/0.6 + (100,000/13,140 + 30)/2.5 + 8,000/N ≈ **73.4 + 8,000/N** €
- AM: C = 0.7·50/0.9 + (500,000/13,140 + 30)/5 + 16,000/N ≈ **52.5 + 16,000/N** €
- Equal cost at **N ≈ 383 parts** (casting is cheaper below, AM above). Casting at N = 100: **≈ €153/part**.
- If the material price rises, casting (40% scrap) suffers more, so the crossover moves to **fewer parts**.

## M. Cost: minimum production rate to keep the profit (solved in class 4 Nov)

Prosthesis 0.9 kg, stamping with f = 0.30, sold at €250 with €30 profit, so C ≤ **€220**. Material €100/kg in 2026, **+20%** (tariffs) in 2027 → €120/kg. C\_t = €5,000, N = 10,000, C\_oh = €100/h (one person), L = 0.3, t\_wo = 5 years, C\_c = €1.8M, so hours = 24·365·5·0.3 = 13,140 h.

1. Material 0.9·120/0.7 = €154.3; tooling 5,000/10,000 = €0.5; the rest must stay ≤ 220 − 154.8 = €65.2 = (1.8M/13,140 + 100)/Ṅ = 237/Ṅ, so **Ṅ ≥ 3.63 → at least 4 parts/h** (with the 2026 price, 2.6 parts/h was enough).
2. Two operators: L = 0.6 but C\_oh = €200/h, so (68.5 + 200)/Ṅ ≤ 65.2 → **Ṅ ≥ 4.1 parts/h**: you must produce faster, so it's a **disadvantage** under these assumptions.

Note the inequality direction: the cost must stay **below** €220, so the rate comes out as a **minimum**.

## N. Control charts (worked examples from the L3.3 slides)

1. **Known parameters:** shaft μ = 74.000 mm, σ = 0.010 mm, n = 5, K = 3 → σ\_X̄ = 0.0045, limits **73.9865 / 74.0135 mm**.
2. **ARL:** K = 3 → α = 0.0027, ARL₀ = **370.4**. A 2σ shift of individual values: 1 − β = P(Z > 1) = 0.159 → ARL₁ ≈ **6.3**.
3. **X̄–R, unknown parameters (25 samples, n = 5):** R̄ = 1.775 → UCL\_R = 2.114·1.775 = 3.752, sample 22 out → removed → R̄ = 1.673, UCL\_R = **3.537**; x̄̄ = 1000.016 → X̄ limits **999.051 / 1000.981** (A₂ = 0.577, D₃ = 0, D₄ = 2.114 for n = 5).
4. **I–MR:** x̄ = 0.4886, MR̄ = 0.7426 → MR chart UCL = 3.267·MR̄ = **2.426**; I chart 0.4886 ± 3·0.7426/1.128 = **−1.49 / 2.46**.

Order of work: look at the data, check normality and independence, dispersion chart first, then the mean chart, remove points only with an assignable cause, recompute.
