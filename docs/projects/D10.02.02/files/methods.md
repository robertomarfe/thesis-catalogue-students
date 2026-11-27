---
title: "Focused methods — Pricing Commodity Options under Mean Reversion"
subtitle: "D10.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Forward dynamics and total variance
In a one-factor Gaussian log-price model under pricing probabilities, deterministic curve fitting gives a forward with loading $\sigma e^{-\kappa(T-t)}$ and zero drift under deterministic rates. For expiry $u\le T$ its log variance is
$$v(u,T)=\frac{\sigma^2}{2\kappa}\left(e^{-2\kappa(T-u)}-e^{-2\kappa T}\right).$$
As $\kappa\to0$, $v\to\sigma^2u$. The exact log-forward transition has mean $\log F(0,T)-v/2$ and variance $v$, ensuring the forward martingale. Distinguish $u$ from $T$ and keep the initial forward fixed across models.

## Option valuation and matching
With deterministic $r$, use Black-76 $e^{-ru}[F(0,T)\Phi(d_1)-K\Phi(d_2)]$ for a call, with $d_1=(\log(F/K)+v/2)/\sqrt v$ and $d_2=d_1-\sqrt v$. Compare matched instantaneous volatility and matched reference total variance at $u=T=1$; the second requires rescaling $\sigma$ with $\kappa$. Check the martingale, independent payoff simulation, confidence intervals and delivery-lag sensitivity. The model assumes positive prices and is not fitted to observed oil options.

## Research checks

Check the constant-volatility limit, separate expiry from delivery and hold forward/discount fixed. Use independent seeds, report sampling error and keep both matching designs distinct.
