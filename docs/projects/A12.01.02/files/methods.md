---
title: "Focused methods — Funding Constraints and the Performance of Low-Beta Strategies"
subtitle: "A12.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

Compare $r_t^{BAB}=a+b^\top f_t+c z_t+e_t$ with the lagged state $z_{t-1}$.

BAB is a provider-defined levered long-short return; do not subtract RF or infer financing treatment. Levels and changes of NFCI differ. Weekly observation dates are not release dates; use actual release and conservative lag. Standardize in training. Contemporaneous factor controls are retrospective, not an implementable forecast. Fixed crisis windows and alternate proxies; no causal claim.

## Research checks

Validate BAB workbook version, long-short orientation/units and common FF/Mom panel; separate contemporaneous versus lagged standardized states with past-only scaling. Joint date blocks, fixed crisis windows and optional ANFCI/NFCICREDIT; report no causality and vintage caveat. No OOS claim from contemporaneous controls.
