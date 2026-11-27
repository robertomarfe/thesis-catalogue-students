# Data and model setup | D06.01.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Use S0=100, K=100, B=70,85,95, r=2%, q=0, sigma=20%, T=0.5 and 1 year. Simulate Q exact GBM at m=12,52,252 equally spaced intervals; 100,000 paths initially, seed and MC errors recorded. Compare naive grid monitoring (exact for a contract monitored on those dates) with bridge-weighted continuous monitoring on the same endpoints and a validated analytic price. No market data needed; no rebate or dividends in baseline.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
