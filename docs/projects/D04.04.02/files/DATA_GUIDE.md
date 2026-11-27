# Data and model setup | D04.04.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic GBM, Heston and Merton Q/P martingale scenarios (set discounted P drift zero); r=.02, q=0, S0=K=100, T=.5, 26 dates. Fixed common clean model premium per scenario. 40k train,10k validation,40k test paths; low-order polynomial/spline features standardized using train data. Benchmark BSM delta with matched initial ATM IV, no hedge, and oracle model delta as diagnostic if available. Baseline frictionless; optional matched cost replay not optimized.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Timing, accounting and units

Define the pricing measure, path measure, position and loss signs, trading dates, initial funding and terminal liquidation. Freeze the provider vintage for empirical designs, retain common dates and distinguish price indices from total-return indices. A historical replay of synthetic option quotes is not a realized traded-option backtest.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
