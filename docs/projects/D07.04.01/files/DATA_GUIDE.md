# Data and model setup | D07.04.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic initial f(0,T)=.02+.01(1-exp(-.4T)); a=.15, sigma0=.01 annual units; 1,2,5,10Y bonds, horizon at most one year and strictly before maturity for pricing checks. Fixed maturity grid, time steps 1/12,1/52,1/252; integrate f using common nodes and trapezoids; simulate Brownian increments on nested grids, seed 270401, 30,000 paths initially. Compute bank account by integrating diagonal forward. Exact deterministic-coefficient Gaussian integrals offer an independent reference. Optional second exponential factor with fixed correlation represented by independent loadings.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Keep the counterexample labeled inadmissible under money-market Q, not an alternative calibrated pricing model. Separate integration bias, sampling uncertainty and runtime.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
