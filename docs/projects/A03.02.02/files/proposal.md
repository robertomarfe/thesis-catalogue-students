---
title: "Habit, Risk Aversion and the Volatility of Asset Prices"
subtitle: "Research proposal | A03.02.02"
---

**Asset pricing · Consumption-based asset pricing and equity term structures · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Persistent habit-related states can change the valuation of many future cash flows, not merely the price of a one-period shock. The same surplus distribution can therefore support different valuation dynamics.

## Research question

How does surplus-consumption persistence interact with risk aversion to generate price-dividend and return volatility, and what trade-off emerges for the risk-free rate?

## Economic mechanism

For a symmetric two-state Markov chain with stay probability $p$, the stationary law is $(1/2,1/2)$ for $0<p<1$, and the nontrivial eigenvalue is $2p-1$.

## Research design

Annual two-state fixed marginal surplus; prescribed stay grid and feasible joint shock mass, exact stationary moments and independent simulation.

For every persistence value record transition probabilities, realized conditional shock-surplus covariance, stationary law, mean and SD of log P/D, conditional rate and premium, and stationary second moments including between-state variation. Compare independent-coupling and constant-surplus controls; independently simulate one interior case with burn-in and MC uncertainty.

\newpage

## Required exhibits

Admissibility map, state-by-state q/Rf, moment tables, persistence/gamma comparative statics and CRRA diagnostics.

## Minimum viable thesis

Finite-state solution with fixed marginal surplus, at least four persistence values, CRRA benchmark, exact moments and price-existence checks. Distinct from A03.02.01 by persistence comparative statics and valuation volatility trade-off.

## Scope and feasibility

Stylized finite-state external habit, not Campbell-Cochrane's nonlinear surplus process. No negative consumption or surplus; check price existence and numerical residual. Mean-preserving persistence experiment also changes coupling feasibility; report realized growth-surplus correlation. Do not discard failed parameters silently or claim exact empirical calibration.

**Prerequisites:** Consumption-based asset pricing, Markov chains, matrix algebra and Python.

**Optional extension:** Use a three-state surplus grid or minimize a small moment criterion against observed consumption and valuation moments subject to admissibility.

## Milestones

W1-3: derive SDF and prices; W4-6: construct transition law and checks; W7-9: compute moments; W10-12: parameter trade-offs and optional targets; W13-16: interpretation and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
