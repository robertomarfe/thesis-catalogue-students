# Research plan | A11.01.02

## Study design and independent work

Use identical sample conventions for both representations and common WLS weights; verify error equivalence before varying weights. Separate free versus traded lambda, report rank, sign diagnostics and joint date-block refits.

## Required tasks

1. Derive mapping and verify equality numerically on a known simulated factor system.

2. Estimate beta and SDF parameters using the same sample moments; check equality of residual vectors and objective to numerical precision.

3. Compare weighting choices, traded restrictions and factor inclusion; report condition numbers and rank.

4. Estimate uncertainty using a joint moving-block bootstrap that recomputes all moments and weights.

5. Compare pricing errors by portfolio group and inspect fraction of negative fitted normalized m as a diagnostic, not a complete no-arbitrage test.

## Required exhibits

Algebraic proof and unit tests, matched residual table, lambda and b estimates, pricing RMSE/weighted loss and bootstrap intervals, rank and SDF-sign diagnostics.

## Robustness

Do not compare unlike weighting matrices, means or sample periods as a test of equivalence. Estimated traded factors may be misspecified. No claim that a normalized linear SDF is a positive equilibrium pricing kernel. Distinct from A11.02.01 HJ bound and A01.02.01 model selection.

## Minimum viable thesis

Two representations derived and verified, FF3 on two portfolio panels, matched weighting, traded/free lambda and uncertainty diagnostics.

## Optional extension

Compare the GMM implementation with a two-pass estimator using identical moment restrictions; discuss generated-beta and weak-factor inference.

## Prerequisites

Asset pricing, linear algebra, covariance estimation, regression and basic GMM.

## Thesis outline

1. Euler restrictions and beta pricing;

2. Linear SDF and mapping;

3. Data and estimation;

4. Empirical equivalence and weighting;

5. Interpretation and limits.

## Milestones

W1-3: derivations; W4-6: simulation and data tests; W7-9: matched empirical estimators; W10-12: weights and bootstrap; W13-16: diagnostics and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
