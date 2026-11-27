---
title: Focused methods note | A08.02.01
---

**Focused methods / A08.02.01**

## 1. Gaussian updating

Let $N$ be the number of assets and $J$ the number of views. $P$ is $J\times N$; $Q$ is $J\times1$. With positive definite $\Sigma,\Omega$ and $\tau>0$, write the posterior precision and mean as

$$H=(\tau\Sigma)^{-1}+P^\top\Omega^{-1}P,$$
$$\mu_{BL}=H^{-1}\{(\tau\Sigma)^{-1}\pi+P^\top\Omega^{-1}Q\}.$$

Use linear solves rather than explicit matrix inversion in numerical code. The conditional covariance of the unknown mean is $H^{-1}$; it is not the return covariance used in the baseline allocation. With zero view innovation the mean is unchanged.

## 2. Distinct sensitivity experiments

If $\Omega=c\tau D$, $D=\operatorname{diag}(P\Sigma P^\top)$, then

$$\mu_{BL}=\pi+\Sigma P^\top(P\Sigma P^\top+cD)^{-1}(Q-P\pi).$$

Changing $\tau$ with $c$ fixed cannot change this mean. Hold $\Omega=c\tau_{ref}D$ fixed, with $\tau_{ref}=0.05$, for the separate prior-uncertainty experiment. Do not treat that sensitivity as structural parameter identification.

\newpage

## 3. Allocation and timing

Given an expected excess-return vector $\widehat\mu_t$, choose

$$\max_{w\geq0,\ \mathbf1^\top w=1}\ w^\top\widehat\mu_t-\tfrac{\gamma_p}{2}w^\top\Sigma_t w.$$

Here $\gamma_p$ is portfolio risk aversion, distinct from the prior scaling $\delta$. Estimate all inputs from trailing matured observations. Before trading, drift the previous weights by realized asset returns and renormalize; compute turnover using the stated full- or half-turnover convention consistently with costs. Apply costs to the same portfolio capital ledger.

## 4. Implementation contract

| Symbol | Code field | Shape |
|:--|:--|:--|
| $\Sigma$ | `s` | $N\times N$ |
| $P,Q$ | `p,q` | $J\times N$, $J$ |
| $\Omega$ | `omega` | $J\times J$ |
| $\tau$ | `tau` | positive scalar |
| $w$ | `weights` | $N$ |

Check dimensions, positive definiteness, sum-to-one and constraints. The student implements rolling views, portfolio optimization and realized returns. No portfolio estimates or empirical results are supplied.
