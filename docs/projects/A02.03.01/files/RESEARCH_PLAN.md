# Research plan | A02.03.01

## Study design and independent work

Toy equal weights sum to one; no immature loss in the adaptive window; perturb future targets and verify earlier weights unchanged; audit common component availability and fixed predictor membership.

## Prespecified implementation

Predeclare seven Goyal predictors and common sample before outcome inspection. At origin t combine individual expanding forecasts using equal weights and inverse MSE on last 120 common matured forecast errors; never in-sample residuals. If fewer matured errors, use available documented history or equal weights under a fixed minimum. Freeze validation decisions before test.

## Required tasks

1. Verify predictor transformations, chronological information sets and target return arithmetic.

2. Reproduce each single-variable and historical mean forecast with expanding coefficients.

3. Evaluate equal/median and inverse past-loss combinations; compare OOS R^2, MSFE and direction accuracy.

4. Decompose forecast-error covariance and weights; use paired time-block bootstrap (including re-estimation where feasible) and Clark-West only for appropriate nested comparisons.

5. Compare rolling versus expanding estimation and crisis versus other periods; optional clipped mean-variance portfolio with costs.

## Required exhibits

Forecast ledger, model and combination score tables, error correlations, cumulative squared-error differential plots, weight stability.

## Robustness

Do not use full-sample error estimates to choose weights or omit underperforming predictors ex post. Predicted returns may be economically small even if R^2 positive. Latest revised data are pseudo-OOS, not full vintage replication.

## Minimum viable thesis

Seven fixed individual models (or documented common available subset), equal and adaptive combination, historical mean and chronological inference. Distinct from A10.01.01 regularized multivariate regression.

## Optional extension

Forecast encompassing, shrinkage of weights toward equal or regime-dependent combination with separate validation.

## Prerequisites

OLS, forecast evaluation, time-series econometrics, Python.

## Thesis outline

1. Predictability and model uncertainty;

2. Combination theory;

3. Real-time design;

4. Forecast comparisons;

5. Economic interpretation.

## Milestones

W1-3: predictors and theory; W4-6: data ledger; W7-9: individual/combined forecasts; W10-12: inference and robustness; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
