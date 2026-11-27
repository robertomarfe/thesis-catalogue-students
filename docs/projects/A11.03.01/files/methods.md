---
title: "Focused methods — Testing Euler Equations with Generalized Method of Moments"
subtitle: "A11.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Moments and derivatives

Let $\theta=(\beta,\gamma)$ and $m=\beta g_c^{-\gamma}$. For a payoff $Y$ with price $p$ (gross bill $p=1$, excess payoff $p=0$), define $u=z_t(mY-p)$. Derivatives of the scalar kernel are
$$\partial_\beta m=g_c^{-\gamma},\qquad \partial_\gamma m=-m\log g_c.$$
The sample Jacobian is the average of $z_tY\partial_\theta m$. Retain the gross bill equation to identify the kernel scale; excess moments alone are homogeneous in $\beta$. The ex post real bill is not conditionally riskless in real units.

## GMM and identification

Minimize $\bar u(\theta)^\top W\bar u(\theta)$ using documented scales. Estimate long-run covariance with Bartlett HAC for the second step. Under correct specification, interior full-rank identification and efficient weighting, $T\bar u^\top W\bar u$ has asymptotic $\chi^2_{q-p}$ law, with $q$ moment count and $p$ parameter count. Weak rank, active bounds or regularization can invalidate this reference. Report profiles and failed starts.

## Research checks

Use quarterly parameters and same-quarter consumption/payoffs; preserve the original broad bounds and fixed moments. Report scaling, HAC bandwidth, effective rank and convergence. Validate independently on a designed simulation before empirical estimation; do not select moments after viewing rejection.
