---
title: "Focused methods — No-Trade Bands for Option Hedging"
subtitle: "D04.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## State-dependent decisions
When $|d_i|>b$, a reset rule trades to $\Delta_i$, while a boundary rule trades to $\Delta_i-b\operatorname{sgn}(d_i)$. Both use only current information. Opening and compulsory liquidation must be treated consistently, independently of the band rule.

## Cost and tail constraint
Use the discounted seller loss, including opening, rebalancing and closing costs. Expected shortfall at confidence $\alpha$ averages the upper $1-\alpha$ loss mass, with fractional boundary weight if needed. Select feasible bands by training costs subject to a predeclared tail constraint. Report infeasibility instead of silently relaxing it. Compare paired test differences and risk-cost frontiers.

## Research checks

Report achieved risk, not merely the intended budget. The comparison must use the same opportunities, shares, premium and cost convention across policies; this is not a neural-policy training study.
