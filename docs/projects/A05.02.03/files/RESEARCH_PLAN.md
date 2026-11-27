# Research plan | A05.02.03

## Study design and independent work

Implement a strong DNS baseline independently before ML. Lock temporal validation and data features, log all tuning choices and missing outcomes, and never select the final model using the final test loss.

## Required tasks

1. Validate yield units and fixed maturities, fit Nelson-Siegel loadings with decay fixed or selected on training.

2. Implement random walk, separate AR, factor VAR and ridge; add shallow boosted trees if sample permits.

3. Select hyperparameters using chronological splits with label-end purging for h>1.

4. Freeze model-selection protocol and compare forecasts at common origins; compute per-maturity and pooled errors, paired loss inference with HAC/block bootstrap.

5. Compare regimes, recursive versus rolling training and yield-change versus level targets.

## Required exhibits

Curve fit residual table; forecast error matrix; cumulative loss plot; tuning log; maturity/horizon robustness.

## Robustness

No random train/test split, full-sample scaling or future factor estimation. GSW yields are fitted not transactions. Overlapping forecast errors and common shocks require time-series inference. ML complexity must be limited; record failures and null improvement.

## Minimum viable thesis

GSW curve, random walk, AR/DNS and ridge or shallow tree, 1/3/12-month forecasts and locked temporal evaluation. Distinct from A05.02.01 DNS-only study.

## Optional extension

European AAA curve as external evaluation; compare forecasts of synthetic bond returns separately.

## Prerequisites

Fixed income, econometrics, regression/ML, Python and sklearn.

## Thesis outline

1. Yield curves and factor models;

2. Data and forecasting protocol;

3. Linear and ML methods;

4. Forecast comparisons;

5. Robustness.

## Milestones

W1-3: theory and design; W4-6: curves and benchmarks; W7-9: ML and tuning; W10-12: locked evaluation; W13-16: documentation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
