# Research plan | D09.03.02

## Study design and independent work

Validate the actual file columns, release metadata, units and common coverage before estimation. Preserve pseudo-OOS wording and the planned ridge sensitivity if separation occurs. No inference based solely on a convenient AUC or retrospective fit.

## Required tasks

1. Audit series, label windows, prevalence and revision caveats.

2. Estimate expanding logit models, training only with labels ending before the origin, initial 1973-1994; report separation and use fixed ridge penalty if necessary.

3. Compare probabilities from 1995 onward via Brier score, log loss, calibration and ROC/PR curves, including base-rate benchmark.

4. Evaluate recession episodes and paired date-block intervals with sensitivity to 12/24-month blocks; avoid treating overlapping labels as independent.

5. Repeat for recession onset rather than any recession month and alternative predictor lags.

## Required exhibits

Forecast probability plot, calibration plot, loss/skill table, recession episode analysis and vintage/timing audit.

## Robustness

NBER dates are retrospective and recognition is delayed; label maturation alone is not real-time availability. Latest-vintage EBP is revised and cannot establish real-time performance. Test extra training-label buffer and report scarcity of recessions. Rights review before any optional Moody's comparison.

## Minimum viable thesis

Public GZ/EBP and Treasury spread, expanding time-ordered logit, base-rate and term-spread comparisons, two proper scores and episode diagnostics.

## Optional extension

Obtain dated predictor and recession-announcement vintages for a true real-time exercise; add permitted rating spreads only as separate robustness.

## Prerequisites

Fixed income, logistic regression, time series and Python.

## Thesis outline

1. Credit and recession risk;

2. Binary forecasting and evaluation;

3. Data and timing;

4. Predictive evidence;

5. Revisions and limitations.

## Milestones

W1-3: literature and label design; W4-6: merge, release and unit audit; W7-9: expanding forecasts; W10-12: calibration and episode robustness; W13-16: inference, reproducibility and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
