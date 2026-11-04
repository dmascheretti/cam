# Cross-topic links for the oral

Every process in the course follows the same chain, so the strongest oral answers place a detail in that chain: **physics → simplified model → what the model misses (model errors + disturbances) → what you can sense → how you close the loop → which automation level it sits in.** The oral explicitly tests "the ability to reason and develop links among the different topics".

|  | Casting (L1.2) | Welding (L1.3–L1.4) | Turning (L1.5) |
| --- | --- | --- | --- |
| Physics | Fluid flow + heat extraction + solidification | Heat source + melting (conduction / keyhole) | Plastic shear + friction, chip formation |
| Simple model | Bernoulli + continuity, T\_MF = V/(A√2gh) | Heat balance AP = whv·E\_v; Rosenthal | v, MRR, Ra = f²/32r, F\_c = k\_c·A\_D, Taylor |
| What it ignores | Friction, turbulence, gate losses (gives a **minimum** fill time) | Convection in the pool, latent heat (Rosenthal) | Built-up edge, wear, chatter, stiffness |
| Disturbances | Furnace drift, coating ageing, operator die-open time, die warm-up | Joint gap, fit-up, surface condition, shielding gas, material batch | Tool wear, chatter, thermal error, material hardness |
| Defects | Gas entrapment, shrinkage porosity (liquid encapsulation) | Lack of penetration/fusion, keyhole porosity, distortion, residual stress | Tolerance and roughness out of spec, tool fracture |
| Sensing | Die thermocouples (max-cycle temperature) | Photodiode, camera, spectrometer, **OCT**, seam tracker, DIC | Spindle power/current, force, vibration, position |
| Control example | **MPC** on reduced state-space model (N4SID) | **PI** on laser power from plasma electron temperature | Adapt feed/speed/offset; change tool at VB\_limit |
| Automation type | Giga casting = **fixed**; sand-casting lines = material handling | Robot cells, scanners = **programmable/flexible** | CNC lathe = **programmable**; turning centre/FMC = **flexible** |

**Recurring threads to name explicitly:**

1. **Fixed vs programmable vs flexible** (L1.1) reappears in every process: Giga casting (fixed, die = IP), robotic welding (programmable, needs repeatable fit-up), CNC turning (programmable → flexible with bar feeders, turrets, pallet changers).
2. **Model fidelity vs computational cost:** FE casting model → reduced model for MPC; Rosenthal (fast, conduction only) vs numerical fluid-flow welding models; tabulated k\_c vs online force estimation (hybrid).
3. **Model errors vs disturbances** (L1.1): friction coefficient (model error, affected by the control) vs operator die-open time (disturbance, not affected) — which is why die-open time is a **feedforward** input in the casting MPC.
4. **Sensor usability for control** (L1.4): observable + fast enough (f\_s > 2 f\_process) + total latency < defect time. Apply it to any sensor the examiner names.
5. **Toyoda and Shewhart** (L0.0): intelligent stopping on a fault, and variability that must be measured and reduced. These are the historical roots of in-process monitoring and closed-loop control.
6. **Power density** links the heat sources: arc 50 W/mm², laser 9,000 W/mm². It also explains why laser welding is narrow and deep with a small HAZ, and why it suits **flexible** automation (fibre delivery, scanners).
