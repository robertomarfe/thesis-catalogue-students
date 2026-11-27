---
title: "Downside versus Upside Market Risk in Factor Investing"
subtitle: "Research proposal | A07.02.02"
---

**Asset pricing · Volatility forecasting and tail risk · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Factor strategies can have different payoffs in rising and falling markets even when their unconditional market exposure is small. This project documents conditional payoffs and their stability; it does not attempt to infer a separate cross-sectional price of downside risk.

## Research question

Which equity factors have asymmetric market exposures and payoff distributions across down and up markets, and how stable is the asymmetry?

## Economic mechanism

With $D_t=\mathbf1_{\{r_{M,t}^e<0\}}$, the interaction model $f_t=a+br_{M,t}^e+cD_t+dD_tr_{M,t}^e+e_t$ permits both intercepts and slopes to differ. The slope difference is $d$.

## Research design

Use common monthly FF5 and momentum histories, fixed market states and subperiods. Compare conditional payoffs, slopes and their differences with joint time-block uncertainty and predeclared rolling windows.

Prespecify the sign cutoff and rolling windows. Report all factors, state counts and crisis sensitivity; distinguish conditional descriptive analysis from a trading signal or a pricing test.

\newpage

## Required exhibits

Conditional payoff table, slope asymmetry estimates and intervals, rolling exposures, state-count and joint-test diagnostics.

## Minimum viable thesis

Five factors plus Mom, predeclared states, conditional slopes and means, uncertainty and subperiod checks. Distinct from A07.02.01, which tests cross-sectional pricing of downside beta.

## Scope and feasibility

Market states are contemporaneous, not a trading signal. Nonlinear slope differences may arise from factor construction and conditional market variance; do not claim structural pricing. Do not subtract RF again from factor payoffs. Report whole sample and crisis sensitivity, not selected best results.

**Prerequisites:** Factor models, regression, bootstrap and Python.

**Optional extension:** Compare factor-level downside exposure with a drawdown-defined state or BAB, without changing baseline selection after results.

## Milestones

W1-3: risk and factors; W4-6: align data and descriptive statistics; W7-9: conditional regressions; W10-12: joint inference and regimes; W13-16: writing and code.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
