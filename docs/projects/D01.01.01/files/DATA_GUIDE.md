# Data and model setup | D01.01.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Use S=100, K/S=0.7 to 1.3, T=0.0833,0.5,1,2 years, sigma=0.1 to 0.5, r=0 to 0.08, q=0 to 0.04. All rates continuously compounded. Use exact BSM and independent discounted integration under Q. In the mixture set equal weights and solve the second component variance to match E_Q[S_T^2] for each T; retain only admissible cases. Optional contextual rates from FRED https://fred.stlouisfed.org/series/DGS1 (not needed for the baseline).

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
