# Data and model setup | D04.03.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Simulate GBM under P with S0=K=100, sigma=20%, mu=5%, r=2%, q=0; T=0.25 and 1 year. Use a 252-step annual grid (adjust to maturity), compare 1, 4, 12, 26, 52 and daily rehedges where feasible; use common underlying paths. Set c=0, 5, 10, 25 basis points per traded notional as illustrative scenarios, not estimated spreads. Use 20,000 training paths and independent 20,000 test paths as initial budget, fixed seeds. Include terminal liquidation without rehedging after expiry. Benchmark prices/Greeks under Q; paths under P.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Timing, accounting and units

Define the pricing measure, path measure, position and loss signs, trading dates, initial funding and terminal liquidation. Freeze the provider vintage for empirical designs, retain common dates and distinguish price indices from total-return indices. A historical replay of synthetic option quotes is not a realized traded-option backtest.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
