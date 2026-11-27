---
title: "Focused methods — Limited Market Participation and Consumption-Based Pricing"
subtitle: "A03.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For jointly Gaussian log shareholder consumption and dividend growth $(g_s,g_d)$, CRRA gives $m=\beta e^{-\gamma g_s}$.

Let $q=E[m e^{g_d}]<1$ and $R_D=e^{g_d}/q$ for the iid perpetuity. Then $E[R_D]/R_f=\exp(\gamma\operatorname{Cov}(g_s,g_d))$. Zero covariance gives zero premium. Gross-mean matching uses $\mu_s=\mu_c+(\sigma_c^2-\sigma_s^2)/2$. A rate-matched beta may be infeasible; retain that result. This is an exogenous marginal-investor pricing experiment, not an equilibrium with resource clearing.

## Research checks

Show FMP equality and zero covariance zero premium; report matched expected gross growth, covariance and q_d existence across four cases. Separate variance-only and covariance changes (when feasible), and beta-adjusted safe-rate diagnostic with bounds. Verify pricing moments by independent Gaussian integration or MC and report price-existence failures.
