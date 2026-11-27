# Research plan | A04.04.01

## Study design and independent work

Freeze lag and return-calendar coverage; use only published EPU and VIX at origin, report conservative extra-lag sensitivity. Match forecast horizon, positive variance units and common origins; train smearing only on mature outcomes; compare paired QLIKE/MSE and crisis sensitivity, no causal claim.

## Prespecified implementation

FF3D daily total market log returns, full calendar monthly sum squares; no intraday RV claim. VIX at last common session, convert index points to decimal annual volatility and square/divide 12 as monthly horizon proxy, not exact physical expected variance. News EPU lagged one month and release checked; if later, longer lag; historical reconstruction/revisions pseudo-OOS. Composite EPU robustness includes non-news components. Use common positive rows, nested log-link or log OLS with training-only smearing and expanding matured labels. Initial train through 2004, validation 2005-09, test 2010-25; no test-based selection. Compare lag RV, VIX-only and joint with/without EPU; paired QLIKE differences block bootstrap, refit sensitivity, report availability losses.

## Required tasks

1. Verify definitions, release timing and data rights; plot series and common sample.

2. Estimate nested log-link models and incremental in-sample association with HAC.

3. Generate expanding-window forecasts and compare QLIKE/MSE with historical RV and VIX-only models.

4. Use paired block-bootstrap loss differences; compare rolling windows and pre/post-2016, pandemic sensitivity.

5. Replace news EPU with composite and longer conservative lag; examine influence of extreme months without selecting the final test sample.

## Required exhibits

Data lineage, uncertainty and variance plots, coefficient tables, OOS score and cumulative loss plots, stability checks.

## Robustness

News-based EPU and composite EPU differ; do not mislabel composite as purely news. EPU may be revised and reconstructed before publication; label pseudo-OOS. Neither predictor importance nor lagged correlation identifies policy shocks. Copyright/citation conditions require review before redistribution.

## Minimum viable thesis

Common data sample, news EPU nested forecasting test, VIX/lagged variance benchmark, QLIKE and timing sensitivity. Distinct from A10.04.01's model-interpretability question.

## Optional extension

Evaluate ALFRED vintage availability or sector-specific uncertainty indices with predeclared multiple-test control.

## Prerequisites

Volatility proxies, predictive regression, forecast evaluation, Python.

## Thesis outline

1. Economic uncertainty and volatility;

2. Index definitions;

3. Forecast design;

4. Results and robustness;

5. Interpretation.

## Milestones

W1-3: theory and data definitions; W4-6: merge and timing; W7-9: nested forecasts; W10-12: scores and sensitivity; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
