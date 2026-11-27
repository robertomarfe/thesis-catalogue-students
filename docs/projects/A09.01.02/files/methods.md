---
title: "Focused methods — International Diversification and Time-Varying Market Integration"
subtitle: "A09.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Regional co-movement and portfolio risk
Let $R_t\in\mathbb R^4$ collect regional USD total returns, not market excess returns. For fixed monthly weights,
$$w^\top\Sigma w=\sum_iw_i^2\sigma_i^2+2\sum_{i<j}w_iw_j\sigma_i\sigma_j\rho_{ij}.$$
The first term is within-region variance contribution, the second between-region contribution. Rolling correlations, common-factor betas and PCA on covariance or correlation answer distinct questions; fix scaling and explain changes in eigenvectors. Use a common 60-month window, and label the earliest date available for any statistic.

## Implementable regime comparison
For equal weights the period portfolio return is $w^\top R_t$ with monthly rebalancing. Compound total returns, not excess returns. Define high volatility from information available before the period using a training-only threshold; contemporaneous crisis splits are descriptive. Use the same calendar, report regime counts and paired block intervals. A leave-one-out equal-weight regional reference is not a market-cap weighted Developed index. USD returns combine local equity and FX risk; correlation alone is not market integration.

## Research checks

Verify the four disjoint constituents and common USD RF. Exclude the overlapping Developed index from portfolio holdings. Record the rolling/regime timing, variance decomposition and sample dependence.
