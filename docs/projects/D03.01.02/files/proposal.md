---
title: "Asymmetric Volatility and the Leverage Effect"
subtitle: "Research proposal | D03.01.02"
---

**Derivatives · Volatility forecasting and tail risk · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Negative equity returns are often followed by more volatile markets than equally large positive returns. A symmetric variance recursion cannot capture this asymmetry. The research separates the shape of the news-impact function from the ability of an estimated model to predict future variation.

## Research question

Do GJR-GARCH and EGARCH improve next-day and multi-day variance forecasts relative to symmetric GARCH, especially after negative market innovations?

## Economic mechanism

In GJR-GARCH, $h_{t+1|t}=\omega+[\alpha+\gamma\mathbf1_{\{u_t<0\}}]u_t^2+\beta h_{t|t-1}$. The response to a negative innovation differs by $\gamma u_t^2$ from that to a positive innovation of equal magnitude.

## Research design

Compare symmetric GARCH, GJR and EGARCH on the same daily market series, with fixed chronological estimation, validation and test periods. Evaluate the sign-conditioned forecast errors at one and, where feasible, five trading days.

Plot news-impact curves at a common prior variance. Report optimization failures and standardized residual checks. Sign-specific forecast improvement is predictive evidence, not proof of financial leverage as a causal mechanism. Use paired time blocks or HAC for overlapping outcomes.

\newpage

## Required exhibits

Parameter and persistence table, standardized residual diagnostics, news-impact curves, forecast loss and conditional loss tables, failure log and forecast date ledger.

## Minimum viable thesis

Three fitted models with admissibility checks, news-impact analysis and chronological loss comparison at one horizon (plus five-day as standard extension), including uncertainty and convergence reporting.

## Scope and feasibility

Compare normal versus t errors, alternative training windows and crisis exclusions predeclared. Do not use future realized losses to define ex ante states. Squared returns are noisy variance proxies; do not interpret forecast superiority as evidence of balance-sheet leverage.

**Prerequisites:** Maximum likelihood, time-series econometrics and Python arch/statsmodels. Understand conditional vs realized variance.

**Optional extension:** Add a VIX-based forecast using aligned units and a separate verified source; do not duplicate the broad GARCH-vs-historical forecasting pilot.

## Milestones

W1-3: derive models and losses; W4-5: clean daily returns; W6-8: estimation and diagnostics; W9-12: rolling forecasts and tests; W13-16: robustness and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
