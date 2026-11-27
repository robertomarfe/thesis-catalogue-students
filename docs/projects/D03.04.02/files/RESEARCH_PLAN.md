# Research plan | D03.04.02

## Study design and independent work

Do not treat VVIX as realized equity variance. Report all nested comparisons on identical matured dates, label rights and backfill risks, and use predeclared threshold sensitivity. Retain failed or single-class training fits.

## Required tasks

1. Audit calendars, units, missing quotes and label maturity.

2. Construct unconditional and VIX/RV logistic benchmarks.

3. Add VVIX under identical expanding origins and training-only regularization.

4. Compare paired proper scores, reliability and uncertainty by block resampling.

5. Stress 75/90th thresholds, leave crisis years out of descriptive score tables and compare continuous RV forecasts.

## Required exhibits

Tail-probability paths, calibration plot, paired scores, event counts, coefficient stability and coverage audit.

## Robustness

Limited extreme events and backfilled index history constrain inference. No Q=P identification or causal mechanism. Do not optimize tail threshold on test dates; rights and actual VVIX history must be confirmed.

## Minimum viable thesis

Two nested logistic forecasts plus unconditional benchmark, common dates and at least two proper scores.

## Optional extension

Add trailing realized variation of VIX as a physical proxy, with lagged availability and matched horizon.

## Prerequisites

Probability, logistic regression, time-series forecasting, Python.

## Thesis outline

1. Vol-of-vol;

2. Tail forecast design;

3. Data;

4. Chronological evaluation;

5. Limits.

## Milestones

W1-3: data and labels; W4-6: baseline; W7-9: VVIX forecasts; W10-12: score and calibration; W13-16: robustness and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
