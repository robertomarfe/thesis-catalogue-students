---
title: "Stochastic Volatility versus Jump Risk: Explaining the Implied Volatility Skew"
subtitle: "Research proposal | D01.03.02"
---

**Derivatives · Vanilla pricing and surfaces · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Negative equity option skew can arise from diffusive leverage or from discontinuous returns. A fit to a restricted set of quotes may not distinguish these mechanisms. This project compares two competing risk-neutral models against known synthetic truth, using held-out maturity and strike information to assess their discriminatory power.

## Research question

Can Heston and Merton models fit the same noisy synthetic vanilla quotes, and which maturity and strike diagnostics discriminate between the two mechanisms?

## Economic mechanism

Both models obey $\mathbb E^{\mathbb Q}[S_T]=F$, the common forward, but diffusive leverage and jumps generate different conditional dynamics. Compare their option-price predictions on contracts excluded from both fits.

## Research design

Generate separate Heston and Merton truth panels over five maturities, with identical controlled noise conventions. Fit both models on selected strikes at three central maturities, withholding short and long maturities. Use multistart calibration, shared error units and independently checked prices.

Generate a separate Heston and Merton truth panel. Use the same objective, bounds policy, numerical precision and untouched test grid across fitted models; report model-dependent failures and do not select short maturities after inspecting errors.

\newpage

## Required exhibits

Smile panels, calibration and held-out tables, parameter profile, residual heatmap and pricing error audit.

## Minimum viable thesis

Two synthetic panels, two calibrated models, held-out strikes/maturities and multistart diagnostic.

## Scope and feasibility

Synthetic model discrimination is not empirical identification. Match quotes, weights, search budget and tolerances; avoid nearly zero vega. No actual option database or structural claim. Unlike D01.03.01, this is cross-model calibration and holdout.

**Prerequisites:** Stochastic calculus, characteristic functions, optimization, Python.

**Optional extension:** Compare Bates model with a parameter-count penalty or barrier prices under observationally similar vanillas.

## Milestones

W1-3: models; W4-6: independent pricing; W7-9: calibration; W10-12: holdouts and profiles; W13-16: writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
