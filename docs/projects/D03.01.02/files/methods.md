---
title: "Focused methods — Asymmetric Volatility and the Leverage Effect"
subtitle: "D03.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## News impact and admissibility
Write the demeaned daily log return as $u_t=\sqrt{h_t}z_t$, where $h_t=h_{t|t-1}$ and the standardized shock has mean zero and variance one. For GJR require $\omega>0$, $\alpha\ge0$, $\alpha+\gamma\ge0$ and $\beta\ge0$. With symmetric shocks, finite unconditional variance requires $\alpha+\beta+\gamma/2<1$. EGARCH instead specifies $\log h_{t+1}=\omega+\beta\log h_t+\alpha(|z_t|-E|z_t|)+\gamma z_t$. Here negative $\gamma$ amplifies negative news. Persistence of log variance does not by itself guarantee a finite unconditional variance of returns.

## Forecast and loss
Use the same mean convention and innovation distribution across models. Sum expected conditional second moments for a five-day variance target; use conditional simulation for nonlinear EGARCH rather than exponentiating expected log variance. For positive prediction $f$ and nonnegative outcome $y$, use $\ell(y,f)=\log f+y/f$ and MSE on identical horizons. Condition loss comparisons on the sign known at formation, not the subsequent realization.

## Research checks

Plot news-impact curves at a common prior variance. Report optimization failures and standardized residual checks. Sign-specific forecast improvement is predictive evidence, not proof of financial leverage as a causal mechanism. Use paired time blocks or HAC for overlapping outcomes.
