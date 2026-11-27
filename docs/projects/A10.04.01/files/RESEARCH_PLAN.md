# Research plan | A10.04.01

## Study design and independent work

Hand-check daily squared-return aggregation and annualization (same for forecast and target); record zero/clipped values; check availability ledger and positive forecasts. Permute grouped blocks, not rows; distinguish importance variability from loss uncertainty.

## Prespecified implementation

Construct next-month sum squared daily market log returns (or centered simple squares consistently as declared); use same target and past 1/3/12-month realized variance. VIX^2/12 in decimal units approximates monthly Q variance; horizon mismatch disclose, NFCI/GS10/TB3MS lagged. Train linear/HAR and shallow RF/boost on identical inputs; require positive forecasts for QLIKE with predeclared floor, report clipping. Group correlated predictors for permutation importance on validation only; final attributions descriptive, no tuning.

## Required tasks

1. Establish chronological feature/label audit and benchmark HAR-style forecast.

2. Fit GLM, forest and boosting and compare QLIKE/MSE on common dates.

3. Compute block permutation and grouped importance (volatility features together), repeating with different block sizes; show held-out fold stability.

4. Plot partial dependence with observed support, compare local effects, and quantify ranking changes.

5. Repeat excluding VIX or crisis observations and report paired block-bootstrap scores and uncertainty.

## Required exhibits

Feature timing table, forecast comparison, fold-wise importance panels, effect plots with support, robustness and uncertainty table.

## Robustness

Permutation of time series can break dependence and create unrealistic feature combinations. Treat importance as model-specific predictive attribution, not a causal effect or risk price. No tuning on test folds. Daily-return proxy is not high-frequency realized variance; VIX is Q implied variance proxy.

## Minimum viable thesis

Linear and two tree methods, time-safe forecasts, grouped importance and stability evaluation. Distinct from A10.02.01 (return forecasts) and D03.01.01 (volatility model horse race).

## Optional extension

SHAP with explicitly documented dependence assumptions, or compare explanation stability with monotone constrained models.

## Prerequisites

Regression, tree models, time-series validation, Python and visualization.

## Thesis outline

1. Volatility forecasting;

2. Interpretability and limitations;

3. Data and validation;

4. Performance and explanations;

5. Conclusions.

## Milestones

W1-3: target and literature; W4-6: data and linear benchmark; W7-9: trees and validation; W10-12: interpretation and robustness; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
