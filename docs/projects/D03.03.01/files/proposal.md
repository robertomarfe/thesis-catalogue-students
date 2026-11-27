---
title: "Latent Stochastic Volatility versus GARCH"
subtitle: "Research proposal | D03.03.01"
---

**Derivatives · Volatility forecasting and tail risk · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

GARCH treats conditional variance as a deterministic function of past returns; stochastic volatility introduces an unobserved, evolving risk state. The empirical question is whether integrating over uncertainty about that state improves the predictive density and the variance forecast enough to justify the computational cost.

## Research question

Does a parsimonious latent stochastic volatility model improve daily predictive density and multi-day variance forecasts relative to GARCH?

## Economic mechanism

In a Gaussian SV model, $u_t=e^{x_t/2}z_t$ and $x_t=\mu+\phi(x_{t-1}-\mu)+\sigma_x\eta_t$, with independent standard Gaussian shocks and $|\phi|<1$. Here $x_t$ denotes log variance, not the conditional variance itself.

## Research design

Validate a latent-state filter on an artificial series first. Then estimate SV and GARCH on matched market returns using chronological splits and the same mean convention. Compare one-step predictive log densities and multi-day expected variance, with independent particle seeds.

Use the specified simulated filter check, compare effective sample sizes and independent seeds, then freeze the model-selection protocol. Separate uncertainty from latent states, parameters and finite particle budgets.

\newpage

## Required exhibits

Simulation filter diagnostics, fitted parameter table, forecast plots, common-date score table and predictive quantile coverage.

## Minimum viable thesis

Simulated filter check, Gaussian SV and GARCH with honest chronological evaluation of log score and variance. No need for SV to win; distinct from D03.02.02's fractional memory focus.

## Scope and feasibility

Approximate log-square estimation is not exact SV maximum likelihood. Use filtering and sequential predictive likelihood, never smoothed states for forecasting. Daily squared returns are noisy variance proxies; enforce common units and holdout dates. Particle likelihood noise and weak identification must be reported.

**Prerequisites:** Time-series likelihood, Monte Carlo, state-space methods, Python.

**Optional extension:** Leverage SV with correlated shocks, or Bayesian posterior predictive distributions with parameter uncertainty.

## Milestones

W1-3: state-space theory; W4-6: filter tests and cleaning; W7-9: parameter estimation; W10-12: predictive scores and robustness; W13-16: report.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
