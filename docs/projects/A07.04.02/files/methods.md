---
title: "Focused methods — Are Equity Factor Premia Compensation for Crash Risk?"
subtitle: "A07.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## State-price intuition
For a stochastic discount factor $m$, $E[mr_i^e]=0$ implies $E[r_i^e]=-\operatorname{Cov}(m,r_i^e)/E[m]$. Negative payoffs when $m$ is high can command compensation, but low market returns are only a proxy for those states. Define crash events using a predetermined rolling quantile of market excess returns. Estimate crash conditional mean payoff or market-adjusted residual payoff; an interaction regression additionally describes slope changes. Include a separate crash intercept as a robustness specification.

## Held-out evaluation
Construct a portfolio's exposure from a trailing window and freeze it before evaluation. Compare subsequent mean excess returns of prespecified sorts and cross-sectional regressions with ordinary beta. Report the sign convention (worse payoff versus larger positive risk score), crash counts, influential dates and joint time-block uncertainty with exposure re-estimation.

## Research checks

Do not infer compensation from contemporaneous bad payoffs alone. Predetermine thresholds, retain sparse-event limitations and report alternative measures and noncrash placebo states. Factor spreads and long-only portfolio excess returns require different RF treatment.
