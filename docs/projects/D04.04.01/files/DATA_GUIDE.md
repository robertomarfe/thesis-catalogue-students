# Data and model setup | D04.04.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Exact synthetic GBM under P, S0=100, K=100, T=.25 or 1, r=.02, q=0, mu=.04, sigma=.20; initial BSM Q premium. 20-50 trading decisions; costs 0,10,30 bp; fixed seeds, 50k train, 10k validation, 50k test paths. Two hidden layers (16 units each), shared policy across time; CPU-sized experiment with PyTorch. Compare daily/weekly delta and validation-tuned band under identical ledger and position bounds.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Timing, accounting and units

Define the pricing measure, path measure, position and loss signs, trading dates, initial funding and terminal liquidation. Freeze the provider vintage for empirical designs, retain common dates and distinguish price indices from total-return indices. A historical replay of synthetic option quotes is not a realized traded-option backtest.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
