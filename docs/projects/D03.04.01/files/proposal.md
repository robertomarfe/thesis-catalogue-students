---
title: "Does the VIX Improve Realized Volatility Forecasts?"
subtitle: "Research proposal | D03.04.01"
---

**Derivatives · Volatility forecasting and tail risk · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Option prices contain forward-looking information about variation, but implied variance is not the physical expectation that a forecaster wishes to estimate. The project asks whether the VIX adds predictive information beyond returns-based models, while respecting horizon and underlying differences.

## Research question

Does lagged VIX improve one-month physical variance forecasts relative to historical and GARCH-based forecasts in genuine chronological evaluation?

## Economic mechanism

If $I_t$ is VIX in index points, $q_t=(I_t/100)^2(30/365)$ approximates 30-calendar-day risk-neutral integrated variance. The realized target is a sum of future squared daily log returns.

## Research design

Align last-common month-end closes, compare historical and GARCH benchmarks with a VIX-augmented physical forecast, and scale to the actual next calendar month's length as an approximation. Keep all estimates and losses on common complete months.

The value added by VIX is a forecasting question, not evidence that the risk-neutral and physical measures are equal. Treat month-length scaling and broad-market versus SPX mismatch as limitations and preserve missing close dates.

\newpage

## Required exhibits

Data alignment audit; time-series forecasts; QLIKE/MSE table and uncertainty; bias plots; reproducible forecast origin ledger.

## Minimum viable thesis

Common sample, two historical benchmarks and VIX-augmented forecast, expanding evaluation and loss comparison.

## Scope and feasibility

Avoid overlapping horizons in baseline, revised inputs and missing VIX dates; daily squared returns are noisy proxies. Do not call VIX physical expectation, and do not claim index-specific replication with French data. Use daily SP500 only if authorized, price-only and limited sample.

**Prerequisites:** Time series, GARCH, regression, Python.

**Optional extension:** Add VIX3M term structure using matched three-month targets and HAC for overlap.

## Milestones

W1-3: theory and data; W4-6: RV/GARCH; W7-9: VIX alignment and forecasts; W10-12: evaluation; W13-16: robustness and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
