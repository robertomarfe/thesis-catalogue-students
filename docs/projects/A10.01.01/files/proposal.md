---
title: "Regularized Regressions for Equity Premium Forecasting"
subtitle: "Research proposal | A10.01.01"
---

**Asset pricing · Predictability and machine learning · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Many correlated predictors make OLS unstable when the historical sample is short. Penalization exchanges bias for lower estimation variance; its benefit must be measured after counting the cost of tuning, not with a penalty selected on the test set.

## Research question

Do ridge, LASSO or elastic-net regressions improve one-month equity premium forecasts relative to the historical mean and ordinary least squares? Are improvements robust to tuning and evaluation windows?

## Economic mechanism

Regularized squared-error forecasts trade estimation variance for bias by shrinking training-standardized coefficients.

## Research design

Use the seven frozen Goyal predictors, target 1927–2025 where feasible; train through 1964, development 1965–1999 and final 2000–2025. Mean/OLS/ridge/LASSO use identical origins and inner chronological tuning; elastic net optional.

Persist scaler means/SD and mature fold IDs; perturb future features and immature labels; earlier tuning and forecasts must be invariant. Check zero penalty against OLS when rank permits; document alpha conventions and zero-variance features.

\newpage

## Required exhibits

Predictor and coefficient plots, reproducible nested temporal split diagram, forecast series, OOS R2/loss table with uncertainty, selected penalty history and sample/timing log. Distinguish statistical accuracy from any optional economic value.

## Minimum viable thesis

Verified author file, fixed target and predictor list, mean/OLS/ridge/LASSO with nested chronological tuning, common untouched evaluation period, loss uncertainty and reproducible pipeline. Elastic net may be secondary if time is limited.

## Scope and feasibility

Prevent scaling, imputation, feature selection and outcome leakage; no full-sample winsorization. Verify one-month shift with a toy series and historical mean using only observed past returns. Compare fixed/expanding training and a prespecified subset of readily observed predictors. Treat revised data and release timing as limitations; do not tune using final results.

**Prerequisites:** OLS, matrix algebra, basic regularization, scikit-learn pipelines, time-series evaluation.

**Optional extension:** Evaluate a prespecified capped mean-variance timing rule with realistic lag and hypothetical costs; compare with nonlinear method only after core tests.

## Milestones

W1-3: verify Goyal file and model theory; W4-6: clean data and test temporal pipeline; W7-10: fit/tune on development and run locked test; W11-13: uncertainty and sensitivities; W14-16: write and reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
