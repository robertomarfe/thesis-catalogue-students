---
title: "Predicting the Distribution Rather Than the Mean of Stock Returns"
subtitle: "Research proposal | A02.04.02"
---

**Asset pricing · Predictability and machine learning · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Expected returns alone do not describe downside exposure. Conditional quantiles target tail outcomes without assuming a full parametric distribution, but lower-tail samples are sparse and quantile crossing complicates interpretation.

## Research question

Do valuation and implied-volatility indicators improve lower-tail monthly market excess-return forecasts relative to unconditional historical and rolling location-scale benchmarks?

## Economic mechanism

The conditional quantile $Q_\tau(x)$ minimizes conditional expected pinball loss for probability $\tau$.

## Research design

Use Goyal valuation, French market/bill and VIXCLS, proposed 1990–2025, train 1990–2004 then expanding test. At least .10/.50/.90 quantiles (optional .25/.75), expanding empirical quantiles and rolling 60-month Gaussian benchmark.

Hand-check pinball loss for positive and negative residuals and empirical quantile convention. Check VIX availability and no future data. Test crossing detection, report event counts, no post-test choice of quantile or rearrangement.

\newpage

## Required exhibits

Quantile fan, calibration and loss table, event counts, crossing diagnostic and origin ledger.

## Minimum viable thesis

Three quantiles including .10, two benchmarks, expanding test, proper scores and calibration.

## Scope and feasibility

Limited tail events; no claim that risk forecasts generate trading gains. Same sample and quantiles across methods; no test tuning. Revised macro/valuation data not real-time vintages.

**Prerequisites:** Quantile regression, forecasting, Python.

**Optional extension:** Fit Student-t location-scale distribution and compare CRPS on identical origins.

## Milestones

W1-3: predictors and scoring; W4-6: benchmarks; W7-9: quantile fits; W10-12: evaluation; W13-16: writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
