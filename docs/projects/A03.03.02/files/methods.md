---
title: "Focused methods — Long-Run Consumption Risk and the Equity Premium"
subtitle: "A03.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

Let $\theta=(1-\gamma)/(1-1/\psi)$ and $w=P_C/C$. The EZ kernel is $m=\beta^\theta G^{-\gamma}[(1+w_j)/w_i]^{\theta-1}$.

With state $x_t=\pm a$ and correlation $\rho^k$ at lag $k$, log growth $g_{t+1}=\mu+x_t+\sigma\epsilon_{t+1}$ has $\operatorname{Var}(g)=a^2+\sigma^2$. For $h$ periods the variance is $h(a^2+\sigma^2)+2a^2\sum_{k=1}^{h-1}(h-k)\rho^k$. The wealth equation is $w_i^\theta=\beta^\theta\sum_j p_{ij}E[G^{1-\gamma}\mid i,j](1+w_j)^\theta$. Price the separate dividend claim using its own growth and the solved consumption kernel. Restrict the supported domain away from $\gamma=1,\psi=1$; CRRA has $\theta=1$. At fixed $a$ vary persistence; $\rho=0$ with $a>0$ is not strict iid conditional growth. Compare price and premium errors, not just wealth approximation error.

## Research checks

Within each fixed a compare rho holding all other primitives fixed; report VR(h), stationary premium and rate, P/D and return volatility, matched CRRA and strict iid, spectral margins and all rejected cells. Independent finite-horizon wealth convergence and quadrature SDF kernels; if pricing with approximate wealth, report its own Euler errors and both premium/yield implications. No claim this replicates BY stochastic-volatility calibration.
