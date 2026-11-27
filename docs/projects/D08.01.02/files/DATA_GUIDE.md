# Data and model setup | D08.01.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Simulate CIR under Q, v0=0.04, theta=0.04, kappa=1 or 3, xi=0.10,0.30,0.60; include v0=0.01 and 0.09 sensitivities; T=0.25,1,2. Exact noncentral chi-square transitions, trapezoidal quadrature of integrated variance, 52/252/504 steps per year. Start 50,000 independent paths, seed 1618, and increase until MC intervals are small relative to material gaps. Include xi=0 as exact limiting benchmark.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Timing, accounting and units

Define the pricing measure, path measure, position and loss signs, trading dates, initial funding and terminal liquidation. Freeze the provider vintage for empirical designs, retain common dates and distinguish price indices from total-return indices. A historical replay of synthetic option quotes is not a realized traded-option backtest.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
