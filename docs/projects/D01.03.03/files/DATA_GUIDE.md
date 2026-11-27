# Data and model setup | D01.03.03

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

S0=100, r=.02, q=0, T=.5Y, K=100, secondary K=90 or 110 with same expiry. Q sigma=.16, lambda=.7, log J N(-.12,.18^2); P baseline annual drift .06, lambda=.7 with same jump sizes; stress lambda=2 and a larger negative-jump mean, kept separate from Q pricing. Daily/weekly hedge times, exact simulated Poisson/lognormal increments, 60,000 common independent test paths, seed 101303; Merton Poisson-series prices and Greeks; BSM delta benchmark at matched ATM IV.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
