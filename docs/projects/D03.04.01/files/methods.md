---
title: "Focused methods — Does the VIX Improve Realized Volatility Forecasts?"
subtitle: "D03.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Risk-neutral and physical objects
The VIX is an annualized volatility index on SPX option-implied variation. For $H_c$ calendar days, $(I_t/100)^2 H_c/365$ is a horizon-variance approximation; it assumes scaling from the 30-day maturity. Actual squared daily log returns on the broad FF market proxy are neither exact SPX returns nor intraday quadratic variation. Record this distinction explicitly.

## Forecast evaluation
Use lagged returns and scaled implied variance in a model for $Y_{t,H}=\sum_{j\in\mathcal S(t,H)}u_j^2$, where $\mathcal S$ is the set of audited trading sessions in the target window. Fit on matured labels only, preserve positivity through a log link or training-only floor, and compare QLIKE $\log f+Y/f$ and MSE at common origins. Estimate uncertainty from paired loss differences, not independent errors from separate samples.

## Research checks

The value added by VIX is a forecasting question, not evidence that the risk-neutral and physical measures are equal. Treat month-length scaling and broad-market versus SPX mismatch as limitations and preserve missing close dates.
