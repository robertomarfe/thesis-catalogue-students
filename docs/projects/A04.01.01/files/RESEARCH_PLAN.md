# Research plan | A04.01.01

## Study design and independent work

Create an origin/release/target-end ledger; reconstruct first three forecasts from the actual workbook, and verify mature training targets at each decision. Compare EG, dp and both on identical origins with a mature historical mean; report effective sample, overlapping h=12 sensitivity, paired loss intervals and pseudo-real-time limitation.

## Prespecified implementation

Use 1992 onward real GDP mean levels for vintage q, q+1; derive annualized ratio of means. Actual release day determines month-end origin; dp from preceding month only and verify availability, otherwise pseudo-real-time. Monthly log excess = log(1+RF+Mkt-RF)-log(1+RF), not log(1+Mkt-RF). Exact subsequent 3 months, optional 12; labels ending before new origin only. Use historical mean, EG-only, dp-only and joint OLS on common rows. Implement chronological forecasting and a strict target-maturity mask independently, HAC for overlap and paired block bootstrap with model refits. Do not treat the EG coefficient as causal. Use predeclared 1992-2007 training, 2008-2025 test, report actual usable dates and pre-1992 exclusion.

## Required tasks

1. Build vintage-to-release map, derive growth series and verify example against published forecast tables.

2. Merge market and risk-free returns; document month-end origins and future target dates, flag revised valuation data.

3. Estimate EG-only, dp-only and joint models, report HAC uncertainty and economic slope per one SD forecast.

4. Produce expanding out-of-sample forecasts with labels fully realized before training; compare OOS R-squared against mean and dp-only.

5. Check 12-month overlap, alternative growth horizon and predeclared crisis exclusions; interpret cash-flow versus discount-rate ambiguity.

## Required exhibits

Vintage alignment ledger, forecast and return plots, regression and OOS loss tables, sensitivity to growth horizon and release lag, complete merge diagnostics.

## Robustness

Use actual release dates rather than assigning forecasts to quarter starts; compare lagged forecast-only specifications if vintage valuation inputs unavailable. Revised dp means pseudo-real-time, not strict real-time. Survey levels are expectations, not realizations. Small quarterly samples and nested forecast models require caution; block bootstrap or appropriate adjusted loss test.

## Minimum viable thesis

One consistent SPF real-growth forecast measure, release-timed 3-month target, EG/dp regression comparison and historical-mean out-of-sample benchmark, with uncertainty.

## Optional extension

Study survey forecast dispersion or forecast revisions as a separate predictor with a predeclared design.

## Prerequisites

Asset pricing, forecasting regressions, date handling and Python pandas/statsmodels.

## Thesis outline

1. Growth expectations and conditional risk premia;

2. Survey timing and forecasting methodology;

3. Data construction;

4. Predictive evidence;

5. Economic interpretation.

## Milestones

W1-3: pricing and survey documentation; W4-6: vintage merge; W7-9: baseline regressions; W10-12: chronological forecasts; W13-16: sensitivity and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
