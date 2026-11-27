---
title: "Stochastic Volatility and the Economic Determinants of the Implied Volatility Smile"
subtitle: "Research proposal | D01.02.02"
---

**Derivatives · Vanilla pricing and surfaces · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

The level, skew and curvature of the implied volatility smile are often associated with different stochastic-volatility parameters. These associations depend on maturity and the baseline parameter vector: multiple perturbations may produce almost indistinguishable smiles. This study uses controlled Heston comparative statics rather than estimating a model from market quotes.

## Research question

Which Heston parameters control distinct smile features, and when do their effects become difficult to distinguish?

## Economic mechanism

For Heston variance with initial value $v_0$, mean-reversion rate $\kappa$ and mean $\theta$, expected integrated variance is $\theta T+(v_0-\theta)(1-e^{-\kappa T})/\kappa$. It is not generally ATM implied total variance.

## Research design

Evaluate the five Heston parameters around a common baseline on a fixed log-forward strike grid and four maturities. Use validated prices and stable implied-volatility inversion. Include a joint correlation and vol-of-vol conditioning exercise at matched expected integrated variance.

First change one parameter at a time at a common forward and grid, then explore jointly varying correlation and vol-of-vol. Report actual expected variance for every scenario, flag price bounds, and assess slope sensitivity to the strike window.

\newpage

## Required exhibits

Smile and term structure panels, sensitivity heatmaps, feature Jacobian, singular-value table, matched-scenario plots.

## Minimum viable thesis

Validated pricing and IV inversion, five parameter comparisons and one conditioning exercise. Distinct from D01.02.01's calibration objective and D02.02.01's parametric surface fitting.

## Scope and feasibility

Parameter changes affect multiple smile features jointly. Do not claim unique parameter identification from a few summaries or physical leverage estimates from Q rho. Very small option time values destabilize IV inversion; report excluded cells and use price checks.

**Prerequisites:** Stochastic calculus, option pricing, numerical integration and linear algebra.

**Optional extension:** Study local identification when maturities and strikes are unevenly sampled or add jump risk as a competing mechanism.

## Milestones

W1-3: theory and feature definitions; W4-6: pricer/IV tests; W7-9: parameter grids; W10-12: Jacobian and robustness; W13-16: figures and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
