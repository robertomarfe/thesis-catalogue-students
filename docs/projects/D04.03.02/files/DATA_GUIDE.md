# Data and model setup | D04.03.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic GBM under P: S0=100, r=.02, q=0, mu=.06, sigma=.20, T=.25 or 1y, K/S0=.9,1,1.1; BSM initial premium under Q. Daily decisions and exact GBM steps; common paths for all policies, 20,000 training and 50,000 independent evaluation paths. Costs 0, 5, 20, 50 bp of traded notional; bands .01-.20 shares; fixed daily/weekly/monthly and no hedge controls. Include initial and liquidation trades in all strategies.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Timing, accounting and units

Define the pricing measure, path measure, position and loss signs, trading dates, initial funding and terminal liquidation. Freeze the provider vintage for empirical designs, retain common dates and distinguish price indices from total-return indices. A historical replay of synthetic option quotes is not a realized traded-option backtest.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
