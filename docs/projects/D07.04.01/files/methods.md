---
title: "Focused methods — HJM and the No-Arbitrage Dynamics of Forward Rates"
subtitle: "D07.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Drift and numeraires
For $\sigma(t,T)=\sigma_0 e^{-a(T-t)}$,
$$\alpha(t,T)=\frac{\sigma_0^2}{a}e^{-a(T-t)}[1-e^{-a(T-t)}].$$
The bond price is $P(t,T)=\exp(-\int_t^T f(t,v)dv)$ and $B_t=\exp(\int_0^t f(s,s)ds)$. Under $\mathbb Q$, $P(t,T)/B_t$ is a martingale (subject to integrability); simulation times must be strictly before bond maturity for the stated checks. With multiple independent Brownian drivers use a vector dot product in the drift restriction.

## Numerical decomposition
Construct Brownian increments on the union of the specified grids, aggregating to each grid for paired comparisons (the 12/52/252 frequencies are not mutually nested). Refine time and maturity integration separately. Compare with exact deterministic-coefficient Gaussian integrals. Report MC standard errors and discretization gaps. Zero forward drift generally fails the Q restriction despite the same initial curve and diffusion.

## Research checks

Keep the counterexample labeled inadmissible under money-market Q, not an alternative calibrated pricing model. Separate integration bias, sampling uncertainty and runtime.
