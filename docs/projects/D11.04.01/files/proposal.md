---
title: "Quadratic Hedging in Incomplete Markets"
subtitle: "Research proposal | D11.04.01"
---

**Derivatives · Credit risk and incomplete markets · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Incomplete spanning leaves a residual component of a claim that a traded proxy cannot hedge. A quadratic loss criterion defines an optimal projection under a specified probability law, while not creating a unique preference-free price.

## Research question

How does an unspanned shock alter minimum mean-square hedging error relative to an independence or delta benchmark, and which part of the loss cannot be hedged?

## Economic mechanism

In discounted units with $\mathbb E^{\mathbb P}[G]=0$, minimize $\mathbb E^{\mathbb P}[(H-a-bG)^2]$ over initial capital and hedge.

## Research design

Use the specified correlated lognormal assets with discounted traded stock a physical martingale. Establish the one-step projection independently, then estimate multi-period conditional hedge on training paths and evaluate on independent paths at the prescribed correlations.

Check one-period orthogonality, out-of-sample error and residual variance for zero, static, dynamic and proxy-delta hedges. Report the full-span continuous limit separately from finite-grid errors.

\newpage

## Required exhibits

Residual risk versus rho, coefficient plots, error decomposition, held-out loss table and numerical convergence.

## Minimum viable thesis

One-period exact projection and multi-period regression with three correlations and independent test paths.

## Scope and feasibility

Identical initial capital and payoff for comparisons; no drift advantage in baseline. Finite rebalancing can leave error even at rho=1. Proxy delta is a feasible control, not the exact discrete optimum.

**Prerequisites:** Probability, conditional expectations, regression, Python.

**Optional extension:** Nonzero physical risk premium with explicitly derived global mean-variance hedge, or a second hedging asset.

## Milestones

W1-3: projection; W4-6: one-step checks; W7-9: dynamic regression; W10-12: test and decomposition; W13-16: robustness and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
