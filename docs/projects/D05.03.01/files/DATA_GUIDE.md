# Data and model setup | D05.03.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

BSM and Heston markets S0=100,r=.02,q=0,v0=theta=.04,kappa=2,xi=.3,rho=-.6. T=.1,1,3 years; strikes 60..140, 1/25/201 queries, include off-grid strikes. Compare adaptive quadrature of damped inversion, FFT N=2^10..2^15 with admissible alpha and grid spacing, and independent Heston P1/P2 integration cross-checked with BSM and Monte Carlo uncertainty. Benchmark warm-up and repeated wall time on same hardware.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
