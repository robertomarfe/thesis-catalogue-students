---
title: "Focused methods — Variance Swap Pricing and Discrete Monitoring Bias"
subtitle: "D08.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Moment decomposition
At zero carry set $X_h=bh+\sigma\sqrt h Z+\sum_{k=1}^{N_h}J_k$, with Poisson intensity $\lambda h$ and martingale drift $b=-\sigma^2/2-\lambda(\mathbb E e^J-1)$. Put $m=b+\lambda\mathbb E J$ and $v=\sigma^2+\lambda\mathbb E J^2$. Then $\mathbb E X_h^2=vh+m^2h^2$. Uniform sampling gives annualized monitoring correction $m^2h$; expected continuous quadratic variation per year is $v$.

## Log contract
The diffusion log-contract quantity $-2\mathbb E\log(S_T/S_0)/T$ becomes $\sigma^2+2\lambda\mathbb E(e^J-1-J)$ under jumps, not generally $v$. The static option-strip representation uses weights proportional to $2/K^2$ plus linear and cash terms. Quantify truncation separately. None of these variance strikes is the fair volatility-swap strike.

## Research checks

Verify the diffusion limit and jump moments, isolate monitoring, jump and option-strip errors, and report MC intervals even if a small correction is unresolved.
