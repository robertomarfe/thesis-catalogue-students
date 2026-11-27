# Data and model setup | D09.02.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic flat 2% discount curve; hazard buckets 0-1,1-3,3-5,5-10y with rates 0.5%,1.5%,2.5%,1%; R=.4; maturities 1,3,5,10y. Generate exact quarterly CDS par spreads; recover bucket hazards with bracketed roots; add independent 1/5/10bp spread noise in 200 seeded perturbations; compare constant intensity fit and nonnegative regularized fit. Stress R=.2,.6. No issuer quotes.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Report survival curves and repricing residuals in basis points. Compare alternative recovery at fixed quotes, rather than relabeling the physical hazard. Retain infeasible noisy cases and disclose the objective and penalty.

## Timing, accounting and units

Specify physical versus risk-neutral probability, discounted versus undiscounted cash flows, maturity and year fractions, and whether rates and spreads are decimals, percentages or basis points. Document default timing and recovery. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For finite-state models define the state support, probability mass and numerical tolerance before fitting.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
