---
title: "Focused methods — The Convexity Adjustment in Volatility Swap Pricing"
subtitle: "D08.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mean and curvature
For $dv=\kappa(\theta-v)dt+\xi\sqrt v\,dW$, the mean of $V_T$ is $m=\theta+(v_0-\theta)(1-e^{-\kappa T})/(\kappa T)$. Taylor expansion of $g(x)=\sqrt x$ at $m>0$ yields
$$\mathbb E\sqrt{V_T}\approx\sqrt m-\operatorname{Var}(V_T)/(8m^{3/2}).$$
Jensen's bound is exact, not this local approximation. Wide or near-zero distributions can make the approximation inaccurate.

## Numerical errors
Exact noncentral chi-square CIR transitions for $\xi>0$ do not make the numerical integral exact. Handle $\xi=0$ separately. Compare integration grids and distinguish sampling standard errors from time-integration bias.

## Research checks

Unlike the VIX futures project, the random quantity is realized integrated variance over the entire swap horizon. Report economic errors in volatility points, not only variance units.
