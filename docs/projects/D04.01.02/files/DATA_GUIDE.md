# Data and model setup | D04.01.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Simulate exact GBM under P with S0=100, r=2%, sigma=20%, mu=6%; T=0.08,0.25,1 year, K=80,90,100,110,120. Use nested 12/48/240 steps per year (rounded to nested contract-specific counts), no transaction costs and matched paths across strikes, using a common fine grid. BSM price initializes a self-financing replicating portfolio. Compare exact discounted terminal error with accumulated leading-order gamma approximation. Include dollar error per share and normalized by spot, not just premium.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Timing, accounting and units

Define the pricing measure, path measure, position and loss signs, trading dates, initial funding and terminal liquidation. Freeze the provider vintage for empirical designs, retain common dates and distinguish price indices from total-return indices. A historical replay of synthetic option quotes is not a realized traded-option backtest.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
