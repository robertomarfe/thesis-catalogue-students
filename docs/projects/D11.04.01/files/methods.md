---
title: "Focused methods — Quadratic Hedging in Incomplete Markets"
subtitle: "D11.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## One-period projection
For a discounted payoff $H$ and traded gain $G$ with positive variance and zero mean, $a=\mathbb E[H]$ and $b=\operatorname{Cov}(H,G)/\operatorname{Var}(G)$. The residual has zero mean and is orthogonal to $G$. Use one common probability law and discounting convention. This least-squares intercept is not in general a unique arbitrage-free price.

## Dynamic projection
With discounted traded martingale $\widetilde S$ and $M_i=\mathbb E[H\mid\mathcal F_i]$, the predictable optimal increment hedge is
$$b_i=\frac{\mathbb E_i[(M_{i+1}-M_i)(\widetilde S_{i+1}-\widetilde S_i)]}{\mathbb E_i[(\widetilde S_{i+1}-\widetilde S_i)^2]}.$$
Use separate training and test paths, identical initial capital and payoff, and only current state features. The proxy delta is feasible but not the exact discrete optimum. Even perfect instantaneous correlation does not ensure exact finite-rebalancing replication. A nonmartingale physical stock requires a different global mean-variance formulation.

## Research checks

Check one-period orthogonality, out-of-sample error and residual variance for zero, static, dynamic and proxy-delta hedges. Report the full-span continuous limit separately from finite-grid errors.
