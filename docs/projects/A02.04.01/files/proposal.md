---
title: "Does Return Predictability Translate into Better Portfolio Decisions?"
subtitle: "Research proposal | A02.04.01"
---

**Asset pricing · Predictability and machine learning · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Statistical forecast gains need not survive estimation error, risk limits, turnover and transaction costs. A controlled portfolio experiment isolates the economic value of the mean forecast, holding variance and trading conventions fixed.

## Research question

Do recursive equity-premium forecasts improve realized certainty equivalent and risk-adjusted portfolio performance relative to historical-mean and fixed-weight policies?

## Economic mechanism

$w_t=\operatorname{clip}(\widehat\mu_t/(\gamma\widehat\sigma_t^2),0,1)$ links the forecast to an approximate funded allocation rule.

## Research design

Use Goyal dp, ep and term spread, proposed 1965–2025, initial 20 years and final 2005–2025. Compare two prespecified predictor policies, historical mean and fixed weight, common lagged variance, gamma 3/5/10, bounds 0–1 and 0/10/25 bp costs.

Reconcile two consecutive months manually including drifted weight and fees; no contemporaneous variance; check compounding and return units; net CE comparison on common dates; clearly label cost-on-pretrade approximation and annualization.

\newpage

## Required exhibits

Forecast and position ledger; OOS accuracy table; net wealth and CE; sensitivity and paired intervals.

## Minimum viable thesis

Historical mean and two prespecified predictor policies, common variance model, locked evaluation and net CE with uncertainty.

## Scope and feasibility

Use identical RF and return series; estimate forecast variance on past returns only; revised predictors make pseudo-real-time experiment, not historical live trading. Avoid optimizing CE on test data.

**Prerequisites:** Predictive regressions, portfolio choice, time series and Python.

**Optional extension:** Use shrinkage of expected returns toward historical mean; compare forecast combination and uncertainty-adjusted weights.

## Milestones

W1-3: utility and data; W4-6: forecast pipeline; W7-9: ledger and validation; W10-12: locked evaluation; W13-16: sensitivity and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
