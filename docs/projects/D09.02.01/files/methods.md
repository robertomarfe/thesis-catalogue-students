---
title: "Focused methods — Reduced-Form Credit Risk and the Term Structure of Default Probabilities"
subtitle: "D09.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Leg conventions
Let $Q(t)$ denote risk-neutral survival, $D(t)$ the discount factor, $t_j$ payment dates and $\alpha_j=t_j-t_{j-1}$. With protection paid at default and accrued premium until default,
$$\mathcal L=\int_0^T D(u)\lambda(u)Q(u)du,$$
$$\mathcal A=\sum_j\alpha_jD(t_j)Q(t_j)+\sum_j\int_{t_{j-1}}^{t_j}(u-t_{j-1})D(u)\lambda(u)Q(u)du.$$
For unit notional, par spread is $(1-R)\mathcal L/\mathcal A$. Split integration at every hazard knot and coupon date. These are simplified contractual assumptions, not a production CDS convention.

## Inverse calibration
Use identical leg definitions when generating and inverting quotes. Each maturity constrains only the buckets preceding it. Verify survival is nonincreasing and all quote residuals are small. Nonnegative piecewise hazards may not exactly fit perturbed quotes; count infeasible roots. A nonnegative penalized fit minimizes quote error plus a declared roughness penalty, selected independently of the final error evaluation.

## Research checks

Report survival curves and repricing residuals in basis points. Compare alternative recovery at fixed quotes, rather than relabeling the physical hazard. Retain infeasible noisy cases and disclose the objective and penalty.
