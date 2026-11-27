---
title: "The Role of Gamma in Delta-Hedging Errors"
subtitle: "Research proposal | D04.01.02"
---

**Derivatives · Hedging and volatility derivatives · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

A delta hedge removes first-order stock exposure at the trading instant, but not option curvature between trades. The project asks whether a local curvature expansion explains the economically important part of replication errors and where it breaks down.

## Research question

How accurately does a gamma-weighted quadratic-variation error explain discrete hedging losses across strikes and maturities, and when does the approximation break down?

## Economic mechanism

For hedge minus claim, the leading discounted error increment is $-e^{-rt}\Gamma_t S_t^2\sigma^2[(\Delta W)^2-h]/2$ over a step of length $h$.

## Research design

Use exact GBM paths and nested grids, comparing exact cash-ledger error against the accumulated left-end gamma approximation across strikes and maturities. Hold the premium, path and dates fixed within each comparison.

Distinguish explanatory accuracy from D04.01.01's convergence study. Verify the sign on a single ledger, then report paired residuals, RMSE, variance ratio and tail errors normalized by spot as well as dollars.

\newpage

## Required exhibits

Tested cash ledger, gamma/error scatterplots, contract-grid heatmaps, predicted versus realized variance tables and approximation residual distributions.

## Minimum viable thesis

Verified sign and cash ledger, three strikes, three maturities and three nested grids, quantitative approximation accuracy and failure diagnostics.

## Scope and feasibility

A leading-order expansion is asymptotic, especially delicate near expiry. Avoid using terminal information to compute gamma. Same paths and notional across contracts; no transaction-cost optimization (D04.03.01) or general convergence-only study (D04.01.01).

**Prerequisites:** Stochastic calculus, BSM Greeks, Monte Carlo and numerical Python.

**Optional extension:** Compare a gamma-neutral hedge with a second option under the same diffusion, incorporating the additional rebalancing requirements explicitly.

## Milestones

W1-3: Taylor/PDE derivation; W4-6: ledger and matched paths; W7-9: contract grid and approximation; W10-12: tail and refinement tests; W13-16: interpretation and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
