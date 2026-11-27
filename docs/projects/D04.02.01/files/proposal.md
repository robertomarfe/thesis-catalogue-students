---
title: "Delta-Vega Hedging under Stochastic Volatility"
subtitle: "Research proposal | D04.02.01"
---

**Derivatives · Hedging and volatility derivatives · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Stochastic variance introduces a shock that the stock alone generally cannot span. A second option can reduce this exposure, but a small variance sensitivity can demand extreme positions. The benefit of additional spanning must be measured net of trading and numerical conditioning.

## Research question

When does a second traded vanilla option materially improve hedging of a target option in a stochastic-volatility market, net of rebalancing and conditioning risk?

## Economic mechanism

For target $C$ and hedge option $H$, match $h_H=C_v/H_v$ and $h_S=C_S-h_HH_S$, where $v$ denotes variance.

## Research design

Price the target and two hedge strikes under a common Heston Q law; simulate the specified P law. Compare delta-only and delta-variance policies on common paths at two frequencies, with costs and position caps.

Retain small-vega configurations and report unhedged exposures after caps. Compare identical premium, costs and paths; do not treat simulated option liquidity as observed market liquidity.

\newpage

## Required exhibits

Heston pricer checks, hedge exposure panels, P&L distributions, tail/turnover/cost tables, condition-number/vega threshold diagnostics.

## Minimum viable thesis

One target and two hedge strikes, validated prices and sensitivities, delta versus delta-vega on common paths at two frequencies, cost and ill-conditioning sensitivity. Distinct from single-stock discrete hedging studies.

## Scope and feasibility

This is a coherent simulated market, not evidence of traded option liquidity. A variance derivative is not volatility vega unless consistently rescaled. Distinguish Q pricer accuracy, P simulation bias, discrete hedging and cash-account errors; near-expiry Greeks and small vega can destabilize hedges.

**Prerequisites:** Stochastic calculus, options Greeks, Fourier integration, simulation and Python.

**Optional extension:** Hedge under model misspecification or optimize a constrained minimum-variance hedge with transaction costs.

## Milestones

W1-3: derive hedge ratios; W4-6: validate Heston pricer and DGP; W7-9: cash-ledger hedges; W10-12: sensitivity and costs; W13-16: tests, interpretation and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
