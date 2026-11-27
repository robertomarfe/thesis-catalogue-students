---
title: "Focused methods — The Impact of Non-Normal Returns on European Option Pricing"
subtitle: "D01.01.03 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## A forward-normalized terminal law
Let $F=\mathbb E^{\mathbb Q}[S_T]$, $D=e^{-rT}$ and $X=\log(S_T/F)$. Begin with $Y$ distributed as a finite Gaussian mixture with weights $p_j$, component means $\mu_j$ and variances $s_j^2$. The unconditional mean is $\bar\mu=\sum_jp_j\mu_j$ and variance is
$$v_Y=\sum_jp_j[s_j^2+(\mu_j-\bar\mu)^2].$$
Center and rescale to the target log variance. For the resulting variable $Z$, set $X=Z-\log\mathbb E[e^Z]$. This common shift preserves all central moments and ensures $\mathbb E[e^X]=1$. It changes the log mean and need not match the arithmetic variance of $S_T$.

## Tail information and prices
If $d_j=\mu_j-\bar\mu$, the third and fourth central moments of the initial mixture are
$$\sum_jp_j(d_j^3+3d_js_j^2),\quad \sum_jp_j(d_j^4+6d_j^2s_j^2+3s_j^4).$$
Divide by $v_Y^{3/2}$ and $v_Y^2$ respectively, subtracting 3 for excess kurtosis. Conditional on a component of the transformed mixture, the stock is lognormal; its forward is $F e^{m_j+w_j/2}$ for conditional log mean $m_j$ and variance $w_j$. Integrate the discounted call payoff over each component and then aggregate by its probability. Compare exact calculations with independent simulation, and invert only prices strictly within Black bounds. Equal skewness and kurtosis do not force equality of option prices at all strikes. This terminal exercise does not impose cross-maturity consistency.

## Research checks

Match log variance and forward before reporting skew or kurtosis. Include a symmetric variance mixture, an asymmetric location mixture and its mirror. Use the same strike coordinates and display the actual moments alongside the smile; the arithmetic variance match is a robustness exercise.
