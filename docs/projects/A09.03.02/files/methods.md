---
title: "Focused methods — Carry as a Cross-Asset Investment Factor"
subtitle: "A09.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Carry versus returns
A carry signal is a conditional return component under specified unchanged-price or curve assumptions, not a realized total payoff. Use only the published realized strategy-return sleeves and their definitions of risk scaling, financing, roll and currency. Do not pool the aggregate with its own constituents. Treat original and updated workbooks as separate vintages.

## Composite construction
With $J$ sleeves, the equal-weight payoff uses $w_j=1/J$. For a risk-scaled sensitivity, estimate $\widehat\sigma_{j,t}$ on a trailing window ending at $t$, and prespecify a floor and cap before normalizing inverse-volatility weights. Test on $t+1$; keep all methods on the same dates. The covariance identity $\operatorname{Var}(w^\top c)=w^\top\Sigma w$ explains fixed-weight contributions, but dynamic weights require realized paired evaluation. Report gross notional, leverage convention and state-conditional intervals. Contemporaneous stress is descriptive, not a trading signal. Do not infer investable wealth from unfunded factors without a capital convention.

## Research checks

Confirm original workbook, documented units, at least three distinct sleeves, no composites or silent splicing. If the core is unavailable, defer. Record stress proxy timing, notional and common dates.
