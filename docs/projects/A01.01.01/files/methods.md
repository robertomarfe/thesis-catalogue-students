---
title: "Focused methods — Testing the CAPM across Size and Value Portfolios"
subtitle: "A01.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Market efficiency and pricing restrictions

Let $x_M$ be market excess return and $\beta_i=\operatorname{Cov}(x_i,x_M)/\operatorname{Var}(x_M)$. With the maintained mean-variance-efficient market proxy, $\alpha_i=E[x_i]-\beta_iE[x_M]=0$. Estimate $x_{it}=\alpha_i+\beta_ix_{Mt}+\epsilon_{it}$. Fit a descriptive cross-sectional line $\bar x_i=a+b\widehat\beta_i+u_i$; the CAPM predicts $a=0$ and $b=E[x_M]$. Estimated betas are generated regressors, not error-free covariates.

## Joint alpha inference

For $T$ dates, $N$ assets and $K$ factors, use covariance matrices $\widehat\Sigma=T^{-1}\sum_t\widehat\epsilon_t\widehat\epsilon_t^\top$ and $\widehat\Omega=T^{-1}\sum_t(f_t-\bar f)(f_t-\bar f)^\top$. The classical GRS statistic is
$$\frac{T-N-K}{N}\frac{\widehat\alpha^\top\widehat\Sigma^{-1}\widehat\alpha}{1+\bar f^\top\widehat\Omega^{-1}\bar f}.$$
The exact $F_{N,T-N-K}$ reference uses the iid Gaussian regression benchmark and full ranks. Robust inference must respect serial and cross-asset dependence. High $R^2$ is not a zero-alpha test.

## Research checks

Use one RF subtraction, common complete dates and separate portfolio panels. Report T, N, K, eigenvalues and failed draws. Re-estimate both regression passes in joint date blocks; do not interpret a rejected joint hypothesis as proof of inefficiency.
