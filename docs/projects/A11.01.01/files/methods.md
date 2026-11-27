---
title: Finite-state pricing kernels
subtitle: 'Focused methods supplement | A11.01.01'
---

This note fixes the payoff orientation and derives pricing restrictions. No solved experiment is supplied.

## 1. Pricing as a weighted projection

Let $X$ be a $J\times N$ matrix of payoffs, $q$ the $N\times1$ price vector, and $\Pi=\operatorname{diag}(\pi)$ the diagonal matrix of strictly positive state probabilities. The SDF vector $m$ solves $X^\top\Pi m=q$. Introduce the Euclidean coordinates $u=\Pi^{1/2}m$ and the matrix $A=X^\top\Pi^{1/2}$. The unrestricted problem is

$$\min_u\ \tfrac12 u^\top u\quad\text{subject to}\quad Au=q.$$

If prices are consistent, $u_*=A^+q$. Hence $m_*=\Pi^{-1/2}A^+q$. For full column rank of $X$, this reduces to $m_*=X(X^\top\Pi X)^{-1}q$. A consistent redundant payoff does not change the minimum-norm kernel: it leaves the span unchanged. In contrast, an inconsistent price makes the system infeasible. Report the singular values and the rank tolerance rather than treating every numerical inverse as reliable.

For any admissible direction $h$ with $X^\top\Pi h=0$, orthogonality implies $m_*^\top\Pi h=0$. Thus

$$\|m_*+h\|_\pi^2=\|m_*\|_\pi^2+\|h\|_\pi^2.$$

Nested consistent spans shrink the feasible set, so the unrestricted minimum norm cannot decrease. If the riskless unit payoff is traded, the mean of every pricing kernel is fixed, and the same monotonicity applies to the minimum variance.

```{=latex}
\newpage
```

## 2. Sharpe ratios and admissibility

A zero-cost excess payoff $x$ satisfies $\mathbb E[mx]=0$. Expanding the expectation gives $\mathbb E[x]=-\operatorname{Cov}(m,x)/\mathbb E[m]$. Cauchy--Schwarz yields

$$\frac{|\mathbb E[x]|}{\operatorname{SD}(x)}\leq\frac{\operatorname{SD}(m)}{\mathbb E[m]}.$$

With a constant riskless payoff, the unrestricted minimum-variance kernel attains the maximum Sharpe bound when the traded excess-payoff span supports the requisite direction and unconstrained linear combinations are allowed. Singular covariance matrices require a consistent independent basis; a constrained portfolio frontier need not attain that equality.

Strict positivity is a different restriction. To compute a nonnegative kernel, minimize $\tfrac12m^\top\Pi m$ subject to pricing and $m_j\geq0$. To test whether a strictly positive kernel exists, maximize $\eta$ subject to pricing, $m_j\geq\eta$ and $\eta\geq0$. The traded riskless payoff makes the latter objective bounded. A positive feasible margin certifies strict positivity in the finite example; a nonnegative optimizer may lie on the boundary.

## 3. Starter and student-owned investigation

Check payoff dimensions and probability weights; design the finite-state experiments independently.

| Symbol | Code convention |
|:---|:---|
| $X$ | `X`: states by assets |
| $\pi$ | `p`: state probabilities |
| $q$ | `q`: traded prices |
| $m_*$ | `m`: unrestricted minimum norm |
| $m_{+}$ | `c`: nonnegative minimum norm |
| $\eta$ | `margin`: maximal feasible lower bound |

Use your own implementations to check pricing residuals and distinguish positivity concepts. The remaining design (nested spans, alternative pricing kernels, Sharpe equality, basis and conditioning tests) is the student's own research. Preserve failed cases and distinguish numerical tolerance from economic feasibility. No observed data or structural preference inference is implied.
