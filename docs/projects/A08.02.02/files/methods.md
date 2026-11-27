---
title: "Focused methods — Robust Portfolio Optimization under Parameter Uncertainty"
subtitle: "A08.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

Let $\mu=\widehat\mu+U^{1/2}z$, $\|z\|_2\leq\delta$. Worst-case mean is $w^\top\widehat\mu-\delta\sqrt{w^\top U w}$.

Cauchy-Schwarz gives an adverse shock opposed to $U^{1/2}w$. Subtract the common variance penalty on the same simplex; radius zero nests plug-in. An iid $U=\Sigma/n_{eff}$ is not automatically a confidence region under dependence. Freeze radius menu, cap, gamma and validation criterion; report actual net CE and all optimizer failures.

## Research checks

Verify support function with explicit worst-case mean vector; radius zero nests plug-in and compare two-asset grid with KKT. Freeze radius menu, window and caps before final sample, report binding constraints, paired OOS net CE and costs with failed windows. If interpreting statistical coverage, justify dependence adjustment separately.
