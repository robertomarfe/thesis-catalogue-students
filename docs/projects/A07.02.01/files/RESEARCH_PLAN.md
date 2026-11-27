# Research plan | A07.02.01

## Study design and independent work

Keep daily estimation and monthly evaluation distinct. Verify portfolio definitions and RF units, report conditional counts and collinearity, and do not infer individual-stock pricing or structural risk compensation from portfolio associations.

## Required tasks

1. Derive exposure estimates and compute joint/downside observation counts; validate conditional centering.

2. Estimate rolling conventional and downside betas, plot distributions, correlation and relative downside exposure.

3. Run monthly cross-sectional regressions using predetermined betas; report average premia, HAC intervals, pricing RMSE and collinearity.

4. Compare beta-only and augmented models using same assets/months; estimate block uncertainty by resampling time jointly and recomputing rolling exposures.

5. Check industry versus characteristic portfolios, alternative market threshold and longer windows; report instability and economic effect per SD exposure.

## Required exhibits

Exposure heatmaps, conditional sample counts, beta correlation and rank plots, cross-sectional premium and error tables, generated-regressor uncertainty diagnostics.

## Robustness

No individual-stock anomaly claim from aggregate portfolios. Distinguish daily beta estimates from monthly pricing regressions; use same RF and market definitions. If conditional betas nearly collinear or imprecise, report weak incremental identification rather than forcing significance. Compare bootstrap sensitivity to block length.

## Minimum viable thesis

Verified daily/monthly panel, predetermined rolling betas, beta-only versus downside-augmented cross-sectional tests and a separate portfolio-panel robustness exercise.

## Optional extension

Control for size/value factor exposures or coskewness, only after baseline; avoid claiming a uniquely identified downside risk price.

## Prerequisites

Conditional moments, factor regressions, cross-sectional econometrics and Python.

## Thesis outline

1. CAPM and asymmetric risk;

2. Downside covariance and pricing tests;

3. Portfolio panel and timing;

4. Cross-sectional evidence;

5. Robustness and limitations.

## Milestones

W1-3: theory and downside beta; W4-6: align daily/monthly data; W7-9: rolling exposures; W10-12: pricing tests and bootstrap; W13-16: robustness and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
