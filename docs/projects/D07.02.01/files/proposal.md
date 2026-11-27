---
title: "Calibrating Hull-White to the Initial Yield Curve"
subtitle: "Research proposal | D07.02.01"
---

**Derivatives · Fixed income and interest rates · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Exact fitting of today's discount curve removes cross-model discrepancies due to initial term structures, but cannot identify future rate volatility or mean reversion. Study how this distinction translates into bond-option values across the specified curve shapes and parameter configurations.

## Research question

How does Hull-White exact initial-curve fitting affect bond-option prices, and how much valuation uncertainty remains after all models fit the same curve?

## Economic mechanism

Under $\mathbb Q$, set $r_t=x_t+\varphi(t)$, $dx_t=-a x_tdt+\sigma dW_t$, $x_0=0$.

## Research design

Construct the three prescribed smooth synthetic forward curves and parameter grids. Recover their discounts using the Hull-White shift, compare an unshifted Vasicek least-squares fit and price bond options. Check the analytical result against an independent Gaussian benchmark; GSW is optional only.

Report curve recovery, price and numerical error separately; evaluate all prescribed curves and a range of option parameters. Do not present an exact fit as evidence that option values are identified.

\newpage

## Required exhibits

Input/recovered curves, fit-error table, option sensitivity heatmaps, MC validation, interpolation diagnostic.

## Minimum viable thesis

Three synthetic curves, exact shift/discount recovery, analytical bond option and independent validation at multiple a,sigma. Optional GSW makes empirical illustration richer but is not required.

## Scope and feasibility

Government fitted curves are not collateralized swap/OIS curves. No swaption volatility data needed for core; parameters are scenarios, not calibrated to market option prices. Avoid differentiating noisy discrete rates without interpolation; do not confuse fit of initial discount factors with model validation.

**Prerequisites:** Fixed income, Gaussian processes, stochastic discounting and Python.

**Optional extension:** Calibrate a,sigma on generated caplet or swaption quotes and assess identification using a Jacobian/synthetic holdout.

## Milestones

W1-3: derive shift and pricing; W4-6: implement curves and Gaussian integrals; W7-9: bond-option benchmark; W10-12: sensitivity and optional GSW; W13-16: write and reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
