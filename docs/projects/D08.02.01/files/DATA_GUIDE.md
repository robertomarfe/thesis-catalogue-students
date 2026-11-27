# Data and model setup | D08.02.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

theta=0.04,v0=0.01/0.04/0.09,kappa=0.5/2/5,xi=0.1/0.3/0.6, maturities 0 to 24 months monthly; include Feller-satisfied and violated parameter cases with exact transition (theta>0). Quadrature or exact MC 200,000 samples, seed 2027, and independent error checks; no market futures needed. Optional Cboe VIX history https://www.cboe.com/tradable-products/vix/vix-historical-data/ for choosing illustrative spot regimes, not calibration of Q dynamics.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Timing, accounting and units

Define the pricing measure, path measure, position and loss signs, trading dates, initial funding and terminal liquidation. Freeze the provider vintage for empirical designs, retain common dates and distinguish price indices from total-return indices. A historical replay of synthetic option quotes is not a realized traded-option backtest.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
