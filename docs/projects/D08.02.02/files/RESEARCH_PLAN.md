# Research plan | D08.02.02

## Study design and independent work

Distinguish D03.04.02's high realized-variance event from this downside-return event. Report rare-event uncertainty and all predeclared thresholds. No traded derivative returns or causal conclusions.

## Required tasks

1. Document indices and align dates without carrying across gaps; plot levels, changes and joint stress episodes.

2. Estimate models with historical event frequency, log VIX alone, log VVIX alone and both, using a fixed threshold and lagged data.

3. Produce held-out probabilities, Brier/log loss, calibration and event counts; use regularized logistic only if specified on validation.

4. Compare semivariance prediction via a simple nonnegative benchmark and combined model, reporting robust loss.

5. Repeat on daily overlapping origins with block uncertainty and check incremental value across predeclared subperiods.

## Required exhibits

Joint index scatter/time plots, event counts, coefficient and loss tables, calibration plot and held-out predictions with dates; source and target definitions.

## Robustness

Use several predeclared thresholds and report all; few tail events imply wide uncertainty. Market return is a broad proxy, not exactly SPX. Avoid using future stress states as predictors, converting VVIX into realized vol-of-vol or interpreting regression association causally. No actual VIX option/futures returns are used.

## Minimum viable thesis

Verified common VIX/VVIX/market panel; descriptive stress analysis and incremental out-of-sample downside-event comparison with uncertainty and event counts.

## Optional extension

Use actual volatility derivative settlement data only after separate access and contract-roll validation; index-only conclusions remain separate.

## Prerequisites

Derivatives concepts, logistic regression, time-series validation and Python.

## Thesis outline

1. Volatility indices and vol-of-vol;

2. Downside risk measures;

3. Data and prediction protocol;

4. Incremental information and stability;

5. Limitations.

## Milestones

W1-3: study VIX/VVIX methods; W4-5: data alignment; W6-8: descriptive and baseline models; W9-12: holdout and robustness; W13-16: interpret and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
