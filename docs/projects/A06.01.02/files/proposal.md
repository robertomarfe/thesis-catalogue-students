---
title: "Do Long-Horizon Valuation Ratios Reflect Cash Flow or Discount Rate Variation?"
subtitle: "Research proposal | A06.01.02"
---

**Asset pricing · Consumption-based asset pricing and equity term structures · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

A valuation ratio can predict future returns, future dividends, or both. A finite-horizon present-value identity makes the role of terminal values and measurement errors explicit.

## Research question

How much of aggregate valuation-ratio variation is associated with expected future returns versus dividend growth, and how sensitive is this decomposition to the forecasting model and horizon?

## Economic mechanism

Use $z_t=\log(D_t/P_t)$ and define $e_{t+1}$ by $r_{t+1}=\kappa+z_t-\rho z_{t+1}+g_{t+1}+e_{t+1}$.

## Research design

Goyal annual data, exact return accounting or explicitly approved proxy; VAR(1) finite horizons 1/5/10/20 with terminal and residual.

Use exact annual timing and report accounting residual before log-linear residual; retain signs [future r,-future g,-residual,terminal]. Compare direct finite sums with loadings, covariance shares including negative terms and terminal, and unstable bootstrap draws; if payout data cannot be matched to return convention, stop or obtain approval for clearly labeled proxy.

\newpage

## Required exhibits

Valuation ratio history, identity-residual plot, horizon contribution table including terminal term, VAR coefficients and bootstrap uncertainty.

## Minimum viable thesis

Consistent annual data, identity check, VAR(1) finite-horizon decomposition with terminal and residual, uncertainty and at least one subsample check.

## Scope and feasibility

Small annual sample and near-unit-root valuations create bias; no causal cash-flow/discount-rate shocks identified. Do not treat rolling annual dividend observations as monthly payouts. Preserve timing; avoid ignoring terminal terms or linearization residual to force shares to sum to one.

**Prerequisites:** Asset pricing, VAR, matrix algebra and Python; advanced time-series skills.

**Optional extension:** Use a separately validated dividend strip dataset to compare forecast-based and model-implied discount-rate variation without asserting equivalence.

## Milestones

W1-3: derive identity and select data; W4-6: audit timing and estimate VAR; W7-9: decompositions; W10-12: bootstrap and sensitivity; W13-16: interpretation and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
