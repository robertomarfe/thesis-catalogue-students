---
title: "The Term Structure of Implied Volatility in Equity Markets"
subtitle: "Research proposal | D02.01.02"
---

**Derivatives · Vanilla pricing and surfaces · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

An implied-volatility term structure combines expectations of future variance with compensation for bearing variance risk. Comparing a short index with a longer-horizon index may reveal useful information about the timing of risk, but the option-implied variance is a risk-neutral quantity and the forecast target is a physical realized variance proxy.

## Research question

Does the slope of the VIX and three-month implied variance curve improve forecasts of subsequent realized market variance relative to the VIX alone and a historical-variance benchmark?

## Economic mechanism

For annualized implied variances $v_a,v_b$ at maturities $T_a<T_b$, the forward-variance proxy is $(T_bv_b-T_av_a)/(T_b-T_a)$. It differs from a raw index slope and from expected physical realized variance.

## Research design

Align VIX and three-month implied-volatility indices with French daily broad-market returns. Compare forecasts of 30- and 90-calendar-day realized variance at common month-end origins, starting with pre-2016 training if coverage permits. Each forecast uses only outcomes matured by its origin.

Check common month-end dates and complete 30/90-calendar-day target intervals before fitting. Preserve the information set at every forecast origin; separate the implied level and forward proxy, and score common outcomes.

\newpage

## Required exhibits

Term structure and forward-variance time series, crisis plots, forecast error and coefficient tables, cumulative loss differences, data-coverage/negative-forward diagnostics and SPX proxy sensitivity. Report forecast gains or lack thereof in units of annualized variance.

## Minimum viable thesis

Verified two implied indices and return series, horizon-matched variance construction, level/slope/historical benchmark comparison in a chronological holdout, dependence-aware inference and economic interpretation of Q-P gap.

## Scope and feasibility

Use nonoverlapping quarterly forecasts as sensitivity, different calendar alignment and VIX-versus-SPX common sample. Never interpret French market RV as exact SPX underlying; separate baseline proxy from matched-index results. Report HAC/block-bootstrap dependence and revised series limits; no arbitrary deletion of inversion days.

**Prerequisites:** Volatility measures, OLS, time-series forecasting and pandas/statsmodels. No option chains required.

**Optional extension:** Add VIX9D or VIX6M only after checking coverage and maturity conventions; compare physical forward variance over days 31-90 rather than adding many regressors.

## Milestones

W1-3: verify index definitions and data; W4-6: construct aligned features/targets and test units; W7-10: estimate and forecast; W11-13: dependence and proxy robustness; W14-16: document and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
