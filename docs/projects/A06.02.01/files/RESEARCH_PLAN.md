# Research plan | A06.02.01

## Study design and independent work

Verify archive/version and Eq.32/33, complete 1-15 annual maturity grid, positive dividend normalization and decimals, exact common month-end GSW SVENY, not par yields. Report common sample, model-implied caveat, slope and fixed curvature definition, centered PCA with sign convention and recession episode counts. Inference conditional on estimated curves; no independent validation of the underlying GKK estimator.

## Prespecified implementation

GKK Eq.32 equity yields in continuously compounded annual units after verifying archive scale and nominal convention. Require complete maturity grid 1–15, exact month-end convention and GSW SVENY01–15 common last valid date; no maturity interpolation unless explicit robustness. Use paired_curves and curve_summary; forward equity yield e-y_b is not forward rate between maturities. Descriptive PCA common dates, HAC/block intervals, USREC retrospective episode means and counts. If actual archive inaccessible, defer or supervisor-approved distinct synthetic exercise.

## Required tasks

1. Plot monthly equity yield curves on selected dates and compute maturity-by-maturity mean, SD and serial correlation.

2. Define slope e(15)-e(1) and curvature 2*e(5)-e(1)-e(15) as descriptive summaries; run PCA on demeaned yields in common units, report explained variance and loadings.

3. Construct matched forward equity yields and their slopes; compare means, volatility and equity-bond slope correlation.

4. Compare recession and expansion average curves and slope differences; use block bootstrap or HAC for serial dependence, and recession-episode sensitivity (few independent cycles). Do not treat recession labels as real-time predictors.

## Required exhibits

Maturity moment table; yield and forward-yield curve plots; slope time series with recession shading; factor-loading and variance-explained chart; conditional means and confidence intervals. Clearly label every series 'model-implied' and explain expected cash-flow growth versus discount-rate variation.

## Robustness

Use alternative slope 10Y-1Y, curvature at a different middle maturity, and pre/post-2004 sample comparison if supported. Check yield definitions and compounding before subtracting bond yields. Inference conditional on estimated GKK inputs does not include first-stage model estimation uncertainty. PCA uses full sample for description only, not OOS claims.

## Minimum viable thesis

Verified GKK aggregate file, maturity profiles, slope/PCA analysis and matched bond and recession comparison; no replication of GKK estimation required. If unavailable, pause or redesign as an explicitly synthetic model exercise, not as observed-market evidence.

## Optional extension

Compare a small prespecified selection of GKK characteristic portfolios with positive dividends, or relate slopes to lagged macro forecasts; avoid a full 102-portfolio search without multiplicity control.

## Prerequisites

Asset pricing SDF, bond yields, time-series statistics and PCA, Python. No licensed dividend strip data or full affine estimation required.

## Thesis outline

1. Dividend strips and economic motivation;

2. Equity yields and forward yields;

3. Model-implied dataset and measures;

4. Curve dynamics and recession evidence;

5. Interpretation and limitations.

## Milestones

W1-3: read GKK theory/definitions and verify download; W4-6: align yields, bonds and recession dates; W7-10: moments, PCA and forward curves; W11-13: conditional comparisons and episode sensitivity; W14-16: write and archive code/data provenance.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
