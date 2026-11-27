# Research plan | A05.02.01

## Study design and independent work

Freeze decay or select it only on training data. A negative OOS result is informative. Do not describe a fitted DNS model as automatically arbitrage-free or an implementable trading rule.

## Required tasks

1. Check curve metadata, calendar, missing nodes and compounding; plot representative curves and PCs for context.

2. Fit DNS factors per date with fixed loadings, report cross-sectional residuals and factors; validate reconstruction in synthetic examples.

3. At each forecast origin estimate factor AR(1) on expanding history and forecast h=1,3,12 months ahead; compare no-change forecast at each maturity and direct yield AR(1). VAR as optional predeclared alternative.

4. Score RMSE and MAE in bp at identical origins; calculate uncertainty of paired squared-error differences using HAC/block bootstrap, especially for overlapping horizons. Test whether any advantage concentrates in slope or curvature movements.

## Required exhibits

Average curve and factor loading figure; factor and residual diagnostics; RMSE/MAE heatmap by maturity/horizon; comparative forecast plots and loss-difference intervals; prespecified sample sensitivity table. Separate curve fit quality from dynamic forecast performance.

## Robustness

No lambda or VAR lag selection using OOS scores; all models receive identical information sets. Compare rolling window and ECB zero curves only if conventions are aligned. Acknowledge GSW revisions and fitted-curve structure; do not claim exact real-time forecasting on revised histories.

## Minimum viable thesis

One consistent monthly zero-yield panel, fixed-lambda DNS, AR factors, no-change benchmark, common-sample 1/3/12-month forecast table with uncertainty and interpretation. DNS need not outperform.

## Optional extension

Compare VAR factors, an arbitrage-free Nelson-Siegel formulation or portfolio duration-risk forecast implications; avoid expanding to return predictability before baseline passes.

## Prerequisites

Fixed income, linear regression, AR/VAR basics, time-series validation, Python. No bond transaction database required.

## Thesis outline

1. Term structure and forecasting;

2. Nelson-Siegel and factor dynamics;

3. Zero-yield data and pseudo-OOS protocol;

4. Forecast evidence;

5. Robustness and limitations.

## Milestones

W1-3: derive loadings and acquire GSW; W4-6: clean monthly curves and validate fits; W7-10: implement recursive forecasts and benchmarks; W11-13: evaluate loss differences and stability; W14-16: write and reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
