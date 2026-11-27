---
title: "Long-Run Consumption Risk and the Equity Premium"
subtitle: "Research proposal | A03.03.02"
---

**Asset pricing · Consumption-based asset pricing and equity term structures · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Persistent expected growth changes the distribution of multi-period consumption without requiring more one-period volatility. Recursive preferences make continuation risk relevant, allowing a direct comparison of long-run and contemporaneous risk.

## Research question

Holding the unconditional distribution of consumption growth fixed, how do persistence of expected growth and recursive preferences jointly change equity premia, valuation volatility and the risk-free rate?

## Economic mechanism

Let $\theta=(1-\gamma)/(1-1/\psi)$ and $w=P_C/C$. The EZ kernel is $m=\beta^\theta G^{-\gamma}[(1+w_j)/w_i]^{\theta-1}$.

## Research design

Two-state exact EZ and separate dividend claims; match one-period mean/variance across state amplitudes and hold the full stationary marginal fixed within each persistence grid; log-linear diagnostic.

Within each fixed a compare rho holding all other primitives fixed; report VR(h), stationary premium and rate, P/D and return volatility, matched CRRA and strict iid, spectral margins and all rejected cells. Independent finite-horizon wealth convergence and quadrature SDF kernels; if pricing with approximate wealth, report its own Euler errors and both premium/yield implications. No claim this replicates BY stochastic-volatility calibration.

\newpage

## Required exhibits

Euler residuals/admissibility table; comparative statics of wealth and dividend premia, real rf and valuation volatility; growth variance-ratio and approximation error plots.

## Minimum viable thesis

Two-state exact EZ solution, verified pricing kernel and dividend claim, matched consumption mean/SD comparison across persistence and preferences, log-linear diagnostic. Distinct from A03.03.01 preference separation itself.

## Scope and feasibility

Finite-state model is stylized; no claim to replicate BY 2004. Fixed unconditional consumption SD does not fix higher-horizon variance; annual parameters not monthly. Solve exact benchmark before log-linearization, report spectral radius and ill-conditioning. No time-varying volatility baseline; extension separate.

**Prerequisites:** Recursive preferences, Markov chains, asset pricing, nonlinear equations and numerical linear algebra.

**Optional extension:** Add two volatility states or estimate a/rho from consumption; retain fixed preferences and avoid weakly identified overfitting.

## Milestones

W1-3: EZ and BY reading; W4-6: exact wealth solver; W7-9: dividend claims and Euler tests; W10-12: persistence and preferences; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
