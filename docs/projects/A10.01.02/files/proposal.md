---
title: "Predicting Factor Returns with Machine Learning"
subtitle: "Research proposal | A10.01.02"
---

**Asset pricing · Predictability and machine learning · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Factor premia may vary with macro-financial state and their own lagged performance. The question is whether regularized forecasts generalize across distinct factor payoffs, not whether a selected winning factor is predictable.

## Research question

Do ridge and LASSO forecasts of monthly SMB, HML and momentum improve over factor-specific historical means and fixed OLS models in a genuinely held-out period?

## Economic mechanism

Each long-short factor payoff has its own conditional mean and forecast loss; pooling three winners after test invalidates joint inference.

## Research design

Use monthly French SMB/HML/Mom plus Goyal dp/tms/dfy/tbl and own lagged return. Training 1965–1994, validation 1995–2009 and test 2010–2025. Compare factor-specific mean, OLS, ridge and LASSO on identical dates.

Check factor signs, dates, percent scaling, source vintage and lags. Keep all three factor loss gains together in resampling. Freeze OLS specification; negative R2 and weak gains allowed; no selected winner p-value.

\newpage

## Required exhibits

Chronological split ledger, tuning curves, OOS forecast and loss files, factor-specific performance table, coefficient paths and multiple-testing diagnostics.

## Minimum viable thesis

Three factors, four benchmarks/models, nested chronological validation, untouched holdout and joint uncertainty assessment; negative R2 acceptable.

## Scope and feasibility

Do not apply random cross-validation or standardize on full sample. Keep target menu fixed; revised macro predictors are pseudo-real-time unless vintages are recovered. Do not call long-short factor timing net-investment returns without a funding convention. Distinct from A10.01.01 aggregate equity premium forecasts.

**Prerequisites:** Factor models, regression, regularization, time-series validation and Python (scikit-learn).

**Optional extension:** Compare a multitask ridge or group-penalized specification, with separate validation and fixed out-of-sample evaluation.

## Milestones

W1-3: factor and ML literature; W4-6: data and chronological splits; W7-9: models and nested tuning; W10-12: holdout and joint tests; W13-16: robustness and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
