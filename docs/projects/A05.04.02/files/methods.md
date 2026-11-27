---
title: "Focused methods — Inflation Risk and the Term Structure of Nominal and Real Interest Rates"
subtitle: "A05.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Measurement
Breakeven inflation is a nominal-real zero yield difference; TIPS indexation, liquidity, deflation protection and fitted-curve conventions may matter. A stylized decomposition is $BEI=E\pi+IRP+\ell+\mathrm{convexity}$, where signs and grouping depend on the convention. Only the sum is observed as a curve difference. CPI10 covers current and next nine calendar years, not automatically a rolling ten-year horizon. Short-horizon SPF forecasts cannot be subtracted from ten-year BEI as a matched expectation.

## Association rather than identification
Compare nominal, real and compensation changes and their co-movement with the released proxy. Use trailing inflation volatility as realized historical uncertainty proxy, not expected conditional uncertainty. Without a documented horizon reconciliation, report co-movement only; even a matched residual is not a pure risk premium.

## Research checks

Verify nominal/real compounding, exact common dates, provider identity and release. Never claim a residual decomposition if the survey alignment fails. This thesis studies inflation compensation, not an ACM nominal premium.
