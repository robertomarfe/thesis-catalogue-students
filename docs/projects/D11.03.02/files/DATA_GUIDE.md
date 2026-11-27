# Data and model setup | D11.03.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic S0=100,r=.02,q=0,T=.25,1; bands [.15,.25], [.10,.35], degenerate [.2,.2]. Call K=100 and butterfly with K=90,100,110; include call spread. Implement monotone explicit or implicit finite differences with appropriate boundaries, enforce nonnegative transition weights and CFL where needed. Independent bounded-volatility controlled tree or policy iteration check, no calibration claims.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Use the degenerate band and convex call limits to check sign and units; record instability and boundary effects. Distinguish the worst-case dynamic control from a search over constant volatilities.

## Timing, accounting and units

Specify physical versus risk-neutral probability, discounted versus undiscounted cash flows, maturity and year fractions, and whether rates and spreads are decimals, percentages or basis points. Document default timing and recovery. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For finite-state models define the state support, probability mass and numerical tolerance before fitting.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
