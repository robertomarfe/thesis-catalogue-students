# Research plan | D03.04.01

## Study design and independent work

The value added by VIX is a forecasting question, not evidence that the risk-neutral and physical measures are equal. Treat month-length scaling and broad-market versus SPX mismatch as limitations and preserve missing close dates.

## Required tasks

1. Align close dates and calculate past/future monthly RV, verify scale.

2. Fit rolling historical RV and daily GARCH with summed forecast variance.

3. Fit RV/VIX combination with training-only coefficient updates.

4. Compare held-out QLIKE/MSE, paired block bootstrap or HAC loss differences and crisis subsamples.

5. Examine calibration, forecast bias and incremental value conditional on prior volatility; report negative results.

## Required exhibits

Data alignment audit; time-series forecasts; QLIKE/MSE table and uncertainty; bias plots; reproducible forecast origin ledger.

## Robustness

Avoid overlapping horizons in baseline, revised inputs and missing VIX dates; daily squared returns are noisy proxies. Do not call VIX physical expectation, and do not claim index-specific replication with French data. Use daily SP500 only if authorized, price-only and limited sample.

## Minimum viable thesis

Common sample, two historical benchmarks and VIX-augmented forecast, expanding evaluation and loss comparison.

## Optional extension

Add VIX3M term structure using matched three-month targets and HAC for overlap.

## Prerequisites

Time series, GARCH, regression, Python.

## Thesis outline

1. Variance and risk-neutral expectations;

2. Forecast models;

3. Data and timing;

4. Out-of-sample results;

5. Interpretation.

## Milestones

W1-3: theory and data; W4-6: RV/GARCH; W7-9: VIX alignment and forecasts; W10-12: evaluation; W13-16: robustness and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
