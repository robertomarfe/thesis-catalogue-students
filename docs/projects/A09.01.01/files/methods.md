---
title: "Focused methods — Global versus Regional Equity Factor Models"
subtitle: "A09.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Pricing tests on common assets
Use monthly decimal total returns $R_{i,t}$ and a common USD risk-free return $R_{f,t}$; set $R^e_{i,t}=R_{i,t}-R_{f,t}$. The regional and developed factor models are not nested. An intercept is the model's mean pricing error, not necessarily abnormal profit available to an investor. Compare $\alpha_i$, residual variance, and cross-sectional RMS alpha on the same assets and months. Report factor correlations and the rank of the combined factor panel before estimating incremental local exposures.

## Joint inference and overlap
For $N$ assets, $K$ factors and $T$ dates, classical GRS uses the residual covariance and the factor mean/covariance, with degrees of freedom $N,T-N-K$ under its distributional and covariance assumptions. Check $T>N+K$, rank and conditioning; do not invert nearly singular matrices without disclosure. Resample common monthly blocks for paired comparisons under temporal and cross-asset dependence. Global factors include local constituents and size/BM portfolios overlap factor construction. Alternative test assets mitigate but do not eliminate this issue; alpha differences alone do not identify integration.

## Research checks

Audit identical USD units and RF, dates, portfolio definition and factor count. Report N, T, K, covariance conditioning and paired uncertainty. Separate factor-construction overlap from the economic interpretation.
