---
title: "Focused methods — Comparing Local and Stochastic Volatility Models: Pricing and Hedging Performance"
subtitle: "D01.02.03 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Marginals versus paths
Let $C(K,T)$ denote the discounted call price at valuation time zero, with deterministic flat rates $r,q$. In the smooth, positive-density region, the Dupire formula is
$$\sigma_{loc}^2(K,T)=\frac{2[C_T+(r-q)KC_K+qC]}{K^2 C_{KK}}.$$
For a regular Heston diffusion it corresponds to $\mathbb E^{\mathbb Q}[v_T\mid S_T=K]$. Derive the relation from the forward equation. The model $dS/S=(r-q)dt+\sigma_{loc}(S,t)dW$ matches the marginal law under appropriate conditions; transition probabilities and conditional barrier survival need not agree. Numerical differentiation of sparse noisy prices can make the denominator small or negative. Report support, smoothing and rejection choices rather than silently clipping.

## Path-dependent valuation and hedge comparison
A discretely monitored down-and-out call with barrier $B<K$ pays $(S_T-K)^+$ only if all monitored spot values exceed $B$. Both models must use the same monitoring dates; continuous monitoring is a different contract. In the physical Heston simulation use the stated physical drift and variance law. Reprice conditional on the contract still being alive; once knocked out the option is worthless. Distinguish strategies initialized at their own premiums from those initialized at a common premium. A stock-only delta hedge cannot in general span the variance shock. Establish held-out vanilla agreement and independent barrier pricing convergence before interpreting hedge results.

## Research checks

Check derivative stability and held-out vanillas before comparing barriers. Hold monitoring and strike fixed. Treat barrier state, cash funding and initial capital explicitly; record the interpolation domain and the handling of out-of-domain simulations.
