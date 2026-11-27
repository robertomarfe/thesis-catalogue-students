# Research plan | A11.02.02

## Study design and independent work

Construct gross returns including the actual monthly bill, not excess returns with unit prices. Distinguish train and holdout metrics and apply common conditioning rules; paired time-block resampling should refit the training step and evaluate common holdout draws.

## Required tasks

1. Derive HJ projection and validate with finite-state exact-pricing example.

2. Estimate linear kernels with common G on training set; report coefficients, rank and conditioning.

3. Evaluate frozen coefficients on holdout and held-out industries; report distance and raw pricing errors.

4. Compare paired moving-block bootstrap differences with refitting training steps and common resampled dates; report intervals, not naive chi-square rankings.

5. Vary test assets and common truncation/regularization; if singular, use independent payoff basis or label regularized metric explicitly.

## Required exhibits

Pricing error and HJ distance tables, train/test comparison, SDF volatility and negativity diagnostics, eigenvalues and uncertainty.

## Robustness

Not the HJ volatility bound (A11.02.01). In-sample smaller distances in nested classes partly mechanical. FF3/FF5 SMB definitions can differ. No arbitrage-free positivity guaranteed. Distances compare only given assets and common metric; held-out dates not truly unrevised data.

## Minimum viable thesis

Three kernels, consistent gross payoff normalization and bill, common G, train/holdout distance comparisons and uncertainty with conditioning checks.

## Optional extension

Evaluate a positivity-constrained distance or compare a consumption kernel only after matching real/nominal payoffs and prices.

## Prerequisites

SDF, factor models, matrix algebra, GMM basics and Python.

## Thesis outline

1. SDF pricing and misspecification;

2. HJ projection and estimation;

3. Data and common metric;

4. Model comparison;

5. Statistical and economic limitations.

## Milestones

W1-3: derive projection; W4-6: data and synthetic tests; W7-9: fit and evaluate kernels; W10-12: bootstrap and conditioning; W13-16: interpretation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
