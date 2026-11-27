---
title: "Macroeconomic Forecast Disagreement and Equity Market Risk"
subtitle: "Research proposal | A04.01.02"
---

**Asset pricing · Macro-finance and policy risk · Level 2/3**

**Data:** Empirical design conditional on actual access and coverage. **Status:** current review draft; supervisor approval pending.

## Motivation

Cross-sectional disagreement about future output can contain information that a mean forecast misses. Disagreement measures heterogeneity, not the conditional variance of growth or a structural uncertainty shock.

## Research question

Does forecast disagreement about next-quarter real output growth add predictive information about subsequent equity volatility beyond past volatility and mean expected growth?

## Economic mechanism

Let $D2_q$ denote the published interquartile range of individual annualized next-quarter growth forecasts. Define quarterly variance $V_q=\sum_{d\in q}r_d^2$ from daily total log returns.

## Research design

SPF D2 RGDP and matched mean growth; daily US market from the Ken French library variance on independently checked session calendar; nested expanding regressions, QLIKE and log-MSE, 80-quarter warm-up.

Match D2 and mean RGDP at the same vintage and q+1 horizon. Audit exchange calendar independently; mark a missing daily return as missing quarterly RV. Show an 80-quarter warmup and only matured next-quarter RV; use training-only log smearing, matched QLIKE and log-MSE with paired blocks; GDP-only robustness.

\newpage

## Required exhibits

Survey and market date ledger; descriptive plots; coefficient and forecasting tables; sensitivity to horizons and sample.

## Minimum viable thesis

One D2 RGDP series, EG and daily market RV, release-aligned quarterly regression and expanding evaluation.

## Scope and feasibility

SPF dispersion D2 is IQR, not realized EG volatility, and survey horizon must be constant. Avoid current-quarter returns preceding release and using GDP levels across incompatible vintages. Revised data are pseudo-real-time; no causal claim.

**Prerequisites:** Financial econometrics, macro data, forecasting, Python.

**Optional extension:** Use individual forecast responses to separate within-forecaster revisions and cross-sectional dispersion, if authorized and documented.

## Milestones

W1-3: survey conventions and readings; W4-6: merge and variables; W7-9: regressions; W10-12: OOS/robustness; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
