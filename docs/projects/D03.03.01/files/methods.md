---
title: "Focused methods — Latent Stochastic Volatility versus GARCH"
subtitle: "D03.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Filtering versus prediction
For latent log variance $x_t$, update the predictive law $p(x_t|\mathcal F_{t-1})$ using the likelihood $u_t|x_t\sim N(0,e^{x_t})$. The one-step predictive density is $p(u_t|\mathcal F_{t-1})=\int p(u_t|x)p(x|\mathcal F_{t-1})dx$. In a bootstrap particle filter, propagate, weight by the likelihood, normalize and resample as needed. Monitor $ESS=1/\sum_i w_i^2$ for normalized weights. A smoothed state uses future observations and cannot enter a forecast.

## Multi-step targets
For $H$ days, forecast $\sum_{j=1}^H E_t[e^{x_{t+j}}]$, integrating over state and transition uncertainty. Use predictive log score (negative log density) for the next observation and QLIKE/MSE for matched variance outcomes. An approximate log-square likelihood is not the exact likelihood; report zero handling, optimization noise and sensitivity to particle budget.

## Research checks

Use the specified simulated filter check, compare effective sample sizes and independent seeds, then freeze the model-selection protocol. Separate uncertainty from latent states, parameters and finite particle budgets.
