# Research plan | A05.03.01

## Study design and independent work

Focus on predictive gains of forward information rather than the common-factor restriction in A05.03.02. Report overlap and latest-vintage pseudo-OOS limitations explicitly.

## Required tasks

1. Construct log prices, one-year forwards and excess holding returns; test flat-curve zero excess when future curve unchanged.

2. Estimate in-sample slope and forward regressions and compare coefficients.

3. Fit CP factor recursively on average realized matured returns, then individual maturity regressions on training only.

4. Compare OOS R2, RMSE and paired block/HAC loss differences; report maturity-by-maturity and aggregate.

5. Analyze subperiods, nonoverlap and sensitivity to first/last month selection; separate statistical forecast from tradability.

## Required exhibits

Price/return construction tests; forward regression table; CP loading plot; OOS accuracy and sample-origin audit.

## Robustness

Do not use yield changes as returns or constant-maturity yield as coupon bond return. Last available estimate may be revised; overlapping outcomes and generated CP factor require robust inference. No full-sample predictor construction in OOS.

## Minimum viable thesis

GSW 1-5Y, historical mean, slope and forward/CP model; rolling-origin evaluation with matured labels and overlap-aware inference.

## Optional extension

Add macro predictors using actual release dates; compare real yields over available TIPS sample separately.

## Prerequisites

Fixed income mathematics, regressions, HAC, Python.

## Thesis outline

1. Expectations hypothesis and premia;

2. Zero-bond return construction;

3. Predictors and sample;

4. In- and out-of-sample tests;

5. Limits.

## Milestones

W1-3: fixed income and paper; W4-6: returns/forwards; W7-9: regressions; W10-12: OOS and inference; W13-16: replicate and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
