---
title: "Dynamic versus Static Stock-Bond Asset Allocation"
subtitle: "Research proposal | A08.04.02"
---

**Asset pricing · Portfolio choice, behavioral finance and market frictions · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Dynamic stock-bond allocation can exploit changing covariance, but comparison requires valid holding returns and equal trading conventions.

## Research question

Does a long-only dynamic stock-bond allocation driven by past covariance estimates improve net risk-adjusted performance relative to static 60/40 and expanding-risk benchmarks?

## Economic mechanism

For continuous zero yield $y_t(n)$, $P_t(n)=e^{-ny_t(n)}$; monthly gross return is $P_{t+1}(n-1/12)/P_t(n)$.

## Research design

GSW 5-year aging zero and French total market, initial 120 months, rolling 36/60 or EWMA, expanding and 60/40, final 15 years where feasible.

Hand-check P_(t+1)(5-1/12)/P_t(5) and common monthly market total return. Verify EWMA versus direct weighted covariance, lag estimates and training-only tuning. Compare same capital/constraints/costs and out-of-sample periods, net performance with paired block inference.

\newpage

## Required exhibits

Wealth and drawdown panels, allocation/correlation paths, net performance and turnover tables, uncertainty and cost break-even sensitivity.

## Minimum viable thesis

Static and two dynamic policies on same dates, valid aging return and drifted turnover, costs and held-out risk/performance uncertainty.

## Scope and feasibility

Synthetic constant-maturity strategy ignores security-level execution and tax; modelled cost not observed cost. Fixed 60/40 is rebalanced, not buy-and-hold. No test-window tuning or ex-post regime policy; differences in return and risk both matter.

**Prerequisites:** Portfolio theory, covariance estimation, fixed income, time series.

**Optional extension:** Add cash-inclusive target-volatility policy with predeclared volatility target, compare equal ex-ante risk and avoid leverage.

## Milestones

W1-3: theory and sources; W4-6: aging returns/ledger; W7-9: validation and freeze; W10-12: held-out and costs; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
