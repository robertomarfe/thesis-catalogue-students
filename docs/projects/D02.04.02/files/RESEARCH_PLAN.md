# Research plan | D02.04.02

## Study design and independent work

Do not replace missing market history with a synthetic study without approval. Freeze the supported nodes, complete session calendar, chronological boundaries and purge. Preserve measurement masks and compare the same targets, including failed or arbitrage-violating forecasts.

## Required tasks

1. Validate permission, dates, surface definitions, interpolation support and missingness.

2. Test grid construction on arbitrage-free synthetic examples; log observed versus interpolated nodes.

3. Fit train-only PCA, persistence, cellwise AR and factor AR/VAR; choose dimension and penalty on validation.

4. Forecast 1,5,20 trading days, score held-out w and IV on identical nodes and dates, report spread-aware error where available.

5. Use paired block bootstrap by date, stress periods and finite-grid forecast arbitrage diagnostics without retrospective refit.

## Required exhibits

Coverage heatmap, fixed factor loadings, held-out error by tenor/moneyness, paired uncertainty, representative predicted and realized surface plots.

## Robustness

No random row splits, forward-filled labels or look-ahead PCA. Interpolation error is part of measurement, not observed quote error. Forecast skill is not trading profit. Vendor-derived IV surface is model-dependent; do not mix definitions without audit.

## Minimum viable thesis

Permission and adequate chronology, fixed supported grid, persistence versus PCA-AR on held-out dates, common-node scoring and leakage audit.

## Optional extension

Evaluate arbitrage-projected forecasts and whether projection helps or hurts held-out accuracy, or compare direct multi-horizon models.

## Prerequisites

Options, time-series forecasting, PCA, interpolation, Python; permitted longitudinal surface data.

## Thesis outline

1. Surface dynamics;

2. Fixed grid and factors;

3. Data and timing;

4. Forecast comparison;

5. Robustness and scope.

## Milestones

W1-3: acquire permission and assess sample; W4-6: grid and timing; W7-9: train/validation; W10-12: held-out and robustness; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
