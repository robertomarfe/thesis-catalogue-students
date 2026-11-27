---
title: "The Impact of Non-Normal Returns on European Option Pricing"
subtitle: "Research proposal | D01.01.03"
---

**Derivatives · Vanilla pricing and surfaces · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Vanilla options reveal distributional information beyond mean and variance because their payoffs are nonlinear. A controlled terminal-distribution experiment can isolate how asymmetry and tail thickness affect the smile without confounding the comparison with a different forward or log-return variance. The task is not to recover a unique distribution from its first four moments.

## Research question

How do risk-neutral skewness and excess kurtosis change European option prices and implied volatility smiles when forward and log variance are matched?

## Economic mechanism

For normalized log spot $X=\log(S_T/F)$, impose $\mathbb E^{\mathbb Q}[e^X]=1$. Matching $\operatorname{Var}(X)$ still leaves higher moments and the nonlinear payoff expectation unrestricted.

## Research design

Generate a Gaussian law, a symmetric variance mixture and asymmetric location mixtures (including a mirror case). Match forward and log variance at each selected maturity. Compare conditional analytic option prices to independent Monte Carlo and use a common forward-moneyness grid.

Match log variance and forward before reporting skew or kurtosis. Include a symmetric variance mixture, an asymmetric location mixture and its mirror. Use the same strike coordinates and display the actual moments alongside the smile; the arithmetic variance match is a robustness exercise.

\newpage

## Required exhibits

Density and moment tables, option price differences, IV smiles, skew/wing metrics and analytic/MC diagnostics.

## Minimum viable thesis

At one maturity: Gaussian and at least three mixture cases, exact forward/log variance matches, analytic pricing, no-arbitrage checks and smile comparisons. Distinct from D01.01.01 sensitivities and D01.01.02 dynamic hedging.

## Scope and feasibility

Distributions are terminal Q marginals, not dynamic hedging models; maturity-by-maturity construction need not be calendar-arbitrage-free. Do not infer Q tails from P returns. IV inversions near price bounds can be unstable; use explicit tolerance and flags. Cumulants are descriptive, not sufficient statistics for all strikes.

**Prerequisites:** Probability, lognormal pricing, numerical root finding and Python.

**Optional extension:** Use a martingale jump-diffusion over all maturities to study how skew and kurtosis vary jointly with maturity.

## Milestones

W1-3: Q moments and pricing; W4-6: construct mixtures and validate prices; W7-9: smile analysis; W10-12: alternate matching and MC checks; W13-16: interpretation and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
