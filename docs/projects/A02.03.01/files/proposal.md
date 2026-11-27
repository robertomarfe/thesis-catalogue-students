---
title: "Combining Equity Premium Forecasts"
subtitle: "Research proposal | A02.03.01"
---

**Asset pricing · Predictability and machine learning · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Forecast combinations diversify parameter and model uncertainty without requiring a large joint regression. Adaptive weights may instead chase noise. The thesis separates combination benefits from extra opportunities to tune after the fact.

## Research question

Can simple forecast combinations outperform individual predictive regressions and the historical mean in a genuinely recursive evaluation?

## Economic mechanism

For weights summing to one, the combined forecast error is $e_c=w^\top e$. Its MSE is $w^\top E[ee^\top]w$.

## Research design

Use the seven Goyal candidates dp, ep, bm, tbl, tms, dfy, svar on common dates, proposed 1963–2025; train through 1989, validate 1990–1999, test 2000–2025. Compare mean, median and nonnegative inverse-MSE combinations of expanding regressions, with a 120 matured-error cap.

Toy equal weights sum to one; no immature loss in the adaptive window; perturb future targets and verify earlier weights unchanged; audit common component availability and fixed predictor membership.

\newpage

## Required exhibits

Forecast ledger, model and combination score tables, error correlations, cumulative squared-error differential plots, weight stability.

## Minimum viable thesis

Seven fixed individual models (or documented common available subset), equal and adaptive combination, historical mean and chronological inference. Distinct from A10.01.01 regularized multivariate regression.

## Scope and feasibility

Do not use full-sample error estimates to choose weights or omit underperforming predictors ex post. Predicted returns may be economically small even if R^2 positive. Latest revised data are pseudo-OOS, not full vintage replication.

**Prerequisites:** OLS, forecast evaluation, time-series econometrics, Python.

**Optional extension:** Forecast encompassing, shrinkage of weights toward equal or regime-dependent combination with separate validation.

## Milestones

W1-3: predictors and theory; W4-6: data ledger; W7-9: individual/combined forecasts; W10-12: inference and robustness; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
