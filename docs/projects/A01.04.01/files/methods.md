---
title: "Focused methods — Factor Spanning and the Economic Value of Additional Factors"
subtitle: "A01.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Orthogonal residual portfolios

Write the vector regression $f_2=a+Bf_1+e$ with $E[e]=0$ and $\operatorname{Cov}(e,f_1)=0$. The traded residual payoff $f_2-Bf_1=a+e$ has mean $a$ and covariance $\Omega$. In these transformed coordinates the covariance is block diagonal, so
$$SR^2_{1,2}=SR^2_1+a^\top\Omega^{-1}a,$$
where $SR^2=\mu^\top\Sigma^{-1}\mu$ for nonsingular covariance and unrestricted portfolios. Derive the identity using the block inverse or orthogonalized span. Zero residual mean implies no gain under these assumptions, not that arbitrary assets are priced. Classical joint intercept inference has the GRS assumptions.

The population identity is not an out-of-sample performance guarantee. Fix training means/covariances and portfolio normalization; evaluate the same weights on later common dates, reporting leverage and realized risk.

## Research checks

Distinguish literal FF5 from the nested union, do not re-subtract RF from spreads, report covariance condition and separate regularization and leverage constraints from the unrestricted identity. Refit in paired time blocks across train/test segments.
