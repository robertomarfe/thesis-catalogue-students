---
title: "Focused methods — Arbitrage-Free Interpolation of Implied Volatility Smiles"
subtitle: "D02.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Finite-grid no arbitrage
For fixed expiry, forward $F$ and discount $D$, a call must satisfy $D(F-K)^+\le C(K)\le DF$. On ordered strikes $K_1<\cdots<K_n$, define secants $s_j=[C(K_{j+1})-C(K_j)]/(K_{j+1}-K_j)$. Required slopes are in $[-D,0]$ and nondecreasing. The convexity inequality corresponds to a nonnegative cost for a properly weighted butterfly on irregular strikes. In a smooth model $C_{KK}=D f_Q(K)$; a piecewise-linear interpolant instead has discrete atoms at changes in slope. Do not treat its knots as a smooth density.

## Projection versus interpolation
Compare cubic IV interpolation, unconstrained price interpolation, and a constrained price projection minimizing $\sum_{j\in\mathcal T}a_j(c_j-C_j^{obs})^2$ under the above linear inequalities with prespecified positive weights $a_j$. Interpolate projected prices linearly on the interior grid. Test all knot intervals and evaluate errors on dense untouched clean strikes. Record optimization failures, actual adjustments to quotes, and size of butterfly violations before and after projection. Individual price clipping does not guarantee convexity. Endpoints and extrapolation require separate assumptions; the baseline is an interior-domain exercise.

## Research checks

Use irregular strike spacing, two independently constructed clean laws and fixed noise draws. Report adjustment cost and holdout recovery separately; distinguish discrete state-price mass from a differentiable density.
