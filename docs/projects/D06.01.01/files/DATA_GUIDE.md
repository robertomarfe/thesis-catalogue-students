# Data and model setup | D06.01.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

S0=100, r=0.02, q=0, T=1, sigma=0.15/0.30/0.50, K=80/100/120. Compare full-year and final-quarter averaging, 4/12/52 equally spaced future fixings within each window, excluding time zero. Terminal European benchmark. Use exact GBM at fixings, 100,000 paths with common random numbers for matched scenarios; independent pilot paths estimate control-variate coefficient, independent seeds for error checks.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
