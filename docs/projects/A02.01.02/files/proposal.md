---
title: "Long-Horizon Stock Return Predictability and Statistical Inference"
subtitle: "Research proposal | A02.01.02"
---

**Asset pricing · Predictability and machine learning · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

A rising long-horizon regression coefficient need not be evidence of stronger economic predictability. Aggregating returns makes successive dependent variables share observations, and persistent valuation ratios amplify finite-sample distortion. This thesis studies inference, not a horse race between forecasting algorithms.

## Research question

How does inference about dividend-price predictability change from one to three and twelve months after accounting for overlap, persistent regressors and joint testing across horizons?

## Economic mechanism

For additive log excess returns, $y_{t,h}=\sum_{j=1}^h[\log(1+R_{t+j})-\log(1+R_{f,t+j})]$. Overlapping targets share innovations.

## Research design

Use monthly Goyal data, proposed 1950–2025, common complete origins for 1, 3 and 12 months, at least 2,000 paired null paths. Vary persistence and contemporaneous innovation correlation; compare naive, HAC and joint max-t inference.

Check that h=1 target uses only t+1; h=12 uses exactly 12 consecutive months; incomplete paths are excluded. Compare simple and HAC inference on a toy sequence. Verify joint critical value is based on max absolute t from the same path, not independent marginal draws. Preserve negative and insignificant results.

\newpage

## Required exhibits

Horizon coefficient and interval plots, cross-horizon correlation matrix, simulated size and joint p-values, persistence diagnostics, reproducible DGP and return construction.

## Minimum viable thesis

Three horizons, correctly aligned series, naive/HAC comparison, null simulation with joint inference and explicit interpretation of uncertainty, regardless of significance.

## Scope and feasibility

Use alternative HAC bandwidth and block or residual-pair bootstrap under the imposed null. Show both conditional-on-estimated-parameters and persistence sensitivity results; no exact finite-sample guarantee. Nonoverlap reduces sample size and is not a cure for persistence. Separate long-horizon inference from A02.01.01's out-of-sample forecasting objective.

**Prerequisites:** Time-series econometrics, HAC, Monte Carlo and Python statsmodels. Advanced level.

**Optional extension:** Compare bias-corrected or IVX predictive regression with baseline; use 60-month horizon only if finite-sample precision supports interpretation.

## Milestones

W1-3: predictive inference literature; W4-5: validate returns and ratios; W6-8: estimate horizon regressions; W9-12: null simulations and joint tests; W13-16: robustness and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
