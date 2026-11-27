# Data and model setup | D01.03.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Generate two truth panels (Heston and Merton), S0=100,r=.02,q=.01; maturities 1m,3m,6m,1y,2y; forward moneyness .8-1.2. Heston v0=theta=.04,kappa=2,xi=.4,rho=-.7; Merton sigma=.15,lambda=.7,m=-.12,s=.15. Use exact model prices plus bounded synthetic measurement noise, reject arbitrage-invalid quotes or fit prices within noise intervals. Calibrate on alternating strikes at 3m,6m,1y; test other strikes and 1m/2y. Multistart with fixed bounds and independent pricing check.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
