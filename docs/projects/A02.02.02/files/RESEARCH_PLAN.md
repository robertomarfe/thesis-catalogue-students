# Research plan | A02.02.02

## Study design and independent work

Assert availability timestamp <= origin for every observation. Perturb all post-origin NFCI observations and ensure features do not change. Check holidays, missing weeks, release lag and common sample. Flag revised values.

## Prespecified implementation

Map weekly NFCI observations to calendar month, use latest observation whose release date precedes origin if vintage available; otherwise lag last observation of prior month conservatively, no forward fill beyond one month. ANFCI sensitivity only. Freeze dp and combined models by validation end and retain 2010–2025 final dates. Separate FF3 optional cross-check from target definition.

## Required tasks

1. Audit index vintage, weekly observation/release dates, levels versus changes and return units.

2. Estimate nested specifications; report HAC intervals, persistence and sample stability.

3. Produce expanding-window one-step forecasts and common-date OOS R2, RMSE and forecast differences.

4. Compare Clark-West for nested linear models and common-date bootstrap; interpret finite-sample uncertainty.

5. Repeat with ANFCI, a 120-month rolling window and quarterly returns with appropriate overlapping inference; quantify effect of release lag.

## Required exhibits

Timing diagram, predictor correlations, coefficient and forecast tables, cumulative squared-error difference plot and stability analysis.

## Robustness

Current revised NFCI histories are pseudo-real-time, not authentic vintages; seek ALFRED vintages for extension. Do not use future index revisions or test-set selection to claim tradability. Limit multiple predictors and distinguish aggregate forecasting from BAB funding mechanism.

## Minimum viable thesis

NFCI and valuation predictors, historical mean benchmark, one chronological forecast test, timing audit, coefficient uncertainty and sensitivity to lags. Null results acceptable.

## Optional extension

Use historical vintages and compare NFCI with GZ excess bond premium under a precommitted model set.

## Prerequisites

Asset pricing, predictive regressions, HAC, Python.

## Thesis outline

1. Conditional equity risk premia;

2. Financial conditions and data;

3. Forecast design;

4. OOS results and robustness;

5. Economic interpretation.

## Milestones

W1-3: theory and vintage audit; W4-6: construct monthly data; W7-9: regressions; W10-12: forecasts and uncertainty; W13-16: robustness and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
