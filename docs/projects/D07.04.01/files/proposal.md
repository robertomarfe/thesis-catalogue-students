---
title: "HJM and the No-Arbitrage Dynamics of Forward Rates"
subtitle: "Research proposal | D07.04.01"
---

**Derivatives · Fixed income and interest rates · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

The HJM drift restriction ties forward-rate changes to discount-bond no-arbitrage. Finite grids can violate the continuous-time martingale identity numerically even when the model is correct. Distinguish this error from a genuinely misspecified zero-drift forward model.

## Research question

How does the HJM drift restriction discipline the evolution of discount bond prices, and how large are discretization errors when a continuous-time no-arbitrage model is implemented on a finite grid?

## Economic mechanism

Under money-market $\mathbb Q$, $df(t,T)=\alpha(t,T)dt+\sigma(t,T)dW_t$, with $\alpha(t,T)=\sigma(t,T)\int_t^T\sigma(t,v)dv$.

## Research design

Use the prescribed deterministic exponential volatility, smooth initial curve and nested time grids. Compute discount bonds on a fixed maturity grid and the bank account from diagonal forwards. Couple paths on the common refinement of the grids. Compare discounted bond martingale estimates with independent Gaussian references and a deliberately wrong zero-drift specification.

Keep the counterexample labeled inadmissible under money-market Q, not an alternative calibrated pricing model. Separate integration bias, sampling uncertainty and runtime.

\newpage

## Required exhibits

Forward and bond evolution plots, discounted-price errors in bp of initial notional with MC intervals, convergence and runtime table, factor loading curves.

## Minimum viable thesis

One-factor deterministic volatility HJM, analytic drift, three maturity/grid checks and zero-drift counterexample; agreement with benchmark within numerical and MC tolerance.

## Scope and feasibility

Do not infer physical forecasts from Q drift. Distinguish MC sampling, quadrature and time-step error; time-to-maturity coordinates require a transport term. Do not claim exact no-arbitrage for arbitrary numerical interpolants.

**Prerequisites:** Stochastic calculus, bond math, Gaussian processes, numerical quadrature, Python.

**Optional extension:** Add a second factor and compare Gaussian bond-option prices with a jointly simulated discounted payoff.

## Milestones

W1-3: derive restriction and quote conventions; W4-6: exact reference and grid tests; W7-9: paired MC; W10-12: factor/grid robustness; W13-16: write and reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
