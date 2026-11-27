---
title: "Focused methods — Tail Dependence in Equity Portfolios and Factor Strategies"
subtitle: "A07.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Dependence conditional on marginals
For continuous marginals, $U=F_1(R_1)$ and $V=F_2(R_2)$ have uniform laws. In practice, fix a training empirical CDF convention and avoid 0 and 1 in inverse transforms. For elliptical copulas the population relation between Kendall's tau and latent correlation is $\rho=\sin(\pi\tau/2)$. Gaussian tail dependence is zero when $|\rho|<1$; the Student-t limit is $2t_{\nu+1}(-\sqrt{(\nu+1)(1-\rho)/(1+\rho)})$ for degrees of freedom $\nu>0$.

## Held-out comparison
At each positive threshold $q$, compare the fitted conditional co-exceedance with joint counts relative to the count of the conditioning event. Report both marginal tail frequencies and the effective denominator. Distinguish finite-threshold prediction from an extrapolated asymptotic parameter. Use joint time blocks, common pairs, and a separate sensitivity to volatility-standardized returns to assess marginal dynamics.

## Research checks

Prespecify pair labels and thresholds; do not search over pairs to obtain significant tail dependence. Report sparse counts and uncertainty, and distinguish the conditioning direction in finite samples.
