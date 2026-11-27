# Data and model setup | D01.03.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic S0=100, r=.02, q=.01, T=.02,.25,1,2 years; strikes .7-1.3 times forward; total variance .09/year, lambda=.25,1,2, m=-.10 or 0, s=.12; discard negative residual diffusion variance. Independent exact terminal simulation with Poisson counts; use tail tolerance for mixture weights and price contribution. No market calibration claimed.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
