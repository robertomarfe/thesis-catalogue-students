---
title: "Discretizing the Heston Model: Bias, Stability and Computational Cost"
subtitle: "Research proposal | D05.04.01"
---

**Derivatives · Numerical pricing and exotics · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Under stochastic volatility the variance can approach zero, where Euler approximations may produce negative latent states or distorted stock dynamics. A nonnegative variance scheme is not necessarily an accurate pricer. This project compares weak pricing bias and computational cost, including near-boundary regimes.

## Research question

Which time-discretization schemes achieve reliable Heston prices at a fixed computation budget, including near-boundary parameter regimes?

## Economic mechanism

For Heston variance $dv=\kappa(\theta-v)dt+\xi\sqrt v\,dW^v$, the Feller condition $2\kappa\theta\ge\xi^2$ controls boundary accessibility, not numerical accuracy.

## Research design

Compare two Euler variants and QE-M on the specified volatility-of-volatility, maturity and strike grid. Use 12–1000 steps per year, repeated seeds, independent European prices and unchanged Asian fixing dates.

Use nested Brownian increments for Euler comparisons and independent replications. Separate path-count error from time-step error. Keep fixing dates constant and report high-vol-of-vol failures.

\newpage

## Required exhibits

Scheme pseudocode and tests; bias/SE/runtime plots; boundary diagnostic; exotic sensitivity and convergence table.

## Minimum viable thesis

Two Euler schemes plus QE-M, two variance regimes, European references and convergence/cost comparison.

## Scope and feasibility

Keep monitoring fixed when refining simulation; compare confidence intervals rather than absolute sample discrepancies. Do not silently clip states or call finest MC exact. Time hardware and setup consistently.

**Prerequisites:** SDEs, Monte Carlo, characteristic functions, Python.

**Optional extension:** Exact CIR transition with approximate integrated variance; compare with Broadie-Kaya exact joint benchmark if feasible.

## Milestones

W1-3: model and schemes; W4-6: reference and Euler; W7-9: QE-M; W10-12: convergence grid; W13-16: exotic and report.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
