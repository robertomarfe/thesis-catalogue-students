---
title: "Focused methods — Combining Equity Premium Forecasts"
subtitle: "A02.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For $K$ fixed component forecasts $f_{k,t}$, $f^{eq}_t=K^{-1}\sum_k f_{k,t}$ and $f^{ad}_t=\sum_k w_{k,t}f_{k,t}$, where $w_{k,t}\ge0$, $\sum_k w_{k,t}=1$. A candidate adaptive rule uses inverse mean squared error on the last at most 120 matured common forecasts, with a declared positive floor and fixed warm-up: $w_{k,t}\propto(\epsilon+\overline L_{k,t})^{-1}$. Fix the numerical floor and minimum history in advance; use equal weights until that minimum is met. Record each forecast origin, target maturity and realization. A component's past loss becomes usable only after its target has matured.

## Identification and implementation

For unbiased errors with positive definite covariance $\Sigma_e$, the unconstrained minimum-variance unit-sum weights are proportional to $\Sigma_e^{-1}\mathbf{1}$. Explain why estimating the covariance can erase theoretical gains. Equal, median and inverse past-MSE rules are the baseline, not the ex post optimum. Fix warm-up and tie/zero-loss rules before test.

## Research checks

Toy equal weights sum to one; no immature loss in the adaptive window; perturb future targets and verify earlier weights unchanged; audit common component availability and fixed predictor membership.
