---
title: "Portfolio Choice under Expected Shortfall Constraints"
subtitle: "Research proposal | A08.04.01"
---

**Asset pricing · Portfolio choice, behavioral finance and market frictions · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Expected shortfall targets adverse outcomes rather than penalizing upside and downside alike. Its benefits depend on scenario quality and feasible training risk budgets.

## Research question

Do expected-shortfall-constrained allocations improve held-out downside risk and economic performance relative to variance-constrained and equal-weight portfolios?

## Economic mechanism

For loss $L=-w^\top r$, ES at confidence $\alpha$ is $\min_z[z+\mathbb E[(L-z)_+]/(1-\alpha)]$.

## Research design

French 10 industries daily, 30 robustness, five-year scenario window, monthly rebalance, .95 ES and fixed sensitivity; variance/equal weight, realized daily net ES with paired blocks.

Verify empirical ES by order statistic and direct Rockafellar-Uryasev objective; compare two-asset LP to enumerated frontier. Record solver status/runtime, prespecified fallback and feasible risk budgets. Run rolling daily scenario fit with monthly trading, actual complete calendar and paired date-block ES intervals. Large grid remains student work.

\newpage

## Required exhibits

Optimization tests; ES/mean frontiers; out-of-sample risk and wealth table; constraint feasibility ledger and sensitivity.

## Minimum viable thesis

Ten industries, historical-scenario LP, equal-weight and variance benchmark, rolling evaluation and realized ES uncertainty.

## Scope and feasibility

Tail estimation error and changing dependence matter; compare same risk/capital convention. No guarantee that ex-ante ES budget holds realized. Do not select risk budget or confidence level using test outcomes.

**Prerequisites:** Convex optimization, portfolio theory, risk measures, Python/SciPy.

**Optional extension:** Add shrinkage or distributionally robust ES with separate validation; include turnover penalty inside optimization.

## Milestones

W1-3: ES derivation and data; W4-6: LP and simulations; W7-9: rolling optimizer; W10-12: held-out evaluation; W13-16: write and reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
