# Data and model setup | D01.02.03

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Heston Q S0=100,r=.02,q=0,v0=theta=.04,kappa=2,xi=.3,rho=-.6. Generate high-accuracy vanilla surface T=.05..2y, K=50..180 with denser central grid; compute regularized derivatives or conditional-variance projection. Check forward and butterfly/calendar consistency. Price down-and-out calls K=100,B=80/90,T=.5/1y in both models on monitored grids; use common random numbers when practical. Hedging experiment under Heston P with drift .06 and same variance dynamics as Q for baseline, explicit variance risk premium zero; initial each model's fair price, also common initial price comparison. Reprice barrier conditionally on alive status; use interpolation/grids and validate Greeks. No market quotes.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
