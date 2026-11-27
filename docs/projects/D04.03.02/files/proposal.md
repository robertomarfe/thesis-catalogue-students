---
title: "No-Trade Bands for Option Hedging"
subtitle: "Research proposal | D04.03.02"
---

**Derivatives · Hedging and volatility derivatives · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

A fixed calendar ignores how far the existing hedge has drifted from the current target. A no-trade band can save trading when that deviation is small. Compare state-dependent intervention against calendar strategies under a common tail-risk budget.

## Research question

Can a delta-band policy reduce expected replication cost at a given tail hedging-error budget, compared with fixed-frequency rebalancing?

## Economic mechanism

For $d_i=\Delta_i-h_{i-1}$, a band $b$ leaves the position unchanged when $|d_i|\le b$.

## Research design

Use daily decision opportunities, common paths and identical costs. Tune reset and boundary bands plus calendar benchmarks on training paths under a declared risk budget, then evaluate on independent paths.

Report achieved risk, not merely the intended budget. The comparison must use the same opportunities, shares, premium and cost convention across policies; this is not a neural-policy training study.

\newpage

## Required exhibits

Self-financing unit tests; error-cost frontier; turnover and ES table; band policy trajectories; out-of-sample stress comparison.

## Minimum viable thesis

One ATM call, three nonzero cost levels, two band rules and calendar benchmarks, independent evaluation with paired uncertainty. Distinct from D04.03.01 (calendar optimization).

## Scope and feasibility

Keep initial premium, trade convention and paths identical. Distinguish hedge error before costs from net P&L. Do not optimize bands on evaluation paths; compare uncertainty and not just mean loss. This is a finite-grid policy comparison, not a proof of global optimality.

**Prerequisites:** BSM, stochastic calculus, simulation, risk measures and Python.

**Optional extension:** Fit a state-dependent band using gamma and remaining maturity, with separate validation; compare under Heston dynamics.

## Milestones

W1-3: derive ledger and policies; W4-6: validate GBM engine; W7-9: train and select bands; W10-12: evaluate and stress; W13-16: reproduce and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
