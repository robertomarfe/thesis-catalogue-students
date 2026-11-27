---
title: "Focused methods — Interpretable Machine Learning for Financial Risk Forecasts"
subtitle: "A10.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

Let $v_{t,h}$ be a prespecified nonnegative realized-variance proxy over the future horizon, and $\widehat v_{t,h}>0$ the forecast, both in the same units. Use the original positive-target QLIKE or its target-only-constant-adjusted ranking loss; disclose the zero-target convention. Declare positive floor for predictions. For a grouped feature set $G$, define validation importance $I_G=\overline L_{perm(G)}-\overline L_{original}$ using repeated date-block permutations within validation periods. Correlated groups, support violations and changes across periods limit causal interpretation.

## Identification and implementation

With positive target $v$, QLIKE is $v/f-\log(v/f)-1$ for forecast $f>0$. The equivalent ranking loss $\log f+v/f$ is finite at $v=0$; if used, disclose the target-only constant and zero-target convention. VIX squared divided by 12 in decimal units approximates monthly risk-neutral variance with horizon mismatch; do not equate it to physical realized variance.

## Research checks

Hand-check daily squared-return aggregation and annualization (same for forecast and target); record zero/clipped values; check availability ledger and positive forecasts. Permute grouped blocks, not rows; distinguish importance variability from loss uncertainty.
