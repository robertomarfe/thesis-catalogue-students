---
title: "Focused methods — Calibrating Hull-White to the Initial Yield Curve"
subtitle: "D07.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Fitting and pricing
Let $f_0(t)=-\partial_t\log P(0,t)$ and
$$\varphi(t)=f_0(t)+\frac{\sigma^2}{2a^2}(1-e^{-at})^2.$$
The integral of $x$ is Gaussian. Its variance over $[0,T]$ is $\sigma^2\int_0^T[(1-e^{-a(T-s)})/a]^2 ds$; using the Gaussian exponential moment shows exact recovery of the initial discount curve. For expiry $u$ and bond maturity $T>u$, $B(u,T)=(1-e^{-a(T-u)})/a$ and forward-measure log variance is $B^2\sigma^2(1-e^{-2au})/(2a)$. The forward is $P(0,T)/P(0,u)$; discount the forward-measure option payoff by $P(0,u)$.

## Identification
Curve fit is not option calibration. Keep the initial curve common across $a,\sigma$. The numerical benchmark must be independently derived, e.g. joint Gaussian factor/integral or forward Gaussian quadrature.

## Research checks

Report curve recovery, price and numerical error separately; evaluate all prescribed curves and a range of option parameters. Do not present an exact fit as evidence that option values are identified.
