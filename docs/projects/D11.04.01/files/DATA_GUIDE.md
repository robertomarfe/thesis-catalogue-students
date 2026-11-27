# Data and model setup | D11.04.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Two independent standard Gaussian shocks per step; discounted stock a martingale under P, nontraded asset Y correlated with stock shock through rho, both lognormal. Claim H=discounted max(Y_T-K,0), r=.02, vol_S=.20, vol_Y=.30, T=1, rho=0,.25,.5,.75,1. One-step analytic covariance via quadrature; 12-step synthetic paths, regress conditional covariance/variance on state (S,Y,time) using independent training and evaluation. Compare zero hedge, one-step projection, dynamic projection and proxy delta from rho*sigma_Y*Y/(sigma_S*S) times Y delta.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Check one-period orthogonality, out-of-sample error and residual variance for zero, static, dynamic and proxy-delta hedges. Report the full-span continuous limit separately from finite-grid errors.

## Timing, accounting and units

Specify physical versus risk-neutral probability, discounted versus undiscounted cash flows, maturity and year fractions, and whether rates and spreads are decimals, percentages or basis points. Document default timing and recovery. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For finite-state models define the state support, probability mass and numerical tolerance before fitting.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
