# Research plan | A04.01.02

## Study design and independent work

Match D2 and mean RGDP at the same vintage and q+1 horizon. Audit exchange calendar independently; mark a missing daily return as missing quarterly RV. Show an 80-quarter warmup and only matured next-quarter RV; use training-only log smearing, matched QLIKE and log-MSE with paired blocks; GDP-only robustness.

## Prespecified implementation

Use SPF D2 RGDP for q+1 in annualized pp, not D1 or D3; mean forecast from same vintage/horizon ratio of levels. Pre-1992 RGNP not RGDP: document and separate full-history GNP/GDP splice as original design; GDP-only robustness. Actual survey release determines next complete calendar quarter; if delayed outside vintage q stop and resolve. Construct total daily market log returns, sum squares on full independently audited US session calendar (a coverage check only tests the supplied calendar), lag previous completed quarter RV. Compare log OLS with training-only smearing or Gamma log-link; fit D2/EG incremental coefficients on same sample, strict label maturation at origin. 80-quarter initial sample, HAC and joint block inference. Optional VIX control on common authorized shorter sample; USREC ex post.

## Required tasks

1. Inspect D2 workbook, RGDP horizon labels and release dates; construct EG from growth forecasts or same-vintage levels.

2. Plot dispersion and lagged/future RV, document missing and revision conventions.

3. Estimate nested predictive models with EG and D2, HAC inference.

4. Compare expanding forecasts using positive bias-adjusted log forecasts or multiplicative model; evaluate QLIKE and loss uncertainty.

5. Examine recession sensitivity, post-1992 GDP-only sample, alternate horizon and VIX control on common shorter sample.

## Required exhibits

Survey and market date ledger; descriptive plots; coefficient and forecasting tables; sensitivity to horizons and sample.

## Robustness

SPF dispersion D2 is IQR, not realized EG volatility, and survey horizon must be constant. Avoid current-quarter returns preceding release and using GDP levels across incompatible vintages. Revised data are pseudo-real-time; no causal claim.

## Minimum viable thesis

One D2 RGDP series, EG and daily market RV, release-aligned quarterly regression and expanding evaluation.

## Optional extension

Use individual forecast responses to separate within-forecaster revisions and cross-sectional dispersion, if authorized and documented.

## Prerequisites

Financial econometrics, macro data, forecasting, Python.

## Thesis outline

1. Beliefs and uncertainty;

2. Forecasting framework;

3. Survey timing and market data;

4. Empirical results;

5. Limits.

## Milestones

W1-3: survey conventions and readings; W4-6: merge and variables; W7-9: regressions; W10-12: OOS/robustness; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
