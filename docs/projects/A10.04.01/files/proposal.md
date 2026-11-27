---
title: "Interpretable Machine Learning for Financial Risk Forecasts"
subtitle: "Research proposal | A10.04.01"
---

**Asset pricing · Predictability and machine learning · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Nonlinear variance forecasts can capture interactions between recent volatility and financial conditions, but interpretation can be unstable with correlated inputs. The thesis asks jointly about forecast quality and stability of attributions, not causality.

## Research question

Do interpretable nonlinear forecasts of market variance improve on linear/HAR benchmarks, and are their feature attributions stable across periods?

## Economic mechanism

Next-month realized variance is a noisy proxy for latent conditional variance; QLIKE assesses positive forecasts in variance units.

## Research design

Use French daily total returns, VIXCLS, NFCI, GS10 and TB3MS; train through 2009, validate 2010–2015 and test 2016–2025. Compare linear/HAR and shallow RF/boost on identical lagged variance/macro features, positive forecasts and grouped attribution.

Hand-check daily squared-return aggregation and annualization (same for forecast and target); record zero/clipped values; check availability ledger and positive forecasts. Permute grouped blocks, not rows; distinguish importance variability from loss uncertainty.

\newpage

## Required exhibits

Feature timing table, forecast comparison, fold-wise importance panels, effect plots with support, robustness and uncertainty table.

## Minimum viable thesis

Linear and two tree methods, time-safe forecasts, grouped importance and stability evaluation. Distinct from A10.02.01 (return forecasts) and D03.01.01 (volatility model horse race).

## Scope and feasibility

Permutation of time series can break dependence and create unrealistic feature combinations. Treat importance as model-specific predictive attribution, not a causal effect or risk price. No tuning on test folds. Daily-return proxy is not high-frequency realized variance; VIX is Q implied variance proxy.

**Prerequisites:** Regression, tree models, time-series validation, Python and visualization.

**Optional extension:** SHAP with explicitly documented dependence assumptions, or compare explanation stability with monotone constrained models.

## Milestones

W1-3: target and literature; W4-6: data and linear benchmark; W7-9: trees and validation; W10-12: interpretation and robustness; W13-16: writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
