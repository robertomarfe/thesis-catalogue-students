---
title: "Focused methods — Robust Option Pricing under Uncertain Volatility"
subtitle: "D11.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Controlled volatility
Under ideal frictionless continuous trading, deterministic $r,q$, and admissible volatility $\sigma_t\in[\sigma_L,\sigma_H]$, the upper value solves
$$V_t+(r-q)SV_S-rV+\max_{\sigma\in[\sigma_L,\sigma_H]}\tfrac12\sigma^2S^2V_{SS}=0,$$
with terminal condition $V(T,S)=g(S)$. The upper controller chooses $\sigma_H$ for positive gamma and $\sigma_L$ for negative gamma; lower reverses this. For globally convex calls the upper and lower values reduce to Black--Scholes endpoints. A butterfly has changing curvature, so constant endpoints do not in general attain the controlled extremum.

## Monotonicity and economic meaning
Check transition/stencil signs and the CFL condition when explicit. Compare independent solvers and common boundaries; report time and spatial convergence. A single volatility model's price is admissible inside the model band, but the band is not a statistical confidence interval or a guaranteed empirical bid-ask quote.

## Research checks

Use the degenerate band and convex call limits to check sign and units; record instability and boundary effects. Distinguish the worst-case dynamic control from a search over constant volatilities.
