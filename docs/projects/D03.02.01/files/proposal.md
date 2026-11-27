---
title: "Multi-Horizon Volatility Forecasting with HAR Models"
subtitle: "Research proposal | D03.02.01"
---

**Derivatives · Volatility forecasting and tail risk · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Market variance evolves on multiple time scales. Daily, weekly and monthly histories may summarize persistent volatility without imposing a fully specified latent process. This thesis asks whether that parsimony improves genuine forecasts, not whether a richer regression fits the past.

## Research question

Do multi-scale variance components improve out-of-sample forecasts of average daily squared market returns at one-, five- and twenty-two-day horizons relative to GARCH and historical averages?

## Economic mechanism

For daily squared innovations $v_t=u_t^2$, the direct HAR target at horizon $H$ is $Y_{t,H}=H^{-1}\sum_{j=1}^{H}v_{t+j}$; predictors are trailing means at 1, 5 and 22 trading days.

## Research design

Estimate a separate HAR regression for each horizon and compare a trailing mean and GARCH on the identical daily panel. Enforce a mature-label cutoff at every monthly refit and compare losses across the predeclared horizons, not across different units.

Record the origin, last training label end and target end for each forecast. An average and a sum differ by the horizon; compare only matching units. Report all horizons and null rankings.

\newpage

## Required exhibits

Forecast alignment tests, coefficient tables, OOS loss and interval tables by horizon, forecast and cumulative loss plots, floor and stability diagnostics.

## Minimum viable thesis

Common daily panel, HAR-h, GARCH and historical benchmark for all three horizons, chronological evaluation with QLIKE/MSE and horizon-aware uncertainty.

## Scope and feasibility

Do not equate daily-based variance with intraday realized variance. Avoid overlapping-label leakage and future realized variance as predictor. GARCH forecast of conditional second moment must be compatible with return demeaning. No claim of universally superior forecasts from one holdout.

**Prerequisites:** Time-series regression, GARCH, forecasting and Python (arch or equivalent).

**Optional extension:** If public intraday realized measures with documented market coverage become available, compare an original HAR-RV specification on a matched sample.

## Milestones

W1-3: volatility theory and loss functions; W4-6: data/target construction; W7-9: forecast models; W10-12: holdout and inference; W13-16: stability and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
