---
title: "Autocallable Notes: Pricing and Embedded Risk"
subtitle: "Research proposal | D06.03.02"
---

**Derivatives · Numerical pricing and exotics · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

An autocallable note couples coupon and repayment timing to the path of observed equity prices. The coupon cannot be interpreted independently of expected life and downside exposure. The project uses one precise contract to study these trade-offs, rather than treating all notes as the same payoff.

## Research question

How do autocall and downside barriers change fair coupon, expected life and tail loss, and how sensitive are valuations to volatility, dividends and issuer credit?

## Economic mechanism

For fixed redemption rules write the discounted payoff as $A+cB_c$, where $A$ is principal PV and $B_c$ is coupon loading. Par pricing imposes $\mathbb E^{\mathbb Q}A+c\mathbb E^{\mathbb Q}B_c=1$.

## Research design

Use the specified three-year quarterly note, exact observation-date GBM and a cashflow truth table. Study fair coupon, redemption-time distribution, bump sensitivities and physical loss, with the coupon frozen in stress tests.

Validate first-call, no-call, equality and maturity paths by hand. Freeze coupon before physical stress. Report ratio uncertainty and infeasibility; do not confuse a stylized price with an issue quote.

\newpage

## Required exhibits

Cashflow specification and tests; fair coupon map; redemption-time and principal-loss distribution; Greek and stress table.

## Minimum viable thesis

One fully specified note, exact observation simulation, fair coupon and sensitivity grid, Q/P distinction and tested cashflow engine.

## Scope and feasibility

Discontinuous payoff makes naive pathwise Greeks unreliable; test bump sizes and sampling error. Coupon and barrier conventions must be explicit. Price is not an observed issue quote; independent issuer hazard is illustrative and excludes wrong-way risk.

**Prerequisites:** Risk-neutral pricing, Monte Carlo, derivative Greeks and Python.

**Optional extension:** Worst-of two-asset note with correlated GBMs; separate correlation sensitivity from single-name volatility.

## Milestones

W1-3: contract and pricing; W4-6: cashflow engine; W7-9: fair coupon and tests; W10-12: risk/stress; W13-16: documentation and thesis.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
