---
title: "Hansen-Jagannathan Distance and the Comparison of Asset Pricing Models"
subtitle: "Research proposal | A11.02.02"
---

**Asset pricing · Cross-sectional pricing and SDF · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

A misspecified pricing model can be compared to others by asking how much its discount factor would have to change to price the same payoff span. The Hansen–Jagannathan distance answers this question in an unrestricted quadratic metric. It is not the volatility bound and does not certify positivity.

## Research question

How do CAPM, FF3 and FF5 linear discount factors compare using Hansen-Jagannathan pricing-error distance on common test assets and independent evaluation periods?

## Economic mechanism

For gross unit-price payoffs $X$, $g=E[mX]-\mathbf{1}$ and $G=E[XX^\top]$, the unconstrained distance is $d=(g^\top G^{-1}g)^{1/2}$.

## Research design

Estimate CAPM, FF3 and FF5 affine kernels on the prescribed 25 size/value gross returns plus bill through 1994. Freeze coefficients and evaluate later dates and the separate industry panel with a common metric per comparison.

Construct gross returns including the actual monthly bill, not excess returns with unit prices. Distinguish train and holdout metrics and apply common conditioning rules; paired time-block resampling should refit the training step and evaluate common holdout draws.

\newpage

## Required exhibits

Pricing error and HJ distance tables, train/test comparison, SDF volatility and negativity diagnostics, eigenvalues and uncertainty.

## Minimum viable thesis

Three kernels, consistent gross payoff normalization and bill, common G, train/holdout distance comparisons and uncertainty with conditioning checks.

## Scope and feasibility

Not the HJ volatility bound (A11.02.01). In-sample smaller distances in nested classes partly mechanical. FF3/FF5 SMB definitions can differ. No arbitrage-free positivity guaranteed. Distances compare only given assets and common metric; held-out dates not truly unrevised data.

**Prerequisites:** SDF, factor models, matrix algebra, GMM basics and Python.

**Optional extension:** Evaluate a positivity-constrained distance or compare a consumption kernel only after matching real/nominal payoffs and prices.

## Milestones

W1-3: derive projection; W4-6: data and synthetic tests; W7-9: fit and evaluate kernels; W10-12: bootstrap and conditioning; W13-16: interpretation and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
