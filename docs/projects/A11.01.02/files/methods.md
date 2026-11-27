---
title: "Focused methods — From Factor Betas to Stochastic Discount Factors"
subtitle: "A11.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Reparameterization

Let $x$ be a column of $N$ excess returns, $f$ a column of $K$ factors, $\mu_x=E[x]$, $\mu_f=E[f]$, $\Sigma_f=\operatorname{Var}(f)$. Normalize the affine candidate to $m=1-b^\top(f-\mu_f)$. Then $g(b)=E[mx]=\mu_x-\operatorname{Cov}(x,f)b$. If $\Sigma_f$ is invertible, the beta representation $g(\lambda)=\mu_x-B\lambda$ follows by $\lambda=\Sigma_fb$. The same fixed quadratic weight on $g$ implies identical feasible errors, although coefficients differ. If the traded excess factors themselves are priced, their restrictions give $\lambda=\mu_f$. Normalizing $E[m]=1$ for excess moments does not price the bill in levels. Positivity is not implied.

With rank deficiency a one-to-one coefficient map need not exist; diagnose the identified span instead of comparing unstable individual coefficients.

## Research checks

Use identical sample conventions for both representations and common WLS weights; verify error equivalence before varying weights. Separate free versus traded lambda, report rank, sign diagnostics and joint date-block refits.
