# Research plan | A05.03.03

## Study design and independent work

Require release and horizon metadata before estimation. If necessary use the original minimum of one released horizon and two maturities; do not substitute dispersion for expected growth. Label the result pseudo-OOS unless vintages are truly reconstructible.

## Required tasks

1. Audit forecasts, release dates, growth conventions and GSW return construction.

2. Construct yield-only features and SPF features, same sample; verify label timing.

3. Estimate nested predictive models with train-only standardization and mature outcomes.

4. Compare held-out MSPE, OOS R2 against common historical mean, paired errors and overlapping-horizon HAC/block inference.

5. Study incremental growth vs inflation, 3/12-month horizons, crisis exclusion and vintage limitations.

## Required exhibits

Forecast calendar and sample table, coefficient paths, OOS forecast performance by maturity, incremental predictive-loss intervals.

## Robustness

SPF levels may mix units or definitions across vintages; use same-vintage ratios and document horizon. Retrospective fitted yields and revisions make exercise pseudo-real-time unless verified. No claim of causal forecasting mechanism or trading profitability.

## Minimum viable thesis

One released SPF horizon, two maturities, historical mean/yield-only/augmented forecasts, overlap-aware held-out scoring.

## Optional extension

Add dispersion measured separately from expected growth, after validating SPF D2 horizon and release conventions.

## Prerequisites

Fixed income, predictive regressions, forecast evaluation, macro data.

## Thesis outline

1. Bond risk premia and survey information;

2. Forward returns and forecasts;

3. Data timing;

4. Predictive comparisons;

5. Interpretation.

## Milestones

W1-3: literature and SPF calendar; W4-6: features and labels; W7-9: rolling estimation; W10-12: held-out and uncertainty; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
