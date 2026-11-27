---
title: "Binomial Trees versus Finite Differences for American Options"
subtitle: "Research proposal | D05.02.01"
---

**Derivatives · Numerical pricing and exotics · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

American puts require a stopping decision as well as a valuation. Two algorithms may agree on inception price yet imply different exercise boundaries, which matter economically. The thesis compares a binomial lattice and an implicit obstacle solver while holding the economic model and contract fixed.

## Research question

How do a CRR binomial tree and an implicit finite-difference obstacle solver compare in American put prices, exercise boundaries and computational efficiency?

## Economic mechanism

With payoff $g(S)=(K-S)^+$ and time to expiry $\tau$, the obstacle equation is $\min(V-g,\partial_\tau V-\mathcal LV)=0$, where $\mathcal L$ is the discounted pricing generator.

## Research design

Compare CRR and implicit finite differences for at least six American puts using the prescribed strikes, expiries, rates and volatilities. Refine the tree, spatial and temporal grids and domain separately; compare prices, exercise boundaries and runtime.

Save the time-dependent boundary or rerun shorter expiries explicitly. Report domain and odd/even effects, complementarity and interpolation uncertainty. Fix price tolerance before timing.

\newpage

## Required exhibits

Verified solvers, European benchmark and complementarity tests, price/convergence/timing tables, exercise-boundary curves and reference uncertainty.

## Minimum viable thesis

Two working American solvers, European analytical checks, independent refined references, convergence and boundary analysis for at least six contracts.

## Scope and feasibility

Do not treat simple projection after an unconstrained implicit solve as an exact LCP solution. Match time-to-expiry and boundary definitions; report interpolation error and incomplete convergence. No market price validation implied by numerical agreement.

**Prerequisites:** Derivatives pricing, numerical linear algebra, PDE basics and Python.

**Optional extension:** Add dividends or Crank-Nicolson with Rannacher smoothing, explicitly treating oscillations near the payoff kink.

## Milestones

W1-3: optimal stopping and LCP; W4-6: European/CRR solver; W7-9: implicit obstacle solver; W10-12: convergence and boundaries; W13-16: robustness and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
