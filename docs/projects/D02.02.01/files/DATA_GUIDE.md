# Data and model setup | D02.02.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Generate risk-neutral European calls from an independently implemented Heston pricer (check quadrature convergence and BSM limit), S0=F=100, r=q=0, T=0.25,0.5,1,2 years. Use several admissible Heston parameter sets spanning mild/strong skew; freeze them and all test seeds. Dense k grid [-0.4,0.4], 0.01 spacing; train on 9-17 points, hold out intermediate strikes and a separate wing set. Perturb training IV by 0, 0.25, 0.5 vol points with fixed seeds; separately flag noisy prices violating bounds, not as true quotes. Use 30+ independent noise draws per case; identical quotes, optimizer budgets and bounds for both models.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
