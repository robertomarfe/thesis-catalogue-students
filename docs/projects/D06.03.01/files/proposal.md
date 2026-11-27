---
title: "Pricing and Risk Decomposition of Capital-Protected Notes"
subtitle: "Research proposal | D06.03.01"
---

**Derivatives · Numerical pricing and exotics · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Principal protection uses part of issue proceeds to finance a promised maturity floor, leaving a residual budget for equity exposure. Low yields, fees and issuer credit therefore affect attainable participation. The project studies the financing constraint and distinguishes promised from reliable protection.

## Research question

How do yield level, volatility, fees and issuer credit affect attainable equity participation and the economic value of principal protection?

## Economic mechanism

For notional $N$, upfront fee fraction $f$, floor fraction $b$ and participation $\alpha$, the default-free budget is $N(1-f)=bND(0,T)+\alpha NC/S_0$. A negative option budget means infeasibility.

## Research design

Use the prescribed rates, volatilities, fees, maturities and independent zero-recovery issuer scenarios. Reconcile default-free replication before credit discounting and physical loss scenarios; the optional sovereign curve is not an issuer curve.

Reconcile components and proceeds for feasible scenarios; retain infeasible ones. Separate Q prices and P losses. The optional GSW curve is sovereign, not issuer funding or collateral.

\newpage

## Required exhibits

Payoff and decomposition diagrams, participation surfaces, feasibility and risk tables, simulated terminal return distributions.

## Minimum viable thesis

Default-free replication, feasible budget grid and unsecured zero-recovery scenario; no observed structured-note data required. Distinct from D06.03.02's autocallable complexity.

## Scope and feasibility

Principal protection holds only at maturity and conditional on issuer performance unless genuinely collateralized. Q fair value and P loss distribution distinct; zero recovery is a scenario. Not investment advice or a dealer quote. Fixed fees and rates are assumptions, not observed spreads.

**Prerequisites:** BSM, discount curves, default intensity basics, simulation.

**Optional extension:** Compare capped participation, collateralization or alternative market-consistent recovery specification.

## Milestones

W1-3: derive note price; W4-6: code validation; W7-9: participation and Greeks; W10-12: P payoff/credit scenarios; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
