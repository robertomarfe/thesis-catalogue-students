# Data and model setup | D02.03.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Generate synthetic BSM or Heston calls on T=0.08,0.25,0.5,1,2 years and a common normalized strike grid x=0.7 to 1.3. Use deterministic r=2%, q=1%, true common forwards/discounts. Add seeded price noise and missing cells; keep noiseless values for independent assessment. Fit unconstrained expiry-wise smooth curves and a constrained quadratic least-squares grid with linear monotonicity/convexity/calendar inequalities and bounds; anchor x=0,c=1 and, for the finite grid experiment, a sufficiently distant zero tail node. Use piecewise-linear interpolation in x and T; acknowledge tail truncation approximation.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
