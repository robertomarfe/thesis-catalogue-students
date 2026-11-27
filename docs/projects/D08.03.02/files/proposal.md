---
title: "Put Writing and the Compensation for Downside Risk"
subtitle: "Research proposal | D08.03.02"
---

**Derivatives · Hedging and volatility derivatives · Level 2/3**

**Data:** Empirical design blocked pending authorized access and coverage; not assignable on this design. **Status:** current review draft; supervisor approval pending.

## Motivation

Cash-secured put writing earns premium while retaining nonlinear downside exposure. Its apparent return advantage may reflect different risk or collateral conventions. Test compensation against ex-ante risk-matched stock-cash portfolios.

## Research question

Does the performance of a put-writing benchmark survive comparison with equity/cash portfolios at comparable ex-ante risk, particularly in turbulent markets?

## Economic mechanism

Collateral growing to $K$ and a short put pay $K-(K-S_T)^+=\min(S_T,K)$ before separate premium accrual.

## Research design

Use authorized PUT history, market total-return comparator and risk-free series. Match common months and lagged risk, assess turbulent-market losses, and verify collateral and roll methodology.

Focus on downside compensation and collateral rather than D08.03.01's upside capture. Defer or explicitly approve redesign if PUT rights or history fail. No silent BXM or synthetic substitution.

\newpage

## Required exhibits

Payoff diagram; common-sample summary and wealth plots; tail/capture statistics; matched-risk and regime table.

## Minimum viable thesis

Authorized PUT series plus equity total-return comparator or labeled French proxy, matched-risk comparison and tail-loss analysis. If PUT unavailable, defer or approve a synthetic redesign.

## Scope and feasibility

PUT is a hypothetical index, not directly investable; do not use price-only S&P500 as benchmark. Avoid interpreting the spread in returns as pure variance premium. Rights, actual data history and launch dates are gates. Costs and collateral yield are not silently ignored.

**Prerequisites:** Option payoff algebra, portfolio statistics, time-series inference and Python.

**Optional extension:** Compare PUT and BXM with documented collateral and roll differences; incorporate trading-cost scenarios.

## Milestones

W1-3: contract/index methods and download gate; W4-6: data alignment; W7-9: matched-risk benchmarks; W10-12: tail and regime checks; W13-16: write/reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
