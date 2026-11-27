# Data and model setup | D01.02.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic European calls only; S0=100, r=2%, q=0, v0=theta=0.04, kappa=2, xi=0.30, rho=-0.65 as an illustrative annualized Q scenario. Use maturities 0.25, 0.5, 1, 2 years and K/S0=0.8,...,1.2; retain alternate strikes and an entire maturity (e.g. 1 year) as untouched tests. Generate prices with a separately checked Fourier/quadrature routine, add reproducible noise in price or IV units (e.g. 0, 0.1, 0.5 volatility points), and flag invalid quotes without silently clipping them. Record seed, noise units and split. No observed option quotes are required.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
