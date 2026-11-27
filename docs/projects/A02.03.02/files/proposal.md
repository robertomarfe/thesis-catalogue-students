---
title: "Structural Instability in Equity Premium Predictability"
subtitle: "Research proposal | A02.03.02"
---

**Asset pricing · Predictability and machine learning · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

A short estimation window adapts to structural change but loses precision when predictability is stable. The thesis identifies that bias-variance trade-off using a controlled simulation and a common-date empirical comparison.

## Research question

Do rolling or discounted-window predictive regressions outperform expanding estimates when equity premium predictability is unstable?

## Economic mechanism

The weighted predictive regression minimizes $\sum_{s\in\mathcal T_t}w_{s,t}(y_{s+1}-a-b^\top x_s)^2$.

## Research design

Use Goyal proposed 1950–2025 and a 240-month initial history. Compare expanding, rolling 120/240, and exponential half-life 120 with fixed predictor menu and a training-only collinearity rule. Simulate stable, abrupt and gradual slope changes; one-month baseline.

Hand-check weighted least squares on a toy matrix; rolling window never uses an immature label; freeze menu before holdout; report MC uncertainty and stable-null behavior; do not optimize break location on final errors.

\newpage

## Required exhibits

Simulated bias-variance curves, coefficient paths, break-statistic diagnostics, recursive forecast and loss tables.

## Minimum viable thesis

Simulation and common-date empirical comparison of three window schemes, one predictor and historical-mean benchmark; descriptive break analysis.

## Scope and feasibility

Full-sample break date cannot be used in real-time prediction. Rolling estimates are correlated; naive t-tests over dates invalid. Persistent predictor and endogenous innovations require careful bootstrap. Distinct from forecast combinations (A02.03.01).

**Prerequisites:** Time-series regressions, rolling estimation, bootstrap, Python.

**Optional extension:** Online change detection or Bayesian time-varying coefficients with past-only tuning.

## Milestones

W1-3: theory/simulation; W4-6: data and timing; W7-9: break diagnostics; W10-12: forecasts; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
