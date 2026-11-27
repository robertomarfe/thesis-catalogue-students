---
title: "Volatility Persistence and Long Memory in Financial Returns"
subtitle: "Research proposal | D03.02.02"
---

**Derivatives · Volatility forecasting and tail risk · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Slowly decaying dependence in volatility may reflect a fractional process, but persistent regime shifts can produce similar sample patterns. The project combines a controlled identification experiment with out-of-sample comparison to assess whether apparent long memory is useful for forecasting.

## Research question

Does a fractional-memory model improve variance forecasts over HAR and conventional persistent volatility models, and can regime shifts mimic its apparent long memory?

## Economic mechanism

A stationary fractional model satisfies $(1-L)^d(z_t-\mu)=e_t$, with $0\le d<1/2$ and an inverse filter whose coefficients decay at a power rate rather than exponentially.

## Research design

Form nonoverlapping weekly variance proxies, compare AR, ARFIMA, HAR and daily GARCH forecasts at one and four weeks, and simulate a break-driven short-memory process with the same length and variance as the fractional benchmark. Select bandwidth and filter length before the final test.

The break exercise is a diagnostic for observational equivalence, not a test that a particular historical break generated the sample. Retain the prescribed chronological periods and include four-week overlap in inference.

\newpage

## Required exhibits

ACF, simulated d distributions, parameter table, loss and forecast comparison, sensitivity to breaks and sample.

## Minimum viable thesis

Weekly variance proxy, AR(1), ARFIMA and HAR forecasts, controlled break experiment and chronological test at both horizons. Distinct from D03.02.01's horizon forecasting by explicit memory-identification exercise.

## Scope and feasibility

Daily returns give noisy realized variance, not intraday realized variance. Avoid choosing break dates using future forecasts or selecting d from the final sample. Truncated fractional filter requires burn-in and convergence. Log transformation changes the loss target.

**Prerequisites:** Time-series econometrics, likelihood, fractional filters, statistical programming.

**Optional extension:** Compare FIGARCH or regime-switching volatility under a common out-of-sample protocol.

## Milestones

W1-3: fractional integration and DGP; W4-6: build proxies and validate filter; W7-9: estimate and simulate breaks; W10-12: rolling forecasts and inference; W13-16: robustness and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
