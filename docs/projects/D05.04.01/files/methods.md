---
title: "Focused methods — Discretizing the Heston Model: Bias, Stability and Computational Cost"
subtitle: "D05.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Conditional moments and joint dynamics
Under $\mathbb Q$, $d\log S=(r-q-v/2)dt+\sqrt v\,dW^S$ and $dv=\kappa(\theta-v)dt+\xi\sqrt v\,dW^v$, with instantaneous correlation $\rho$. For step $h$, $a=e^{-\kappa h}$, conditional mean $m=\theta+(v-\theta)a$ and variance $s^2=v\xi^2a(1-a)/\kappa+\theta\xi^2(1-a)^2/(2\kappa)$. Full truncation uses $v^+=\max(v,0)$ in drift and diffusion but allows negative latent states. Partial truncation retains the latent state in drift. Derive each update, including correlated log-stock increments. QE-M uses conditional moments and a martingale correction; consult the original algorithm and respect its moment-domain restrictions.

## Weak errors
Check conditional variance moments and $\mathbb E^{\mathbb Q}[e^{-rT}S_T]=S_0e^{-qT}$. Compare signed option bias relative to independent quadrature, with replicate SE and cost. Record negative states and rejected QE-M cases. A finest-grid Asian reference is numerical, not exact.

## Research checks

Use nested Brownian increments for Euler comparisons and independent replications. Separate path-count error from time-step error. Keep fixing dates constant and report high-vol-of-vol failures.
