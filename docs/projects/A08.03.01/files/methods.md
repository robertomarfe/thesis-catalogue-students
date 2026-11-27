---
title: "Focused methods — Risk Parity versus Minimum-Variance Portfolios"
subtitle: "A08.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For variance $v=w^\top\Sigma w$, normalized risk contribution is $RC_i=w_i(\Sigma w)_i/v$.

Contributions sum to one but can be negative for arbitrary portfolios. With positive budgets $b_i$ summing to one, solve the convex problem $\min_{x>0}x^\top\Sigma x/2-\sum_i b_i\log x_i$ for SPD covariance, then normalize. FOC gives $x_i(\Sigma x)_i=b_i$. Diagonal covariance gives inverse-vol weights for equal budgets. Ex-ante budget equality is not realized risk equality.

## Research checks

Check contribution sum, positive budget and ERC residual on diagonal and correlated SPD matrices; report KKT for GMV and eigenvalues. Compare four methods with common dates/covariance, cost drift and ex-ante contributions plus held-out realized contribution estimates and uncertainty.
