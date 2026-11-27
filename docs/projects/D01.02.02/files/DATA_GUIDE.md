# Data and model setup | D01.02.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

S0=100, r=2%, q=0, v0=theta=0.04, kappa=2, xi=0.3, rho=-0.6. Use admissible parameter grids (v0,theta>0,kappa>0,xi>0, abs(rho)<1); flag Feller violations, avoid unreliable integration regimes. Maturities 1m,3m,1y,3y, k=-0.3..0.3. Hold one parameter fixed except the selected perturbation; add a variance-matched xi/rho grid. Compute prices using validated Heston integration and parity, implied vol by bracketed inversion.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
