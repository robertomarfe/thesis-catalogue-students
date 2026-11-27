---
title: "Focused methods — Excess Volatility and the Present-Value Model of Equity Prices"
subtitle: "A11.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Projection and variance inequality

Assume the constant real discount rate $r$, appropriate integrability and the maintained pricing recursion. Iterating it gives the finite-horizon benchmark in the proposal; write $P_t^{*,H}=P_t+e_{t,H}$ where $E_t[e_{t,H}]=0$. Orthogonality yields
$$\operatorname{Var}(P_t^{*,H})=\operatorname{Var}(P_t)+\operatorname{Var}(e_{t,H}).$$
This is a population identity for comparable square-integrable random variables, not an exact finite-sample ordering. A deterministic detrending scale must apply to both price and benchmark with appropriate growth adjustment. An arbitrary dividend terminal approximation is not the exact conditional projection. Infinite-horizon claims additionally require transversality.

Convert prices and annual dividend-flow approximations to real units consistently. December annualized dividend data are interpolated trailing-flow proxies; do not sum twelve annualized monthly entries.

## Research checks

Use identical origin dates for horizon comparisons, report terminal contributions and fixed discount/growth assumptions. Future prices enter only the ex post benchmark. Document stationarity limitations, overlapping horizons and sampling sensitivity; do not confuse this exercise with news decomposition.
