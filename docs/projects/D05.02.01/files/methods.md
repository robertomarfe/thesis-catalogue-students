---
title: "Focused methods — Binomial Trees versus Finite Differences for American Options"
subtitle: "D05.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Stopping and complementarity
Let $\mathcal LV=(r-q)SV_S+\sigma^2S^2V_{SS}/2-rV$. The obstacle requires $V\ge g$, $V_\tau-\mathcal LV\ge0$ and their product zero, with terminal condition $V(S,0)=g(S)$. A CRR step of length $h$ uses $u=e^{\sigma\sqrt h}$, $d=1/u$, probability $p=(e^{(r-q)h}-d)/(u-d)$ in $[0,1]$, and the maximum of immediate exercise and discounted continuation.

## Implicit obstacle solver
For discretized operator $L$, define $A=I-hL$. With boundary terms in $b$, solve $v\ge g$, $Av-b\ge0$ and $(v-g)^\top(Av-b)=0$. Projection after an unconstrained solve need not satisfy complementarity. Record residuals, match time to expiry and spot when comparing boundaries, and exclude zero-payoff ties. Validate European prices analytically, then use two separately refined American methods as numerical references, not exact truth.

## Research checks

Save the time-dependent boundary or rerun shorter expiries explicitly. Report domain and odd/even effects, complementarity and interpolation uncertainty. Fix price tolerance before timing.
