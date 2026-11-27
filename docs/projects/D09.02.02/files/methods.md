---
title: "Focused methods — Credit Default Swap Pricing and Recovery Risk"
subtitle: "D09.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Premium and protection legs
Define survival $Q(t)=\exp[-\int_0^t\lambda(u)du]$ and discount $D(t)$. With scheduled accrual $\alpha_j=t_j-t_{j-1}$ and accrued premium paid at default,
$$\mathcal L=\int_0^T D\lambda Q\,du,$$
$$\mathcal A=\sum_j\alpha_j D(t_j)Q(t_j)+\sum_j\int_{t_{j-1}}^{t_j}(u-t_{j-1})D(u)\lambda(u)Q(u)du.$$
For unit notional, $s=(1-R)\mathcal L/\mathcal A$; the buyer's value at contractual coupon $c$ is $(s-c)\mathcal A$ on the specified valuation date and remaining schedule. Seller value reverses sign.

## Two recovery experiments
At fixed hazard, $\partial V/\partial R=-\mathcal L$. At fixed quote, solve anew for the admissible hazard; both risky annuity and protection leg change. Compare values of the existing contract with coupon and remaining dates unchanged. The par contract has zero value in its own calibration; an off-market contract need not. No upfront convention or ISDA production implementation is assumed.

## Research checks

Check zero par MTM, buyer/seller antisymmetry and alternate-recovery repricing. In the continuous-premium flat-hazard limit, $s=(1-R)\lambda$; quarterly accrual is evaluated using its own convention.
