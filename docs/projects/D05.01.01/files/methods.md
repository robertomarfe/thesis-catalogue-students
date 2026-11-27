---
title: "Focused methods — Variance Reduction in Monte Carlo Option Pricing"
subtitle: "D05.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Sampling and controls
Under the pricing measure $\mathbb Q$, exact GBM log increments over $h$ have mean $(r-q-\sigma^2/2)h$ and variance $\sigma^2h$, where $r,q,\sigma$ are rate, dividend yield and volatility. The price is $\mathbb E^{\mathbb Q}X$ for discounted payoff $X$. Antithetic normals $Z,-Z$ produce one independent pair average. A control $Y$ with known mean $\mu_Y$ gives the adjusted payoff $X-b(Y-\mu_Y)$; minimizing variance yields $b^*=\operatorname{Cov}(X,Y)/\operatorname{Var}(Y)$ for positive control variance. Estimate $b$ on independent pilot paths to preserve conditional unbiasedness. Discounted stock has mean $S_0e^{-qT}$. The geometric Asian payoff is a control for the arithmetic claim; the Gaussian log-average variance is $\sigma^2m^{-2}\sum_{i,j}\min(t_i,t_j)$ for $m$ fixings.

## Precision and cost
Compare equal raw payoff evaluations and include pilot overhead. Assess coverage against the analytic European reference and RMSE relative to an independent arithmetic reference with its own uncertainty. Count pairs rather than treating their members as independent. Variance times runtime measures cost-adjusted precision; report absolute errors where ratios are unstable.

## Research checks

Freeze the payoff, seed and timing protocol. The combined estimator addresses the full question even when the MVT requires only two methods. Do not label a high-budget arithmetic reference exact.
