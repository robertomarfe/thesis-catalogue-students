---
title: "Focused methods — Three Factors or Five? Comparing Fama-French Asset Pricing Models"
subtitle: "A01.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Pricing and joint tests

For traded excess factors $f_t$, the factor model implies $E[x_i]=\beta_i^\top E[f]$ if $\alpha_i=0$. Report mean absolute alpha and $\mathrm{RMSE}_\alpha=(N^{-1}\sum_i\widehat\alpha_i^2)^{1/2}$ as economic magnitudes. Multiplying monthly alpha by 12 is arithmetic annualization, not compounding. GRS uses the joint residual covariance and the factor mean correction; its classical F law requires iid Gaussian disturbances, full rank and $T>N+K$. Do not compare p-values as an improvement statistic.

## Nested versus published models

Denote the published size columns $\mathrm{SMB}_3,\mathrm{SMB}_5$. Compare $(M,\mathrm{SMB}_3,H)$ against $(M,\mathrm{SMB}_5,H,R,C)$ as delivered. For the nested experiment compare $(M,\mathrm{SMB}_5,H)$ to $(M,\mathrm{SMB}_5,H,R,C)$, freezing the common columns and dates. The nested comparison isolates the addition of profitability and investment factors.

## Research checks

Require the monthly return blocks, matched RF and common complete calendar, positive GRS degrees of freedom, and at least the original provisional subperiod coverage. Refit paired alpha differences in joint time blocks. Document covariance singularity rather than silently regularizing the classical GRS statistic.
