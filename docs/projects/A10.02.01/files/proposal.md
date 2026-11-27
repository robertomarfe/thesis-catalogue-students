---
title: "Tree-Based Models for Stock Market Return Predictability"
subtitle: "Research proposal | A10.02.01"
---

**Asset pricing · Predictability and machine learning · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Shallow ensembles can capture thresholds and interactions, but financial time series contain few independent observations. The fair test gives nonlinear and linear models the same information and honest selection budget.

## Research question

Do shallow tree ensembles provide incremental out-of-sample equity-premium forecast accuracy relative to linear models under identical information and model-selection rules?

## Economic mechanism

A tree estimates nonlinear conditional means by partitioning predictors; ensembles average trees or fit successive residuals.

## Research design

Use Goyal dp/ep/svar/tbl/tms/dfy with conservative t-1 lag; train 1950–1989, validate 1990–2004, final 2005–2025. Fixed shallow RF/boosting grid, seed 2718, identical inputs and dates for ridge and mean.

No random cross-validation; identical dates/features and mature label rules; perturb future inputs and labels; verify depth/minimum leaf constraints; record seeds and failed fits, not only successful winners.

\newpage

## Required exhibits

Forecast ledger, chosen hyperparameter history, loss/OOS R2 table, uncertainty, interpretability figures and optional economic value comparison.

## Minimum viable thesis

Expanding mean, ridge and one shallow ensemble, nested chronological tuning, untouched holdout loss table and uncertainty. Distinct from A10.01.01 linear regularization and A10.04.02 search-bias simulations.

## Scope and feasibility

Current workbook revised; pseudo-OOS not real-time. No random cross-validation or full-sample scaling. Tree extrapolation is limited and feature importance not causal. If no gains, interpret complexity/variance trade-off, not failed thesis.

**Prerequisites:** Time series, basic ML, Python/scikit-learn and return arithmetic.

**Optional extension:** Test real-time vintages or a predefined interaction model; do not expand the model zoo until baseline protocol is frozen.

## Milestones

W1-3: literature and forecast design; W4-6: data and linear benchmarks; W7-9: nested trees; W10-12: held-out inference; W13-16: interpretation, code and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
