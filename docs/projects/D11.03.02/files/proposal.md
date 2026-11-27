---
title: "Robust Option Pricing under Uncertain Volatility"
subtitle: "Research proposal | D11.03.02"
---

**Derivatives · Credit risk and incomplete markets · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

A trader who cannot specify a unique future volatility process may instead consider all admissible volatilities inside a band. Robust valuation then responds to the curvature of the payoff, not merely to two constant-volatility prices.

## Research question

How wide are robust upper and lower option values under bounded volatility, and why do non-convex payoffs differ from simple calls?

## Economic mechanism

The upper value uses $\max_{\sigma\in[\sigma_L,\sigma_H]}\tfrac12\sigma^2 S^2V_{SS}$ in its pricing PDE; the lower value uses the minimum.

## Research design

Use the prescribed volatility bands, call, butterfly and call spread. Implement monotone finite differences with appropriate boundaries and an independent controlled-tree or policy benchmark. Compare constant-volatility values, degenerate band and refinement.

Use the degenerate band and convex call limits to check sign and units; record instability and boundary effects. Distinguish the worst-case dynamic control from a search over constant volatilities.

\newpage

## Required exhibits

Convergence table; robust price intervals and constant-vol comparison; gamma/control map; discrete hedge shortfall analysis.

## Minimum viable thesis

Monotone solver, BSM and convex benchmark, butterfly price bounds and convergence/constant-vol comparison. Hedge replay secondary if time permits.

## Scope and feasibility

Non-convex bounds need dynamic controls, not extrema of constant vol prices. Check stability, boundary sensitivity and discrete comparison principle. Finite sampled paths do not prove superhedging. No empirical volatility-band estimate required.

**Prerequisites:** PDEs, stochastic control, BSM and numerical analysis; Python.

**Optional extension:** Include discrete quoted vanilla constraints or alternative uncertain-drift/transaction-cost models, keeping assumptions separate.

## Milestones

W1-3: theory; W4-6: solver; W7-9: benchmark/refine; W10-12: nonconvex and hedge checks; W13-16: writing and code.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
