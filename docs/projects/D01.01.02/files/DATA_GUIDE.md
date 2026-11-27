# Data and model setup | D01.01.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Use S0=100, r=2%, q=0, diffusion sigma=20%, Q lambda=0,0.5,1.5/year, log-jump mean -0.10 and SD 0.15; T=0.25,1 and K=80,90,100,110,120. Verify Poisson-tail truncation. Fit BSM ATM separately by expiry and hold other strikes out. Simulate P paths with same jump law as baseline (explicit choice), total expected return 6%, plus a different P intensity sensitivity. Compare fixed calibrated BSM volatility and model-consistent delta on the same paths, daily/weekly grids, identical true initial option premium and cash financing.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
