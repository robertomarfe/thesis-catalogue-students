---
title: "Focused methods — Calendar-Spread Arbitrage and the Construction of Volatility Surfaces"
subtitle: "D02.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Forward-normalized restrictions
For deterministic rates and proportional dividends, define $x=K/F_T$, $c(x,T)=C(K,T)/(D_TF_T)$ and $w(k,T)=T I(k,T)^2$, with $k=\log x$. The normalized underlying $S_T/F_T$ is a martingale under $\mathbb Q$. Conditional Jensen gives increasing call expectations in $T$ at fixed $x$, equivalent to nondecreasing $w$ at fixed $k$ for Black prices. Raw-strike IV-level monotonicity is not the condition. In strike, require $(1-x)^+\le c\le1$ and increasing slopes in $[-1,0]$.

## Joint grid fit
Use a common ordered $x$ grid. With maturities $T_a<T_b$, impose $c_{j,b}\ge c_{j,a}$ at every common node, in addition to per-slice bounds, monotonicity and convexity. Estimate a constrained least-squares grid on observed cells only, preserving masks for missing cells; anchor $x=0,c=1$ and explicitly treat a distant finite tail node as an approximation. Linear interpolation in $x$ and between maturities preserves the finite-domain inequalities on a common grid. Verify them after interpolation and examine sensitivity to the tail choice. Compare accuracy against held-out clean truth separately from objective fit to noisy quotes; no global extrapolation or smooth-density claim follows.

## Research checks

Use normalized strikes and identical forward inputs before assessing calendars. Distinguish observed masks, withheld truth and artificial tail anchors; check between-node restrictions and report solver slacks and adjustment cost.
