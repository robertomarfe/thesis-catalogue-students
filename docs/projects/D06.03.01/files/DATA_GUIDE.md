# Data and model setup | D06.03.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic zero curves flat r=-1%,0%,2%,5%; S0=100,q=1%,sigma=15%,25%,40%; T=1,3,5y; fees f=0,1%,2%; lambda_Q=0,1%,3%. Compare par budget, 100% floor and optional 90% floor. Use BSM with deterministic rates. Simulate P equity drift 6%, volatility scenarios and independent physical hazard lambda_P, 50,000 paths, seed 2027. Optional GSW yield curve https://www.federalreserve.gov/data/nominal-yield-curve.htm as sovereign benchmark, not issuer funding or collateral curve.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
