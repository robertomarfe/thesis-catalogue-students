---
title: "Principal Components of Implied Volatility Index Curves"
subtitle: "Research proposal | D02.04.01"
---

**Derivatives · Vanilla pricing and surfaces · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

The term structure of option-implied volatility reflects common movements in risk as well as changes concentrated at short or long horizons. PCA describes these movements using a small number of statistical components. The key question is whether such compression remains informative outside the estimation period and across regimes, rather than whether a full-dimensional basis can reconstruct the sample.

## Research question

How much of the variation in a common panel of short-, medium- and longer-horizon implied volatility indices can be explained by level, slope and curvature? Are principal components stable across market regimes?

## Economic mechanism

Let $x_t$ collect eligible annualized variance changes and $L_m$ the first $m$ training eigenvectors. Test the reconstruction $\bar x+L_mL_m^\top(x_t-\bar x)$ using the training mean $\bar x$ and fixed loadings.

## Research design

Align daily closing indices at three or four documented horizons, targeting 2014–2025 when available. Analyze eligible consecutive changes in annualized variance. Fit PCA on the first 60% of observations, freeze the basis and evaluate the final 40%; compare rolling three-year subspaces.

Verify three distinct horizons, common eligible session changes and the sample before fitting. Freeze training centering and eigenvectors; compare compression against simple contrasts, then investigate rolling stability without interpreting arbitrary sign changes as economic reversals.

\newpage

## Required exhibits

Data dictionary, maturity curves, scree plots, loading plots, holdout RMSE by maturity and rolling subspace diagnostics; reproducible date-aligned panel.

## Minimum viable thesis

At least three verified maturity series, reproducible alignment, factor interpretation, held-out one/two-factor comparison and stability analysis. A fourth maturity is required for a nontrivial three-factor compression test.

## Scope and feasibility

Repeat with standardized changes, weekly changes and levels, always labeling the estimand. For three maturities report one/two factor compression, never claim that three-factor fit is evidence. Handle Cboe backfilled histories and crisis concentration explicitly. PCA does not identify a causal risk factor or tradable VIX futures curve.

**Prerequisites:** Linear algebra, time-series statistics, derivatives basics and Python pandas/NumPy.

**Optional extension:** Estimate a parsimonious factor VAR and test forecasts of variance curves against persistence; separate from D02.01.02, which targets realized variance prediction.

## Milestones

W1-3: read index methods and PCA; W4-5: acquire and align series; W6-8: estimate PCA; W9-12: held-out and rolling diagnostics; W13-16: robustness and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
