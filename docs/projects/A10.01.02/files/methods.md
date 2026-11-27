---
title: "Focused methods — Predicting Factor Returns with Machine Learning"
subtitle: "A10.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For $k\in\{SMB,HML,MOM\}$, predict $f_{k,t+1}$ with an individual training-only ridge or LASSO fit. Define $d_{k,t}=L_{mean,k,t}-L_{model,k,t}$, keeping the vector $d_t$ intact in date-block resampling to preserve cross-factor dependence. Factor-specific historical means use matured factor returns only. Factor returns are long-short payoffs, not automatically funded excess-return investment strategies; collateral and financing require a separate convention.

## Identification and implementation

For model $j$ define $R^2_{OS,k,j}=1-\mathrm{SSE}_{k,j}/\mathrm{SSE}_{k,0}$. Joint date blocks retain correlation of the three loss differences. A simultaneous confidence region or prespecified multiplicity adjustment distinguishes individual from family-wide evidence. Do not subtract RF from zero-cost factor payoffs.

## Research checks

Check factor signs, dates, percent scaling, source vintage and lags. Keep all three factor loss gains together in resampling. Freeze OLS specification; negative R2 and weak gains allowed; no selected winner p-value.
