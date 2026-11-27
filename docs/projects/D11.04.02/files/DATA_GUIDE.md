# Data and model setup | D11.04.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic Gaussian X with mean .04, SD .20 in discounted units, H with mean .08, SD .15, correlations 0,.3,.6,.95,1; gamma .5,1,2,5,10. Check units for risk aversion and notional. For nonlinear extension, discrete X and independent binary nontraded shock, H=(Y-K)^+ with bounded Y; full-support probabilities, tradable up/down gains straddling zero. Optimize scalar position by convex log-sum-exp, verify first-order conditions and certainty-equivalent equality.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Compare numerical certainty-equivalent equality and analytic prices, risk-aversion and correlation sensitivity and scaling. If a nonlinear claim is added, distinguish a preference-dependent value from no-arbitrage bounds.

## Timing, accounting and units

Specify physical versus risk-neutral probability, discounted versus undiscounted cash flows, maturity and year fractions, and whether rates and spreads are decimals, percentages or basis points. Document default timing and recovery. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For finite-state models define the state support, probability mass and numerical tolerance before fitting.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
