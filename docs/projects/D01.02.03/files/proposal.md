---
title: "Comparing Local and Stochastic Volatility Models: Pricing and Hedging Performance"
subtitle: "Research proposal | D01.02.03"
---

**Derivatives · Vanilla pricing and surfaces · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Two models can reproduce the same vanilla option surface yet disagree on the law of the underlying path. Local volatility encodes the one-dimensional risk-neutral marginals; stochastic volatility retains a latent variance state. Barrier options and hedging provide a way to assess the economic relevance of this distinction while controlling the quality of the vanilla fit.

## Research question

When a local-volatility model reproduces a Heston-generated vanilla surface, how different are barrier prices and delta hedges in the Heston data-generating market?

## Economic mechanism

For call price $C(K,T)$, strike $K$, maturity $T$ and flat rates $r,q$, Dupire local variance is $2[C_T+(r-q)KC_K+qC]/(K^2C_{KK})$. This determines a marginal-consistent diffusion, not the full stochastic-volatility path law.

## Research design

Generate a high-accuracy Heston surface; recover local variance using the forward equation or conditional-variance projection. Verify withheld vanilla prices before evaluating down-and-out calls at two barriers and maturities. Simulate an independent physical Heston hedge experiment, keeping monitoring identical.

Check derivative stability and held-out vanillas before comparing barriers. Hold monitoring and strike fixed. Treat barrier state, cash funding and initial capital explicitly; record the interpolation domain and the handling of out-of-domain simulations.

\newpage

## Required exhibits

Vanilla price error map; local variance surface; exotic pricing and uncertainty table; delta-hedge distributions and stress diagnostics.

## Minimum viable thesis

One validated synthetic surface, withheld vanilla tests, one barrier family and one independent hedge experiment. Distinct from Heston calibration and surface fitting projects.

## Scope and feasibility

Vanilla agreement within tolerance is a prerequisite, not a finding. Avoid taking noisy second derivatives without positivity diagnostics. Both models' delta hedges incomplete in stochastic-vol market; report failed extrapolations, MC and discretization errors.

**Prerequisites:** Ito calculus, Heston, PDE/Monte Carlo, surface differentiation; advanced Python.

**Optional extension:** Compare forward-start options or delta-vega hedging as a separate control.

## Milestones

W1-3: theory and pricer; W4-6: surface and derivatives; W7-9: vanilla checks and barriers; W10-12: hedging/stress; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
