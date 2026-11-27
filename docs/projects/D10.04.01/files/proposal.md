---
title: "Currency Option Pricing and Interest Rate Differentials"
subtitle: "Research proposal | D10.04.01"
---

**Derivatives · International finance, FX and commodities · Level 1/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Currency options depend on two interest rates. Their effects operate through discounting and the forward, so a comparison at fixed spot strike differs from a comparison at matched forward moneyness. Hedging must account for interest on the foreign cash position.

## Research question

How do domestic and foreign rates affect currency option prices and hedge ratios, and how much of the effect is mediated by forward moneyness?

## Economic mechanism

With $S$ USD/EUR, $F=Se^{(r_d-r_f)T}$ and the domestic price discounts the domestic-currency payoff at $r_d$.

## Research design

Use the specified Garman--Kohlhagen grid, first holding K/S fixed across rate scenarios, then holding K/F fixed in a separate comparison. Derive Greeks at fixed contractual strike, verify against finite differences and use a domestic-cash/foreign-money-market delta ledger.

Check parity, fixed-strike sensitivities and self-financing ledger. Separate matched moneyness comparisons from Greeks. Keep quote orientation and foreign accrual explicit.

\newpage

## Required exhibits

Price and Greek grids; parity/finite difference checks; hedge error distribution; optional scenario charts.

## Minimum viable thesis

Synthetic Garman-Kohlhagen pricing and Greek sensitivity with both rate and moneyness conventions. Delta ledger tested; historical inputs optional.

## Scope and feasibility

Quote direction and units fixed. Money market yields are not necessarily risk-free or collateralized. Use domestic discounting and foreign accrual consistently; no claims about FX basis or market implied volatility from synthetic prices.

**Prerequisites:** BSM, probability, FX conventions, basic Python.

**Optional extension:** Two deterministic term structures or stochastic rates and quanto adjustments.

## Milestones

W1-3: derivation; W4-6: pricer and Greeks; W7-9: rate grid; W10-12: ledger and optional replay; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
