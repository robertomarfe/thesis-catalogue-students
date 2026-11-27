---
title: "Focused methods — Modeling the VIX Futures Curve under Mean Reversion"
subtitle: "D08.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Conditional variance window
Under constant Q CIR parameters and a continuous stock diffusion, conditional expected annualized variance from $T$ to $T+\Delta$ is $A+Bv_T$. With deterministic rates, the model futures price is $100\mathbb E_0^{\mathbb Q}\sqrt{A+Bv_T}$. Jensen bounds it above by $100\sqrt{A+B\mathbb E_0^{\mathbb Q}v_T}$.

## Term structure
At delivery zero the price equals model spot VIX. Long delivery converges to the stationary-law expectation for positive mean reversion and long-run variance. Feller violation allows visits to zero, not failure of the exact transition. Hold $\kappa,\theta$ fixed when isolating $\xi$. The continuous diffusion construction is a model approximation to the index methodology.

## Research checks

Separate the future conditional window from D08.01.02's realized swap variance. Check zero delivery, Jensen and convergence. Do not claim empirical futures calibration from spot observations.
