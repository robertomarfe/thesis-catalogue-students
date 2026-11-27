---
title: "Habit Formation and Time-Varying Equity Risk Premia"
subtitle: "Research proposal | A03.02.01"
---

**Asset pricing · Consumption-based asset pricing and equity term structures · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Even when consumption growth and the surplus-state transition have unchanged marginal distributions, their coupling can alter the covariance of marginal utility with payoffs. This isolates a mechanism distinct from a change in unconditional volatility.

## Research question

How does the dependence of surplus consumption on consumption shocks change conditional risk prices, equity premia and risk-free rates relative to a CRRA benchmark?

## Economic mechanism

For external habit surplus share $S_t>0$, the kernel is $m=\beta(G S_{t+1}/S_t)^{-\gamma}$.

## Research design

Quarterly three-state surplus model; fixed transition and shock marginals, change only their coupling, then vary move probability and gamma.

Verify each conditional joint row sums to one, shock marginals and P are identical across coupling cases, same stationary weights, CRRA constant-surplus and Euler checks. Show covariance identity by state and distinguish SDF volatility from priced covariance; retain nonfinite present-value cells.

\newpage

## Required exhibits

Transition matrices, pricing and Euler tests, state-dependent SDF and return tables, spectral radius diagnostics and comparative-static plots.

## Minimum viable thesis

Exact finite-state solution with CRRA benchmark, dependent/independent surplus cases, state-dependent risk prices and comparative statics, including feasibility and risk-free diagnostics.

## Scope and feasibility

The bounded surplus process is exogenous external habit, not the original continuous surplus law or full general equilibrium calibration. Countercyclical premia are a hypothesis, not imposed; boundary effects and risk-free variation must be reported. Keep annual/quarterly preference units consistent.

**Prerequisites:** Consumption-based asset pricing, Markov chains, linear algebra, numerical methods and Python.

**Optional extension:** Approximate the Campbell-Cochrane surplus sensitivity function on a refined grid and compare risk-free stabilization; optionally match public consumption moments after acquisition.

## Milestones

W1-3: habit and SDF derivation; W4-6: finite-state transitions and solver; W7-9: benchmarks and state outcomes; W10-12: comparative statics; W13-16: economic interpretation and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
