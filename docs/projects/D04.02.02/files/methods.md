---
title: "Focused methods — Historical Stress Paths and the Performance of Model-Based Option Hedges"
subtitle: "D04.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Information and return conventions
Write $u_i=\log(I_i/I_{i-1})$. Annualized trailing volatility is $\sqrt{252\widehat{\operatorname{Var}}(u_{i-m+1},\ldots,u_i)}$ using available observations at formation. A next-close trade requires a different lag. Freeze pricing, funding and initial premium conventions before replay.

## Interpretation
The observed price index excludes reinvested dividends; it is the replay underlying, not a total-return comparator. Use identical rebasing, strike, expiry, grid, carry and funding for GBM. Drawdown-based stress labels use future outcomes and are descriptive. Nonoverlapping windows reduce overlap but need not be independent.

## Research checks

Check actual permissions, warmup and complete sessions before assignment. Report eligible windows and separate historical sampling uncertainty from simulation error. If access fails, defer or approve a retitled simulated stress study; no silent substitution.
