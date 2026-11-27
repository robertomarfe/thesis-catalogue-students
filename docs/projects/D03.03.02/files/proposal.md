---
title: "Volatility Regimes and Crisis Forecasting"
subtitle: "Research proposal | D03.03.02"
---

**Derivatives · Volatility forecasting and tail risk · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Markets may move between calm and turbulent conditions rather than evolve through a single smooth variance process. A two-state model can express this possibility, but useful stress forecasting requires probability calibration on future observations, not a convincing retrospective classification of crises.

## Research question

Do filtered two-state volatility regimes improve short-horizon variance and stress-event forecasts relative to GARCH and simple historical variance?

## Economic mechanism

For a row transition matrix $P$ and filtered state probabilities $p_{t|t}$, the forecast is $p_{t+j|t}=p_{t|t}P^j$. Conditional variance is the probability-weighted average of state variances in the zero-mean model.

## Research design

Use a two-state Gaussian variance HMM with sorted variances and compare GARCH and historical variance on common 5- and 20-session targets. Freeze the high-variance event threshold from training and produce probabilities by integrating over future states and returns.

Verify the transition convention, use the same target for GARCH and rolling forecasts, retain false alarms and rare-event counts, and account for overlap. The stress event is high realized variance, not a recession indicator.

\newpage

## Required exhibits

Filtered probability and variance plots; forecast loss and event calibration tables; transition and state-duration diagnostics.

## Minimum viable thesis

Validated two-state filter, GARCH/rolling benchmarks, common held-out variance and event score comparison. Distinct from D03.03.01 continuous latent SV density forecasting.

## Scope and feasibility

Crisis event means high realized variance, not recession or causal prediction. VIX is option-implied not physical future variance. Revised source data yield pseudo-OOS; overlapping windows invalidate naive IID tests.

**Prerequisites:** Time series, likelihood, simulation, probability, Python.

**Optional extension:** Student-t emissions or Markov-switching GARCH with careful likelihood validation.

## Milestones

W1-3: Markov filtering; W4-6: simulated validation; W7-9: empirical fits; W10-12: forecasts and rare events; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
