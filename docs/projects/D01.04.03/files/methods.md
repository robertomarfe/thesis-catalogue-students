---
title: "Focused methods — Model Complexity versus Pricing Accuracy in Modern Option Pricing"
subtitle: "D01.04.03 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## A common comparison metric
Compare the constant-volatility BSM model, compensated Merton jump diffusion and Heston stochastic volatility at the same forward and discount factor. Their typical free parameter vectors are $(\sigma)$, $(\sigma,\lambda,m,s_J)$ and $(v_0,\kappa,\theta,\xi,\rho)$. For training contracts, define
$$\mathcal L(\vartheta)=\sum_{i\in\mathcal T}w_i[C_i(\vartheta)-C_i^{obs}]^2,$$
where weights come from the prespecified noise design, not from test outcomes. Use comparable tolerances and report runtime including failed starts; price accuracy should be small relative to the smallest meaningful noise scale. Check valid nested limits (zero jumps; deterministic constant variance), without asserting that Heston nests Merton.

## Prediction, recovery and cost
Generate separate clean and noisy truth panels. Measure clean-truth held-out error separately from fit to noisy quotes, with identical test contracts. Report parameter recovery only for the correctly specified family; scaled Jacobian singular values and multistart dispersion diagnose local weak identification. Freeze training, validation and test subsets and do not retune on the held-out maturity. A model may give similar predictions over a range of parameters; runtime and convergence can distinguish practically equivalent alternatives. The results are conditional on the chosen synthetic truth and noise, not a claim of market dominance.

## Research checks

Record noise draws, holdouts, solver starts and comparable timing rules before fitting. Separate nested limits, recovery under correct specification and prediction under misspecification. Rank models using predeclared metrics, not whichever metric favors one model.
