---
title: "Focused methods — Stochastic Volatility and the Economic Determinants of the Implied Volatility Smile"
subtitle: "D01.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Expected variance and implied variance
Under $\mathbb Q$ use Heston variance $dv_t=\kappa(\theta-v_t)dt+\xi\sqrt{v_t}dW_t^v$ and stock diffusion $dS_t/S_t=(r-q)dt+\sqrt{v_t}dW_t^S$, with correlation $\rho$. The conditional mean solves a linear ODE, so $\mathbb E[v_t]=\theta+(v_0-\theta)e^{-\kappa t}$ and
$$\mathbb E\left[\int_0^T v_tdt\right]=\theta T+(v_0-\theta)\frac{1-e^{-\kappa T}}{\kappa}.$$
It is not generally ATM implied total variance. Specify all volatilities in annualized decimal units and distinguish the initial variance from its square root.

## Smile features and conditioning
Let $k=\log(K/F)$ and $I(k,T)$ denote Black implied volatility. At a fixed maturity, estimate ATM level $I(0,T)$, centered slope $[I(h,T)-I(-h,T)]/(2h)$ and curvature $[I(h,T)-2I(0,T)+I(-h,T)]/h^2$. A smaller $h$ amplifies numerical inversion errors. Derive and validate the characteristic-function pricer or independent numerical reference. Form a finite-difference Jacobian of smile features with respect to appropriately scaled parameters; its singular values describe local conditioning, not global identification. For the joint $\xi,\rho$ experiment hold the expected variance curve fixed, and disclose any additional matching targets. Negative $\rho$ is a risk-neutral leverage mechanism, not direct physical evidence.

## Research checks

First change one parameter at a time at a common forward and grid, then explore jointly varying correlation and vol-of-vol. Report actual expected variance for every scenario, flag price bounds, and assess slope sensitivity to the strike window.
