---
title: "Focused methods — Do Long-Horizon Valuation Ratios Reflect Cash Flow or Discount Rate Variation?"
subtitle: "A06.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

Use $z_t=\log(D_t/P_t)$ and define $e_{t+1}$ by $r_{t+1}=\kappa+z_t-\rho z_{t+1}+g_{t+1}+e_{t+1}$.

Iteration yields $z_t=\sum_{j=1}^H\rho^{j-1}(r_{t+j}-g_{t+j}-e_{t+j}-\kappa)+\rho^H z_{t+H}$. Conditional forecast components have signed covariance shares with $z_t$; they need not be positive. For centered VAR state $X_t$ with transition $A$, forecast loadings use $A^j$ and the long-run discounted sum requires spectral radius of $\rho A$ below one. Audit exact gross return accounting before the approximation. Closure of the algebra is not proof of correct data or forecasts.

## Research checks

Use exact annual timing and report accounting residual before log-linear residual; retain signs [future r,-future g,-residual,terminal]. Compare direct finite sums with loadings, covariance shares including negative terms and terminal, and unstable bootstrap draws; if payout data cannot be matched to return convention, stop or obtain approval for clearly labeled proxy.
