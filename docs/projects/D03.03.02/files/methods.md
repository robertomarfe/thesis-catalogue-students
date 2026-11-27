---
title: "Focused methods — Volatility Regimes and Crisis Forecasting"
subtitle: "D03.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## State inference
Let $P_{ij}=\Pr(s_{t+1}=j|s_t=i)$ and $p_{t|t}$ be a row vector. Predict $a=p_{t-1|t-1}P$, then update $p_{t|t,j}=a_j f_j(u_t)/\sum_k a_k f_k(u_t)$, where $f_j$ is the state-specific Gaussian density. The likelihood contribution is the normalizing denominator. Impose an ordering of state variances and monitor occupation, transition boundaries and expected duration $1/(1-P_{jj})$.

## Stress forecast
For horizon $H$, average the expected squared innovations, $H^{-1}\sum_{j=1}^H p_{t|t}P^j v$, for state variances in column vector $v$. Forecast the event that the realized mean square exceeds the frozen training percentile using predictive paths; the probability of a high latent state is not this event probability. Compare Brier and logarithmic loss for the event and QLIKE for variance. Use filtered probabilities, not smoothed probabilities, at forecast origins.

## Research checks

Verify the transition convention, use the same target for GARCH and rolling forecasts, retain false alarms and rare-event counts, and account for overlap. The stress event is high realized variance, not a recession indicator.
