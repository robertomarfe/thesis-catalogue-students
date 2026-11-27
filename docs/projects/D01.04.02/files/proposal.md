---
title: "Rough Volatility and the Short-Term Behavior of Option Prices"
subtitle: "Research proposal | D01.04.02"
---

**Derivatives · Vanilla pricing and surfaces · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Short-dated option skew can be steep even when the expected variance curve is smooth. Rough volatility changes the sensitivity of instantaneous variance to recent innovations. The scientific challenge is to separate the predicted short-time scaling from the numerical error in pricing options at very short expiries.

## Research question

How does the roughness parameter alter the scaling of near-ATM skew as maturity decreases, and can the predicted distinction be measured reliably with numerical prices?

## Economic mechanism

For roughness $H$ and normalized Gaussian Volterra process $Y_t$, $\operatorname{Var}(Y_t)=t^{2H}$. Near-ATM skew has leading short-time power $T^{H-1/2}$ under appropriate conditions, not an exact finite-maturity identity.

## Research design

Simulate rough Bergomi with a constant forward variance curve and roughness values 0.1, 0.25 and 0.5. Compare six maturities from one to 32 weeks. Price options on near-ATM strikes proportional to the square root of maturity; vary the strike window, numerical grid and simulation precision.

Validate the covariance and cross-covariance before simulating prices. Keep the initial variance curve and other parameters fixed across H. Separate grid refinement, sampling uncertainty and finite-maturity asymptotic bias, with a Brownian-kernel reference.

\newpage

## Required exhibits

Variance-path statistics, short-tenor smiles, log-log skew and slope uncertainty, martingale and runtime diagnostics.

## Minimum viable thesis

Two H values including .5, validated Gaussian kernel, 4+ maturities with error bars, short-skew scaling and convergence caveats.

## Scope and feasibility

Small option-price errors inflate IV derivative error. Do not claim empirical roughness estimation; synthetic H is known. Compare equal variance curves and rho; finite-T asymptotic bias, discretization and MC error must be reported separately.

**Prerequisites:** Gaussian processes, stochastic calculus, option pricing, MC and numerical linear algebra.

**Optional extension:** Compare a Markovian multifactor exponential-kernel approximation with the rough benchmark under matched error budget.

## Milestones

W1-3: Volterra kernel and asymptotics; W4-6: exact covariance and simulation; W7-9: price/skew panels; W10-12: grid and MC tests; W13-16: writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
