---
title: "Protective Puts and the Cost of Crash Insurance"
subtitle: "Research proposal | D08.04.01"
---

**Derivatives · Hedging and volatility derivatives · Level 2/3**

**Data:** Empirical design blocked pending authorized access and coverage; not assignable on this design. **Status:** current review draft; supervisor approval pending.

## Motivation

A rolling protective-put index may limit large losses at the cost of repeated insurance purchases. Its realized protection depends on contract design and market history, and must be compared with lower equity exposure rather than attributed mechanically to put premiums.

## Research question

How much downside protection does a systematic protective-put strategy provide relative to buy-and-hold and risk-matched stock-cash allocations, and at what realized return cost?

## Economic mechanism

Stock plus put pays $\max(S_T,K)$; with financed premium $P_0$, terminal wealth subtracts $P_0e^{rT}$.

## Research design

Obtain authorized PPUT and common total-return comparator or declared proxy. Assess monthly risk-matched performance and tail outcomes, with a small synthetic roll illustration; separate live and backfilled periods.

Unlike D08.04.02, this is historical rolling insurance evaluation. Gate remains blocked. Report achieved risk and uncertainty; simulation-only redesign needs explicit approval.

\newpage

## Required exhibits

Index provenance and comparator check; wealth/drawdown charts; risk-return and stress table; synthetic insurance-cost decomposition.

## Minimum viable thesis

Authorized PPUT and comparator, historical risk-matched comparison and a small transparent synthetic payoff exercise, or approved simulation variant.

## Scope and feasibility

Do not use price-only SP500; distinguish hypothetical index, trade costs and actual investability. Tail estimates imprecise; no claim of optimal insurance. If rights or history unavailable, switch to synthetic-only variant only with supervisor approval and revise empirical claim.

**Prerequisites:** Options, portfolio returns, risk measures, bootstrap, Python.

**Optional extension:** Compare puts with put spreads at common budget, separating protection and cap.

## Milestones

W1-3: acquisition/rights and payoff; W4-6: index validation; W7-9: benchmarks; W10-12: tail and synthetic attribution; W13-16: writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
