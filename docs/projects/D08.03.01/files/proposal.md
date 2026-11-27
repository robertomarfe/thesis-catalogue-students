---
title: "Covered Calls versus Buy-and-Hold: Risk and Performance"
subtitle: "Research proposal | D08.03.01"
---

**Derivatives · Hedging and volatility derivatives · Level 2/3**

**Data:** Empirical design blocked pending authorized access and coverage; not assignable on this design. **Status:** current review draft; supervisor approval pending.

## Motivation

Covered-call indices can display lower volatility because some equity upside is sold. Comparing with unscaled buy-and-hold confounds reduced risk exposure with insurance value. Evaluate against a feasible lagged risk-matched equity/cash portfolio.

## Research question

How much upside does a covered-call benchmark sacrifice, and does its downside protection survive comparison with a volatility-matched equity/cash portfolio?

## Economic mechanism

The one-period covered call pays $S_T-(S_T-K)^+=\min(S_T,K)$ before accounting for the premium. A rolling total-return index is not this payoff.

## Research design

Obtain authorized BXM and the prescribed total-return comparator or labeled French proxy. Form common monthly returns, risk and capture statistics, and a trailing volatility-matched benchmark. Separate backfill from live history.

This is historical buy-write evaluation, not synthetic hedge optimization. Gate remains blocked until BXM rights and history pass. Price-only SP500 is not an admissible comparator; no pure option-premium interpretation.

\newpage

## Required exhibits

Payoff diagram; wealth/drawdown plots; paired performance, capture and beta table; volatility-matched comparison.

## Minimum viable thesis

BXM plus authorized equity total-return comparator/proxy, monthly paired returns, risk/capture and trailing volatility-matched baseline. If BXM unavailable, defer assignment; synthetic-only redesign needs approval.

## Scope and feasibility

BXM is a hypothetical benchmark, not actual investor returns. Price-only SP500 is invalid as total-return comparator. Proxy basis risk, taxes, costs and index methodology must be disclosed; do not infer pure option premium from differences.

**Prerequisites:** Option payoffs, total returns, portfolio metrics, regression and bootstrap.

**Optional extension:** Add BXMD or BXY if complete authorized histories exist; compare strike selection.

## Milestones

W1-3: payoff and data gate; W4-6: clean indices; W7-9: performance and exposures; W10-12: risk-matched and robustness; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
