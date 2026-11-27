---
title: "Focused methods — Basket and Worst-of Options: The Role of Correlation"
subtitle: "D06.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Fixed marginals and dependence
Under $\mathbb Q$, $R_i=\exp[(r-q_i-\sigma_i^2/2)T+\sigma_i\sqrt T Z_i]$ with normal marginal shocks and correlation matrix $\mathcal R\succeq0$. Basket weights are nonnegative and sum to one. The worst-of put is a put on the minimum, not the basket. In equal-carry, equal-volatility and perfect positive correlation, normalized prices coincide. For $n$-asset equicorrelation the admissible range is $[-1/(n-1),1]$.

## Comparison and sensitivity
Use stable factorization at singular limits, documenting numerical eigenvalues. A geometric basket has Gaussian log price and can supply a control. Compare a two-asset worst-of claim against independent integration or an established formula under matching assumptions. Use paired normal draws for correlation bumps; record the factorization because it can affect paired variance. Optional dependence mixtures must preserve marginals.

## Research checks

Keep discount and marginal inputs fixed; test PSD before every bump. Examine different strikes and volatilities rather than extrapolating one correlation sign. Distinguish tail dependence from linear correlation.
