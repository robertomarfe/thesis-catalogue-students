# Data and model setup | D09.04.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic GBM under Q, S0=100, r=.025, dividend yield 0, sigma=.25, 3Y long forward with fair strike S0 exp(rT), closeout V_t=S_t-K exp(-r(T-t)), R=.4, lambda=.02 and .05; rho=-.8,-.4,0,.4,.8. Monthly/weekly grids and common random normals, seed 290402; 200,000 paths or more for rare default. Grid default times rounded upward; use pre-settlement exposure at maturity. Use a shorter maturity and analytic marginal hazard checks.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Check marginal survival at all grid dates, exposure distributions, paired loss differences and grid refinement; distinguish dependence from changes in hazard or recovery. Contrast long and short forwards. A common latent horizon across maturities is a possible redesign, not part of the current frozen scope.

## Timing, accounting and units

Specify physical versus risk-neutral probability, discounted versus undiscounted cash flows, maturity and year fractions, and whether rates and spreads are decimals, percentages or basis points. Document default timing and recovery. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For finite-state models define the state support, probability mass and numerical tolerance before fitting.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
