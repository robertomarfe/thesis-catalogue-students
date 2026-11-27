# Data and model setup | D11.01.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Build a two-period nonrecombining binary tree, dt=0.5, B0=1, r0=0.03, r1=0.01 or 0.07; choose Q^B up probabilities 0.4,0.6,0.45 at nodes. Set terminal stock values e.g. 150,105,95,65 and calculate intermediate stock prices by discounted backward induction (no dividends). Build T-bond identically with payoff 1, B by accrual; all positive. Test call and put strikes 80,100,120 and a digital payoff. No external data; extend to 3-6 periods.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Check all three measure transformations at every node, local payoff rank, transition sums, price equality and replication residuals. Extend only after the two-period benchmark is independently reproduced.

## Timing, accounting and units

Specify physical versus risk-neutral probability, discounted versus undiscounted cash flows, maturity and year fractions, and whether rates and spreads are decimals, percentages or basis points. Document default timing and recovery. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For finite-state models define the state support, probability mass and numerical tolerance before fitting.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
