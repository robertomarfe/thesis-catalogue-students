---
title: "Modeling the VIX Futures Curve under Mean Reversion"
subtitle: "Research proposal | D08.02.01"
---

**Derivatives · Hedging and volatility derivatives · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

The VIX futures curve reflects both risk-neutral mean reversion and the distribution of future variance. The nonlinear square-root expectation separates state and convexity effects that would be conflated by taking the square root of expected variance.

## Research question

How do the current variance state, mean reversion and volatility-of-volatility jointly shape a model-implied VIX futures curve?

## Economic mechanism

In a diffusion CIR model, $\mathrm{VIX}_T=100\sqrt{A+Bv_T}$, $B=(1-e^{-\kappa\Delta})/(\kappa\Delta)$ and $A=\theta(1-B)$, with 30-day window $\Delta$.

## Research design

Construct curves across the prescribed variance states, mean reversion, vol-of-vol and delivery dates. Validate via independent exact-transition integration or simulation; optional spot VIX history is context, not calibration.

Separate the future conditional window from D08.01.02's realized swap variance. Check zero delivery, Jensen and convergence. Do not claim empirical futures calibration from spot observations.

\newpage

## Required exhibits

VIX futures curve families, parameter sensitivity and Jensen-gap tables, exact/MC agreement, convergence and stationary-limit diagnostics.

## Minimum viable thesis

Exact synthetic futures curve under at least three variance states and multiple kappa,xi; independent pricing validation and decomposition of state and convexity effects. Distinct from D08.01.02 integrated realized volatility swap.

## Scope and feasibility

CIR positivity/nonnegativity boundary must be handled exactly. Model assumes continuous returns, deterministic rates and theoretical VIX payoff rather than SOQ calculation; no observed futures returns, term premium or trading performance claimed. VIX spot alone cannot identify Q dynamics.

**Prerequisites:** Risk-neutral valuation, square-root diffusions, noncentral chi-square distribution and Python.

**Optional extension:** Compare one- and two-factor variance models or calibrate to synthetic VIX futures with held-out maturities.

## Milestones

W1-3: derive VIX approximation; W4-6: CIR transition and quadrature; W7-9: curve experiments; W10-12: sensitivity and limits; W13-16: documentation and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
