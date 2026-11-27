---
title: "Focused methods — Habit Formation and Time-Varying Equity Risk Premia"
subtitle: "A03.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For external habit surplus share $S_t>0$, the kernel is $m=\beta(G S_{t+1}/S_t)^{-\gamma}$.

Let $K_{ij}=E_i[mG\mathbf{1}_{S_{t+1}=s_j}]$. For the consumption claim, $v=K(\mathbf{1}+v)$ where $v=P/C$. Require a nonnegative kernel and spectral radius below one for the finite present-value solution. The independent-coupling comparison must use the same conditional growth marginal and surplus transition matrix. Compute conditional covariance and safe rate on the same supported outcomes; high SDF volatility alone does not imply a larger premium.

## Research checks

Verify each conditional joint row sums to one, shock marginals and P are identical across coupling cases, same stationary weights, CRRA constant-surplus and Euler checks. Show covariance identity by state and distinguish SDF volatility from priced covariance; retain nonfinite present-value cells.
