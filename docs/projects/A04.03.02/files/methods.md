---
title: "Focused methods — Monetary Policy and the Joint Response of Nominal and Real Yields"
subtitle: "A04.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For matched maturity $n$, define $\Delta BE_e(n)=\Delta y^N_e(n)-\Delta y^R_e(n)$, all in basis points, on the identical event window $e$.

For a common design matrix containing an intercept and rates-only surprise, OLS is linear in the response: $\widehat b_{BE}=\widehat b_N-\widehat b_R$. This holds for every coefficient only if rows and regressors match. Estimate uncertainty directly from the difference response or paired meeting resampling; subtracting standard errors is invalid. Breakeven changes include inflation risk and liquidity compensation. Verify actual same-window nominal/TIPS coverage, units, time zone, event IDs and unmatched counts before fitting. If intraday matching fails, a daily-response design for both yields needs explicit approval, with distinct shock and response windows.

## Research checks

Validate one actual nominal/real maturity and exact same-window surprise mapping. Estimate all three responses with identical design rows; verify intercept and slope identity beta_BE=beta_N-beta_R and compute inference on the actual difference (not by subtracting standard errors). Report unmatched counts and TIPS caveats; if overlap fails defer or seek explicit daily redesign.
