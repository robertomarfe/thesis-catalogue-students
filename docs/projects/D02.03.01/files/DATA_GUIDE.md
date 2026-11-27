# Data and model setup | D02.03.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Use F=100, D=1, T=0.5 and 1.0. Generate clean calls from a mixture of two lognormal terminal distributions with positive weights, each mean F (e.g. vol 15% and 40%, weights 0.8/0.2); a second skewed scenario uses component means 90 and 110 with equal weights. Use 9, 13 and 21 uneven strikes within [65,145], nested dense truth grid, perturb prices with independent Gaussian noise of 0.02/0.10 price units. Use fixed seeds, 50 replicates per case; quote clipping to individual bounds does not enforce convexity. Add endpoints only with explicit wing assumptions; baseline guarantees interior domain only.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
