---
title: "Focused methods — Risk-Neutral Moments and the Limits of Option-Implied Information"
subtitle: "D11.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Strip identity
For $s>0$ and twice differentiable $g$, the Taylor integral identity yields
$$\begin{aligned}g(s)={}&g(F)+g'(F)(s-F)\\ &+\int_0^F g''(K)(K-s)^+dK\\ &+\int_F^\infty g''(K)(s-K)^+dK.\end{aligned}$$
If integrable, take $\mathbb Q$ expectation; the linear term vanishes since $\mathbb E[S_T]=F$, and divide observed option prices by discount $D_T$. For $z=\log(K/F)$, $g''(K)=[j(j-1)z^{j-2}-jz^{j-1}]/K^2$ for $j\ge2$; for $j=1$ it is $-1/K^2$. Obtain central variance, skewness and excess kurtosis from raw moments; check positive variance before standardizing.

## Support and noise
Signed weights can induce cancellation and sensitivity to small strikes. For bounds use a strictly positive lower support endpoint (log payoff diverges at zero), upper endpoint and consistent quote restrictions. The resulting bound is conditional on that support and discretization, not a global moment bound.

## Research checks

Report absolute moment errors and cancellation across strip, tail and noise choices. Compare central moments only on admissible inputs. Record the exact support and quote tolerance for conditional bounds.
