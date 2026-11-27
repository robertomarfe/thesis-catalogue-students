---
title: "Focused methods — Interest Rates and the Predictability of Stock Market Excess Returns"
subtitle: "A02.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

Let $y_{t+1}=R_{m,t+1}-R_{f,t+1}$ in decimal units. Set $s_t=i^{10y}_t-i^{3m}_t$ after documenting the yield conventions and availability. Compare forecasts from $x_t=dp_t$, $x_t=(i^{3m}_t,s_t)$ and their union with the matured historical mean. For losses $L_{j,t}=(y_{t+1}-\widehat y_{j,t})^2$, define $R^2_{OS,j}=1-\sum_t L_{j,t}/\sum_t L_{0,t}$. Incremental value beyond valuation is measured by paired $L_{dp,t}-L_{both,t}$, not a causal effect. Treasury yields are predictor levels, not the realized risk-free return in the dependent variable.

## Identification and implementation

For a genuinely nested squared-error comparison, let $f_0,f_1$ be restricted and unrestricted forecasts. The Clark–West adjusted difference is $e_0^2-e_1^2+(f_0-f_1)^2$. Report unadjusted paired loss as the economic forecast comparison. The adjustment is not a generic test for nonnested competitors.

## Research checks

First three forecasts recomputed by hand; no forward fill from later observations; exact common evaluation origin list; risk-free and yield units checked separately. Negative OOS R2 retained.
