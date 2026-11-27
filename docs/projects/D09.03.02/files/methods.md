---
title: "Focused methods — Do Corporate Bond Spreads Forecast Economic Downturns?"
subtitle: "D09.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Information and target maturation
At monthly origin $t$, use the lagged credit and rate predictors. Treasury slope $z_t=y_t^{10y}-y_t^{3m}$ is measured in percentage points with different quotation bases acknowledged. For a training origin $s$, the 12-month target is available only after $s+12\le t$ and the required recession information is known. Preserve missing calendar months. NBER retrospective dates and revised model-generated EBP prevent a real-time claim.

## Forecast comparison
A logit assigns $p_t=(1+\exp[-a-b^\top x_t])^{-1}$. Compare base rate, Treasury-only and augmented models with identical matured labels and evaluation origins. Brier loss is $(Y_t-p_t)^2$; log loss is $-[Y_t\log p_t+(1-Y_t)\log(1-p_t)]$. Use a declared numerical rule for extreme probabilities and report separation failures and episode counts. Overlapping labels create serial dependence; use block or episode-based sensitivity. Do not use the Fed-published recession probability as an input.

## Research checks

Validate the actual file columns, release metadata, units and common coverage before estimation. Preserve pseudo-OOS wording and the planned ridge sensitivity if separation occurs. No inference based solely on a convenient AUC or retrospective fit.
