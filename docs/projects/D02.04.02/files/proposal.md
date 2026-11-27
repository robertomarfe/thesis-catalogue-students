---
title: "Implied Volatility Surface Dynamics and Forecasting"
subtitle: "Research proposal | D02.04.02"
---

**Derivatives · Vanilla pricing and surfaces · Level 3/3**

**Data:** Empirical design blocked pending authorized access and coverage; not assignable on this design. **Status:** current review draft; supervisor approval pending.

## Motivation

A surface forecast must be evaluated on comparable contracts or coordinates through time. Dynamic factors may capture common movements, but apparent forecast skill can result from look-ahead interpolation or a basis estimated using test observations. This study tests factor forecasts against persistence and cellwise time-series benchmarks on a fixed, supported grid.

## Research question

Do dynamic factors of constant-maturity implied total variance outperform persistence and simple autoregressions for out-of-sample surface forecasts?

## Economic mechanism

For each snapshot use $w_t(k,T)=T I_t(k,T)^2$ on supported fixed nodes. Estimate a factor basis on training dates only and reconstruct predictions from forecasts of those factors; persistence is the reference.

## Research design

Subject to authorized historical option quotes or a separately approved vendor surface, construct 15 fixed total-variance nodes on five moneyness coordinates and three maturities. Require at least three years and 500 common sessions; compare persistence, node AR and factor forecasts at 1, 5 and 20 sessions with chronological purging.

Do not replace missing market history with a synthetic study without approval. Freeze the supported nodes, complete session calendar, chronological boundaries and purge. Preserve measurement masks and compare the same targets, including failed or arbitrage-violating forecasts.

\newpage

## Required exhibits

Coverage heatmap, fixed factor loadings, held-out error by tenor/moneyness, paired uncertainty, representative predicted and realized surface plots.

## Minimum viable thesis

Permission and adequate chronology, fixed supported grid, persistence versus PCA-AR on held-out dates, common-node scoring and leakage audit.

## Scope and feasibility

No random row splits, forward-filled labels or look-ahead PCA. Interpolation error is part of measurement, not observed quote error. Forecast skill is not trading profit. Vendor-derived IV surface is model-dependent; do not mix definitions without audit.

**Prerequisites:** Options, time-series forecasting, PCA, interpolation, Python; permitted longitudinal surface data.

**Optional extension:** Evaluate arbitrage-projected forecasts and whether projection helps or hurts held-out accuracy, or compare direct multi-horizon models.

## Milestones

W1-3: acquire permission and assess sample; W4-6: grid and timing; W7-9: train/validation; W10-12: held-out and robustness; W13-16: writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
