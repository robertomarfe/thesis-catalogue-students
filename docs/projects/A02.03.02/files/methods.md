---
title: "Focused methods — Structural Instability in Equity Premium Predictability"
subtitle: "A02.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

At origin $t$, solve $\min_{a,b}\sum_{s\in\mathcal T_t}w_{s,t}(y_{s+1}-a-bx_s)^2$ using matured targets. Expanding uses all eligible history, rolling uses a fixed last $W$ observations, and discounted uses $w_{s,t}=2^{-(t-s)/H}$ with prespecified half-life $H$. In simulation, contrast a stable slope with a fixed known change in $b_t$ under common innovation draws. A hindsight break estimate may describe the sample but cannot select a forecast rule on the final block.

## Identification and implementation

For fixed design and slope drift, weighted least squares estimates a weighted projection of the history, not automatically the current slope. Shorter windows lower stale-data bias after a break but increase estimation variance. Report adaptation delay under common simulated paths and separate retrospective sup-Wald diagnostics from executable forecasts.

## Research checks

Hand-check weighted least squares on a toy matrix; rolling window never uses an immature label; freeze menu before holdout; report MC uncertainty and stable-null behavior; do not optimize break location on final errors.
