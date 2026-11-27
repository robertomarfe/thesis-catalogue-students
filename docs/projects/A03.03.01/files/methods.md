---
title: Focused methods note | A03.03.01
---

**Focused methods / A03.03.01**

## 1. Consumption wealth and the Euler equation

Define $a=1-1/\psi$ and $\theta=(1-\gamma)/a$. With the notation in the proposal,

$$w_i^\theta=\beta^\theta\sum_j p_{ij}\mathbb E_i[G^{1-\gamma}\mid j](1+w_j)^\theta.$$

This follows directly from $\mathbb E_i[M R^w]=1$; the exponent on continuation wealth is $\theta$, not $1-\gamma$. For positive wealth and $\theta\ne0$, take logs and solve the resulting fixed point. The implementation below is restricted to non-singular preferences; derive limits separately rather than dividing by zero.

In the iid lognormal economy with log growth mean $\mu$ and variance $s^2$, let $q=w/(1+w)$. Then

$$\log q=\log\beta+a[\mu+\tfrac12(1-\gamma)s^2],\qquad w=\frac{q}{1-q},$$

provided $0<q<1$. The real gross safe return satisfies

$$\log R_f=-\log\beta+\frac{\mu}{\psi}-\frac12\left(\gamma+\frac{\gamma-1}{\psi}\right)s^2.$$

When $\psi=1/\gamma$, $\theta=1$ and $M=\beta G^{-\gamma}$.

\newpage

## 2. Markov pricing and checks

For a dividend claim with growth $G^d$, define pricing matrices

$$K^d_{ij}=p_{ij}\mathbb E_i[M G^d\mid j],\qquad K^0_{ij}=p_{ij}\mathbb E_i[M\mid j].$$

A finite positive price-dividend vector solves $d=K^d(\mathbf1+d)$ when the spectral radius of $K^d$ is below one. Safe rates are $R_{f,i}=1/(K^0\mathbf1)_i$. Confirm the consumption wealth Euler equation separately, and distinguish conditional return means from stationary averages. Report both within- and between-state variation.

## 3. Notation and numerical contract

| Symbol | Implementation | Meaning |
|:--|:--|:--|
| $\beta,\gamma,\psi$ | `beta, gamma, psi` | preferences |
| $p_{ij}$ | `P[i,j]` | transition probability |
| $w_i,d_i$ | `w[i], d[i]` | ex-dividend ratios |
| $K^d,K^0$ | `Kd, K0` | price kernels |

Check positivity, root residuals, uniqueness within tested starts and the iid/CRRA benchmarks. A small residual alone is not a global existence proof. The student derives and implements the full grids and Markov solver. No solved preference grid is supplied.
