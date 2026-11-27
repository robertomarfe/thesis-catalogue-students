# Research plan | A10.01.02

## Study design and independent work

Check factor signs, dates, percent scaling, source vintage and lags. Keep all three factor loss gains together in resampling. Freeze OLS specification; negative R2 and weak gains allowed; no selected winner p-value.

## Prespecified implementation

Build factor-specific SMB,HML,Mom targets in decimal; no RF subtraction from spreads. Features common Goyal dp/tms/dfy/tbl plus lagged own factor. For each target tune ridge and LASSO by prior dates and use factor-specific recursive mean. Joint date-block bootstrap across three loss gains; funding/collateral needed for economic factor timing.

## Required tasks

1. Construct one-month-ahead factor labels, predictor timing and common sample.

2. Implement historical mean, OLS with same X, ridge and LASSO; use a prespecified penalty grid and rolling-origin validation.

3. Report factor-by-factor OOS R2, MAE, cumulative squared loss and paired block intervals.

4. Report joint evidence across three factors using a common-date max-statistic or multiple-testing adjustment.

5. Inspect coefficients and stability, and optionally compute risk-scaled factor exposure using lagged risk and declared leverage/costs.

## Required exhibits

Chronological split ledger, tuning curves, OOS forecast and loss files, factor-specific performance table, coefficient paths and multiple-testing diagnostics.

## Robustness

Do not apply random cross-validation or standardize on full sample. Keep target menu fixed; revised macro predictors are pseudo-real-time unless vintages are recovered. Do not call long-short factor timing net-investment returns without a funding convention. Distinct from A10.01.01 aggregate equity premium forecasts.

## Minimum viable thesis

Three factors, four benchmarks/models, nested chronological validation, untouched holdout and joint uncertainty assessment; negative R2 acceptable.

## Optional extension

Compare a multitask ridge or group-penalized specification, with separate validation and fixed out-of-sample evaluation.

## Prerequisites

Factor models, regression, regularization, time-series validation and Python (scikit-learn).

## Thesis outline

1. Time-varying factor premia;

2. Regularization and validation;

3. Predictors and information timing;

4. OOS evidence across factors;

5. Economic interpretation and limitations.

## Milestones

W1-3: factor and ML literature; W4-6: data and chronological splits; W7-9: models and nested tuning; W10-12: holdout and joint tests; W13-16: robustness and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
