---
title: "Focused methods — Rough Volatility and the Short-Term Behavior of Option Prices"
subtitle: "D01.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Volterra variance
In rough Bergomi, let $0<H\le1/2$ be the roughness parameter, $\eta$ vol-of-vol, and $\xi_0(t)$ the initial forward variance curve. Define
$$Y_t=\sqrt{2H}\int_0^t(t-s)^{H-1/2}dW_s,\quad v_t=\xi_0(t)e^{\eta Y_t-\eta^2t^{2H}/2}.$$
Itô isometry gives $\operatorname{Var}(Y_t)=t^{2H}$ and the Gaussian covariance at $t,u$ is $2H\int_0^{\min(t,u)}(t-s)^{H-1/2}(u-s)^{H-1/2}ds$. Hence $\mathbb E[v_t]=\xi_0(t)$. Use $dS/S=(r-q)dt+\sqrt v dB$ with instantaneous Brownian correlation $\rho$; $H=1/2$ reduces the kernel to Brownian motion, not the Heston model. The joint covariance with stock-driver increments matters when simulating leverage.

## Scaling and numerical uncertainty
Define the centered near-ATM slope using strikes $k=\pm c\sqrt T$ in log-forward units. In the model's applicable short-time asymptotic regime the magnitude of skew has leading power $T^{H-1/2}$, with sign governed by the correlation for the chosen parameters. Estimate the log-log slope only on prespecified maturities with reliable nonzero skew. Monte Carlo noise in both prices and their implied-vol inversion can dominate a small strike difference. Use paired simulation, error bars and grid refinement; check the discounted stock mean. The model's finite-horizon predictions need not follow the asymptotic power exactly.

## Research checks

Validate the covariance and cross-covariance before simulating prices. Keep the initial variance curve and other parameters fixed across H. Separate grid refinement, sampling uncertainty and finite-maturity asymptotic bias, with a Brownian-kernel reference.
