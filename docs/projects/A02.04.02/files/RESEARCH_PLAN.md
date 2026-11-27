# Research plan | A02.04.02

## Study design and independent work

Hand-check pinball loss for positive and negative residuals and empirical quantile convention. Check VIX availability and no future data. Test crossing detection, report event counts, no post-test choice of quantile or rearrangement.

## Prespecified implementation

At least q=.10,.50,.90 (freeze probabilities before test). Quantile regression with identical past features dp and end-month available VIX. Compare expanding empirical quantile and rolling 60-month Gaussian location-scale. Use pinball and coverage, note crossing, predeclare noncrossing rearrangement as sensitivity rather than hiding failures. No future volatility in features.

## Required tasks

1. Construct predictor/target timing ledger and units.

2. Fit unconditional and location-scale benchmarks.

3. Estimate quantile regressions using lagged valuation and log VIX, freeze model form.

4. Compare quantile scores, interval coverage and paired block bootstrap.

5. Evaluate crossing, tail event counts, crisis sensitivity and risk decision under fixed exceedance tolerance.

## Required exhibits

Quantile fan, calibration and loss table, event counts, crossing diagnostic and origin ledger.

## Robustness

Limited tail events; no claim that risk forecasts generate trading gains. Same sample and quantiles across methods; no test tuning. Revised macro/valuation data not real-time vintages.

## Minimum viable thesis

Three quantiles including .10, two benchmarks, expanding test, proper scores and calibration.

## Optional extension

Fit Student-t location-scale distribution and compare CRPS on identical origins.

## Prerequisites

Quantile regression, forecasting, Python.

## Thesis outline

1. Distribution forecasts;

2. Quantile methods;

3. Timing and data;

4. Scores and calibration;

5. Limits.

## Milestones

W1-3: predictors and scoring; W4-6: benchmarks; W7-9: quantile fits; W10-12: evaluation; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
