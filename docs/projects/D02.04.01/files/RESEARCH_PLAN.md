# Research plan | D02.04.01

## Study design and independent work

Verify three distinct horizons, common eligible session changes and the sample before fitting. Freeze training centering and eigenvectors; compare compression against simple contrasts, then investigate rolling stability without interpreting arbitrary sign changes as economic reversals.

## Required tasks

1. Document maturity, units and historical methodology for each index; align observations and summarize missingness.

2. Plot variance curves, crisis episodes and forward variance proxies; flag negative values without automatic repair.

3. Fit covariance PCA to daily changes; report loadings, eigenvalues, explained variance and one/two/three-component reconstructions.

4. Measure held-out reconstruction error and compare fixed level/slope contrasts with PCA.

5. Examine rolling loading stability using sign alignment and subspace angles; distinguish genuine changes from near-equal eigenvalues.

## Required exhibits

Data dictionary, maturity curves, scree plots, loading plots, holdout RMSE by maturity and rolling subspace diagnostics; reproducible date-aligned panel.

## Robustness

Repeat with standardized changes, weekly changes and levels, always labeling the estimand. For three maturities report one/two factor compression, never claim that three-factor fit is evidence. Handle Cboe backfilled histories and crisis concentration explicitly. PCA does not identify a causal risk factor or tradable VIX futures curve.

## Minimum viable thesis

At least three verified maturity series, reproducible alignment, factor interpretation, held-out one/two-factor comparison and stability analysis. A fourth maturity is required for a nontrivial three-factor compression test.

## Optional extension

Estimate a parsimonious factor VAR and test forecasts of variance curves against persistence; separate from D02.01.02, which targets realized variance prediction.

## Prerequisites

Linear algebra, time-series statistics, derivatives basics and Python pandas/NumPy.

## Thesis outline

1. Volatility indices and variance horizons;

2. PCA and factor interpretation;

3. Data construction;

4. Dimensionality and stability;

5. Limits and extensions.

## Milestones

W1-3: read index methods and PCA; W4-5: acquire and align series; W6-8: estimate PCA; W9-12: held-out and rolling diagnostics; W13-16: robustness and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
