# Research plan | A02.01.02

## Study design and independent work

Check that h=1 target uses only t+1; h=12 uses exactly 12 consecutive months; incomplete paths are excluded. Compare simple and HAC inference on a toy sequence. Verify joint critical value is based on max absolute t from the same path, not independent marginal draws. Preserve negative and insignificant results.

## Prespecified implementation

Use gross total and bill compounded separately for simple h-month excess (or explicitly choose additive log excess consistently). Common complete origins h=1,3,12. For null simulation choose log excess additive version or simulate gross total/bill consistent with observed units; estimate persistence and innovation correlation under slope-zero null, compare naive/HAC t and max |t| across horizons per same simulated path; >=2000 replications left to student.

## Required tasks

1. Construct monthly returns and lagged valuation ratio; validate date alignment with a hand-worked example.

2. Estimate all horizons, report raw slopes and b_h/h, R-squared, naive and HAC intervals; compare nonoverlapping origins across phases.

3. Simulate the no-predictability null with joint innovations and reproduce overlapping regressions.

4. Compute empirical size of naive/HAC tests and a simulated joint max-|t| critical value, using the same estimator in data and simulation.

5. Compare observed estimates with null joint distribution and evaluate sensitivity to rho and innovation correlation.

## Required exhibits

Horizon coefficient and interval plots, cross-horizon correlation matrix, simulated size and joint p-values, persistence diagnostics, reproducible DGP and return construction.

## Robustness

Use alternative HAC bandwidth and block or residual-pair bootstrap under the imposed null. Show both conditional-on-estimated-parameters and persistence sensitivity results; no exact finite-sample guarantee. Nonoverlap reduces sample size and is not a cure for persistence. Separate long-horizon inference from A02.01.01's out-of-sample forecasting objective.

## Minimum viable thesis

Three horizons, correctly aligned series, naive/HAC comparison, null simulation with joint inference and explicit interpretation of uncertainty, regardless of significance.

## Optional extension

Compare bias-corrected or IVX predictive regression with baseline; use 60-month horizon only if finite-sample precision supports interpretation.

## Prerequisites

Time-series econometrics, HAC, Monte Carlo and Python statsmodels. Advanced level.

## Thesis outline

1. Present-value motivation;

2. Overlap, persistence and inference;

3. Data and simulation design;

4. Horizon-specific and joint evidence;

5. Conclusions.

## Milestones

W1-3: predictive inference literature; W4-5: validate returns and ratios; W6-8: estimate horizon regressions; W9-12: null simulations and joint tests; W13-16: robustness and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
