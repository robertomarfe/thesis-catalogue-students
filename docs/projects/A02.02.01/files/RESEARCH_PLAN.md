# Research plan | A02.02.01

## Study design and independent work

First three forecasts recomputed by hand; no forward fill from later observations; exact common evaluation origin list; risk-free and yield units checked separately. Negative OOS R2 retained.

## Prespecified implementation

GS10 and TB3MS are monthly average annualized percent rates, not realized monthly RF. Lag both by one calendar month. Use dp alone, rates alone and combined on common Goyal target. 12-month secondary horizon requires maturity audit. Record whether rate effects remain conditional on valuation.

## Required tasks

1. Construct target and timed predictors, assess persistence, collinearity and missingness.

2. Estimate historical mean, dp-only, rates-only and dp-plus-rates expanding forecasts.

3. Report in-sample slopes with HAC and OOS R2, loss differences and cumulative loss; use paired blocks and nested adjustment with caveats.

4. Compare pre/post-2008 and low-rate episodes on the same forecasting rules.

5. Repeat with 12-month compounded excess-return convention explicitly defined and nonoverlapping evaluation as robustness.

## Required exhibits

Timed data panel, predictor and regression tables, OOS forecasts and loss plots, incremental value of rates and regime sensitivity with intervals.

## Robustness

Do not substitute yield changes for rate levels without separate specification. Do not infer causality from slope signs. Avoid future macro revisions as real-time information and incomplete overlapping labels in estimation. Distinct from A02.01.01 valuation-focused and A02.01.02 long-horizon inference-focused designs.

## Minimum viable thesis

Three prespecified predictor models and historical mean, common monthly sample and expanding forecast evaluation with uncertainty and stability checks.

## Optional extension

Compare nominal versus real rate proxies using appropriately dated expected inflation, or examine a fixed predeclared allocation rule.

## Prerequisites

Time-series econometrics, bond yields, equity risk premia and Python.

## Thesis outline

1. Rates and equity risk premia;

2. Predictive regressions and forecasts;

3. Data and timing;

4. Incremental forecasting evidence;

5. Regime sensitivity and limits.

## Milestones

W1-3: theory and predictor definitions; W4-6: panel and timing tests; W7-9: forecast implementation; W10-12: OOS and regime diagnostics; W13-16: robustness and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
