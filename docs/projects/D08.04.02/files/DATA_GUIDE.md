# Data and model setup | D08.04.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Use S0=100, T=1, r=2%, q=0. Price with BSM baseline Q vol 20%, 25%, 35%; physical GBM drift 6%, vol 15%/25%, and a compensated negative jump scenario under P with explicit mean. Optional coherent Q jump-price robustness, not necessary for P stress. Choose Kp=90 or 95 and optimize overlay quantity subject to net premium 1% (also 0.5%,2%) of capital, cap quantity at one share; put spread Klow=75, collar call strike >100 solved or grid selected within cost/quantity constraints. Unspent budget remains risk-free; never force equality if infeasible. Same paths for all hedges, 100,000 terminal draws and independent evaluation seeds.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Timing, accounting and units

Define the pricing measure, path measure, position and loss signs, trading dates, initial funding and terminal liquidation. Freeze the provider vintage for empirical designs, retain common dates and distinguish price indices from total-return indices. A historical replay of synthetic option quotes is not a realized traded-option backtest.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
