---
title: "Focused methods — The Hansen-Jagannathan Bound and the Volatility of the Pricing Kernel"
subtitle: "A11.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Bound from traded payoffs

For any vector $w$, $E[m]E[w^\top x]=-\operatorname{Cov}(m,w^\top x)$. Cauchy–Schwarz bounds the payoff Sharpe ratio by $\operatorname{sd}(m)/E[m]$. Maximizing over unrestricted weights gives the displayed bound. A singular covariance requires checking whether the mean is in its range; a nonzero mean in a zero-variance direction implies no finite bound. Adding assets on an identical population cannot weaken the unrestricted bound. Positive-kernel restrictions are stronger.

## Real units and consumption benchmark

Compound monthly nominal gross total and bill returns separately into each complete quarter and divide both by the same inflation factor. Define $x=R_i^{real}-R_b^{real}$; the ex post real bill is not a known constant real risk-free asset. For quarterly consumption growth $g_c$, $m=\beta g_c^{-\gamma}$; the dispersion ratio cancels positive $\beta$. Check actual $E[mx]$ in addition to the bound: meeting the necessary bound is not sufficient for pricing.

## Research checks

Use identical complete quarters for all nested sets. Report raw covariance spectrum, rank policy, bootstrap and labeled shrinkage sensitivity; never claim an observed constant real bill or infer rejection solely from a sample bound gap.
