---
title: "Focused methods — The Variance Risk Premium and the Predictability of Stock Market Returns"
subtitle: "A07.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Ex ante variance premium proxy
$Q_{t,30}$ is a VIX-based risk-neutral variance proxy, not a precise traded variance-swap quote. Estimate $P_{t,30}$ from forecasts of daily squared log SPX returns summed over scheduled sessions in the next 30 calendar days. Then $Q-P$ is known at formation. Substituting realized future variance for $P$ creates a look-ahead variable; ex post differences may be reported separately.

## Predictive regression
At month-end $t$, form a target $R^e_{t,t+H}=\prod_{j=1}^H(1+R_{m,t+j})-\prod_{j=1}^H(1+R_{f,t+j})$, where $R_m$ is total simple market return and $R_f$ is bill return. Estimate a historical mean and a regression on the lagged proxy at identical dates. Admit training labels only when their full horizon has matured. Use HAC or joint blocks for overlapping three-month outcomes; report one-SD effects and OOS loss, not just in-sample significance.

## Research checks

The matched SPX source remains blocked until rights and actual coverage are confirmed. Short samples may support descriptive results only; long-proxy OOS analysis requires explicit supervisor agreement. No silent source substitution or claim of an intraday replication.
