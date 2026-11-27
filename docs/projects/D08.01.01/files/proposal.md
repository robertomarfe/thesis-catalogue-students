---
title: "Variance Swap Pricing and Discrete Monitoring Bias"
subtitle: "Research proposal | D08.01.01"
---

**Derivatives · Hedging and volatility derivatives · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Variance swaps exchange sampled squared log returns against a fixed strike. Continuous log-contract replication relies on path continuity; jumps introduce an additional economic correction. Separate sampling error from the jump correction.

## Research question

How large is the discrete-monitoring correction to variance-swap fair strikes in diffusion and jump-diffusion models, and how much of the difference from log-contract replication is due to jumps rather than discretization?

## Economic mechanism

The fair discrete variance strike is $K_{\mathrm{disc}}=T^{-1}\sum_i\mathbb E^{\mathbb Q}[X_i^2]$ for log increments $X_i$.

## Research design

Use exact Gaussian and compound-Poisson increments on the prescribed grids. Compare expected discrete variance, continuous quadratic variation and the log-contract quantity under the same risk-neutral drift; validate with independent simulation.

Verify the diffusion limit and jump moments, isolate monitoring, jump and option-strip errors, and report MC intervals even if a small correction is unresolved.

\newpage

## Required exhibits

Table of fair strikes, MC errors and confidence intervals, monitoring-frequency convergence figures, jump correction plots and strip integration convergence. Include exact GBM baseline and at least one compound-Poisson case with economically interpreted variance notional.

## Minimum viable thesis

Exact GBM and jump formulas with independent simulation validation; at least two frequencies and jump scenarios, decomposition and numerical log-contract/option-strip illustration. Report MC uncertainty even if bias is not statistically resolvable.

## Scope and feasibility

Use common nested increments when comparing monitoring frequency; independent seeds for uncertainty checks. Maintain risk-neutral compensator, payoffs in log-return variance and exact contract convention. Distinguish quadratic variation, log-contract price, variance risk premium and volatility swap; no calibration to traded quotes.

**Prerequisites:** Ito calculus, risk-neutral pricing, compound Poisson processes, Monte Carlo and numerical integration.

**Optional extension:** Add stochastic volatility or explore daily return conventions, business-day versus calendar scaling and discretization under stochastic rates.

## Milestones

W1-3: derive variance/log-contract formulas; W4-6: implement and test exact increments; W7-10: run pricing and integration grids; W11-13: convergence and jump sensitivity; W14-16: interpretation and thesis.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
