# Research plan | A03.01.02

## Study design and independent work

Provide calendar-aware pair counts and separate fitted conditional rate mean/SD from ex-post real bill mean/SD; test the Gaussian formula by quadrature. Derive beta frontier, retain beta outside (0,1) as inadmissible, and include uncertainty in AR persistence and conditional variance; a rate-volatility mismatch need not imply rejection solely of gamma.

## Prespecified implementation

Use identical quarterly inputs as A03.01.01; estimate AR(1) of g on contiguous quarterly runs only (no row shift across gaps). For stationary g use conditional mean mu+phi(g_t-mu) and residual SD; annual log safe rate=4*log_safe. Analytic stationary SD of the annualized conditional rate is 4*gamma*abs(phi)*sigma_g, with sigma_g innovation SD/sqrt(1-phi^2). Compare ex post rolling real bill log return proxy, not risk-free asset. Solve annual beta frontier via quarterly log rate mean, flag beta>=1. Refit model inside paired block bootstrap with gaps respected.

## Required tasks

1. Derive Euler equation and lognormal short-rate formula, including quarterly/annual conversion.

2. Estimate iid and stationary AR(1) consumption growth models, reporting mean, variance, persistence and residual diagnostics.

3. Compute model-implied real log short-rate mean and SD on beta/gamma grid, annually expressed as 4 times quarterly log rate; separate growth and precautionary terms.

4. Compare empirical ex post real bill proxy moments, with HAC or block bootstrap uncertainty and caveat on inflation surprises.

5. For each gamma compute beta needed to match the empirical mean; identify infeasible or implausible combinations and whether they improve the volatility discrepancy.

## Required exhibits

Consumption moments, implied rate contour plots, discount-factor feasibility frontier, model/data moments table, AR(1) predicted rate and empirical proxy plots.

## Robustness

Check aggregation and revised data; include alternative sample excluding pandemic quarters, and optional verified TIPS yields as longer-maturity context only. Ex post proxy variance includes unexpected inflation and rolling-rate uncertainty; cannot interpret difference as exact model rejection. Constant iid conditional variance cannot generate rate variation. Do not optimize all parameters merely to hit moments.

## Minimum viable thesis

Derivation, iid and conditional mean cases, documented quarterly consumption/bill dataset and rate-moment/parameter frontier analysis.

## Optional extension

Compare with recursive preferences or time-varying consumption uncertainty after baseline; avoid duplicating A03.01.01's equity premium target.

## Prerequisites

Expected utility, macro-finance, lognormal moments and time-series regression.

## Thesis outline

1. Euler equation and intertemporal substitution;

2. Risk-free rate puzzle;

3. Consumption and bill data;

4. Quantitative restrictions and sensitivity;

5. Interpretation.

## Milestones

W1-3: derive SDF and rate; W4-5: data and units; W6-8: consumption models; W9-12: parameter grid and moment uncertainty; W13-16: robustness and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
