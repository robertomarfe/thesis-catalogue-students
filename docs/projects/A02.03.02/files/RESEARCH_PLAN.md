# Research plan | A02.03.02

## Study design and independent work

Hand-check weighted least squares on a toy matrix; rolling window never uses an immature label; freeze menu before holdout; report MC uncertainty and stable-null behavior; do not optimize break location on final errors.

## Prespecified implementation

Fixed expanding, rolling 120/240 months and exponentially weighted OLS half-life 120. Predeclare collinearity rule using training data only. In artificial piecewise slope scenario compare adaptation delay, then actual common dates; no ex-post breakpoint used to forecast. Use historical mean baseline.

## Required tasks

1. Simulate persistent predictor with null, fixed beta and one break, 500 seeded paths; compare forecast errors and break-test size/power.

2. Plot rolling coefficients and intervals; implement trimmed full-sample break statistic using appropriate bootstrap.

3. Generate recursive forecasts with fixed windows and same information, expanding historical mean.

4. Compare OOS R2 and block-bootstrap loss differences on common dates; predefine subperiods 1970-1999 and 2000-2025 as feasible.

5. Stress persistent predictors and valuation definitions, alternative lags; report negative results and instability without ex post timing.

## Required exhibits

Simulated bias-variance curves, coefficient paths, break-statistic diagnostics, recursive forecast and loss tables.

## Robustness

Full-sample break date cannot be used in real-time prediction. Rolling estimates are correlated; naive t-tests over dates invalid. Persistent predictor and endogenous innovations require careful bootstrap. Distinct from forecast combinations (A02.03.01).

## Minimum viable thesis

Simulation and common-date empirical comparison of three window schemes, one predictor and historical-mean benchmark; descriptive break analysis.

## Optional extension

Online change detection or Bayesian time-varying coefficients with past-only tuning.

## Prerequisites

Time-series regressions, rolling estimation, bootstrap, Python.

## Thesis outline

1. Predictability and instability;

2. Estimators and inference;

3. Simulation;

4. Empirical forecasts;

5. Conclusions.

## Milestones

W1-3: theory/simulation; W4-6: data and timing; W7-9: break diagnostics; W10-12: forecasts; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
