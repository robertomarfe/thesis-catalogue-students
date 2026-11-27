# Data and model setup | D04.02.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

S0=100,v0=theta_Q=0.04,r=0.02,q=0,kappa_Q=2,xi=0.35,rho=-0.7; P stock drift 0.06, kappa_P=1.5, theta_P=0.04, same xi/rho. Target six-month ATM call, hedge option one-year call at K=100 or 120. Use validated Fourier Heston pricer and central differences for C_v, C_S; price/Greeks convergence and positivity checks. Simulate 5,000 paths with common shocks using fine full-truncation Euler or QE; rebalance weekly/daily, seed 2027; compare half-step simulation and transaction cost scenarios 0/5/20 bp of traded notional (illustrative).

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Timing, accounting and units

Define the pricing measure, path measure, position and loss signs, trading dates, initial funding and terminal liquidation. Freeze the provider vintage for empirical designs, retain common dates and distinguish price indices from total-return indices. A historical replay of synthetic option quotes is not a realized traded-option backtest.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
