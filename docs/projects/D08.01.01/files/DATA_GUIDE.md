# Data and model setup | D08.01.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

S0=100; T=0.25,1; sigma=15%,30%; lambda=0,0.5,2 per year, log jump mean -0.10, SD 0.15, plus positive-jump scenario. Sample n=12,52,252 per year rounded for maturity. Use exact independent Gaussian/compound-Poisson increments, 50,000 paths initially, increase until 95% MC intervals resolve material differences or report noise. Freeze seed and parameters; independent reference paths. Rates zero; fair strike in variance units and optionally vol points via square root (not volatility swap price).

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Timing, accounting and units

Define the pricing measure, path measure, position and loss signs, trading dates, initial funding and terminal liquidation. Freeze the provider vintage for empirical designs, retain common dates and distinguish price indices from total-return indices. A historical replay of synthetic option quotes is not a realized traded-option backtest.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
