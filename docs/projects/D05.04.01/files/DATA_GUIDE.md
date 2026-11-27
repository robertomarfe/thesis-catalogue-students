# Data and model setup | D05.04.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic S0=100, v0=theta=.04, kappa=1.5, rho=-.7, r=.02, q=0, xi=.2,.6,1.0, T=.25,1,2. Grids 12-1000 steps/year; strikes .8,1,1.2 times S0. Independent converged Heston characteristic-function quadrature for European calls; 30k-200k paths and repeated seeds, nested Brownian increments for Euler comparisons. Record wall time and MC standard error separately.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
