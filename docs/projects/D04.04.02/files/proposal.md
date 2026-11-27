---
title: "Hedging with Model-Free Regression Policies"
subtitle: "Research proposal | D04.04.02"
---

**Derivatives · Hedging and volatility derivatives · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Transparent regression hedges offer a structural-model alternative when model parameters are unavailable. Their value depends on observable features that predict useful conditional covariances. The question is whether a richer feasible basis improves replication on independent paths.

## Research question

Can transparent regression hedges improve on BSM delta when the underlying follows a stochastic-volatility or jump process and the policy is trained without access to true model parameters?

## Economic mechanism

In a discounted martingale market, minimize $\mathbb E[(Y-p_0-\sum_i h_i\Delta\widetilde S_i)^2]$ over adapted positions.

## Research design

Use GBM and one or both prescribed misspecified DGPs with martingale discounted stock. Fit linear and enriched bases on training paths, tune regularization on validation and compare against BSM delta at matched initial ATM IV.

Distinguish quadratic regression hedges from neural entropic-risk optimization. Test future-input perturbation, rank and conditioning, validation-only penalty choice, paired test squared loss and tails.

\newpage

## Required exhibits

Held-out hedging error table, policy slices, basis/penalty diagnostics, learning curve and distribution-shift results.

## Minimum viable thesis

GBM and one misspecified DGP, linear and enriched basis, independent test and BSM benchmark.

## Scope and feasibility

Model-free describes policy inputs, not data generation. No observed market performance; no claim of global optimality or cost-optimal policy. Shared discounted ledger and identical constraints; separate latent oracle from feasible inputs.

**Prerequisites:** BSM, regression, Monte Carlo, Python.

**Optional extension:** Train cost-aware policy with backward regression or compare neural policies on identical paths.

## Milestones

W1-3: ledger and theory; W4-6: simulations; W7-9: policy fitting; W10-12: independent tests; W13-16: writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
