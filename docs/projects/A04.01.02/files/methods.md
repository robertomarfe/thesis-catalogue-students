---
title: "Focused methods — Macroeconomic Forecast Disagreement and Equity Market Risk"
subtitle: "A04.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

Let $D2_q$ denote the published interquartile range of individual annualized next-quarter growth forecasts. Define quarterly variance $V_q=\sum_{d\in q}r_d^2$ from daily total log returns.

Fit $\log V_{q+1}=a+b\log V_{q-1}+c EG_q+d D2_q+e_{q+1}$ using the preceding completed quarter at survey release. The log-model level forecast requires a training-only smearing factor $\widehat E[\exp(e)]$; exponentiation alone is not a mean forecast. Score positive forecasts $f$ by $L(V,f)=V/f-\log(V/f)-1$ and log errors on common dates. Check complete exchange sessions independently; do not fill missing returns with zero. Require 80 matured quarters before evaluation. Do not pool GNP and GDP without a documented historical splice and GDP-only sensitivity.

## Research checks

Match D2 and mean RGDP at the same vintage and q+1 horizon. Audit exchange calendar independently; mark a missing daily return as missing quarterly RV. Show an 80-quarter warmup and only matured next-quarter RV; use training-only log smearing, matched QLIKE and log-MSE with paired blocks; GDP-only robustness.
