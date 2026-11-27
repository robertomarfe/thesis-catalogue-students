# Research plan | D03.02.01

## Study design and independent work

Record the origin, last training label end and target end for each forecast. An average and a sum differ by the horizon; compare only matching units. Report all horizons and null rankings.

## Required tasks

1. Construct daily, 5-day and 22-day variance proxies and forward targets; verify alignment on a hand example.

2. Fit direct HAR and GARCH; use a fixed small positive floor learned from training only and report frequency of clipping.

3. Evaluate MAE, MSE and QLIKE=log(forecast)+realization/forecast on identical observations.

4. Use HAC or paired block bootstrap for loss differences and compare nonoverlapping evaluation dates.

5. Inspect coefficients, crisis versus calm loss differences and changes from adding weekly/monthly components.

## Required exhibits

Forecast alignment tests, coefficient tables, OOS loss and interval tables by horizon, forecast and cumulative loss plots, floor and stability diagnostics.

## Robustness

Do not equate daily-based variance with intraday realized variance. Avoid overlapping-label leakage and future realized variance as predictor. GARCH forecast of conditional second moment must be compatible with return demeaning. No claim of universally superior forecasts from one holdout.

## Minimum viable thesis

Common daily panel, HAR-h, GARCH and historical benchmark for all three horizons, chronological evaluation with QLIKE/MSE and horizon-aware uncertainty.

## Optional extension

If public intraday realized measures with documented market coverage become available, compare an original HAR-RV specification on a matched sample.

## Prerequisites

Time-series regression, GARCH, forecasting and Python (arch or equivalent).

## Thesis outline

1. Volatility persistence;

2. HAR and GARCH forecasts;

3. Daily-return data and timing;

4. Multi-horizon forecast evaluation;

5. Economic and measurement limitations.

## Milestones

W1-3: volatility theory and loss functions; W4-6: data/target construction; W7-9: forecast models; W10-12: holdout and inference; W13-16: stability and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
