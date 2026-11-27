---
title: "Focused methods — Jump Risk and the Pricing of Equity Options"
subtitle: "D01.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Compensated jump dynamics
Under $\mathbb Q$, write log jump $Y\sim N(m,s_J^2)$, $a=\mathbb E[e^Y]=e^{m+s_J^2/2}$, and Poisson intensity $\lambda$. The compensated stock dynamics are
$$dS_t/S_{t-}=[r-q-\lambda(a-1)]dt+\sigma dW_t+(e^Y-1)dN_t.$$
Conditional on $N_T=n$, the log spot is Gaussian with mean $\log S_0+(r-q-\lambda(a-1)-\sigma^2/2)T+nm$ and variance $\sigma^2T+ns_J^2$. Derive the mixture price as a Poisson-weighted sum of conditional lognormal call values. The forward is $S_0 e^{(r-q)T}$. When truncating, bound the omitted stock leg, whose Poisson weights are tilted by $a^n$.

## Controlled variance
Independence gives annual log variance $v=\sigma^2+\lambda(m^2+s_J^2)$; preserve $v$ when changing the jump distribution, rejecting infeasible negative residual diffusion variance. This differs from matching terminal arithmetic stock-price variance. Compare to a Gaussian benchmark with volatility $\sqrt v$, using identical forward moneyness $k=\log(K/F)$. Verify the zero-intensity limit, put–call parity and independent exact terminal simulation. Short-maturity wings may be economically informative, but extremely small time values can make implied-volatility inversion unstable. Do not interpret the chosen pricing intensity as a physical crash probability.

## Research checks

Build admissible variance-matched configurations before calculating prices. Hold forward fixed and compare several maturities; report ordinary and stock-weighted truncation diagnostics. Keep jump-size and intensity perturbations distinct.
