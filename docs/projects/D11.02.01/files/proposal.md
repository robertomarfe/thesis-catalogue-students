---
title: "Recovering Risk-Neutral Densities from Option Prices"
subtitle: "Research proposal | D11.02.01"
---

**Derivatives · Credit risk and incomplete markets · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

A smooth option smile can mask severe instability in its second derivative. Recovering a risk-neutral distribution from limited noisy prices is an inverse problem whose economically useful outputs include tail probabilities, not simply a small quote fitting error.

## Research question

How accurately can a nonnegative risk-neutral density and its tail probabilities be recovered from sparse and noisy option prices?

## Economic mechanism

With $x=S_T/F$, $k=K/F$ and $c(k)=C(K,T)/(D_TF)$, $c(k)=\mathbb E^{\mathbb Q}[(x-k)^+]$.

## Research design

Generate the prescribed lognormal and mixture markets at several maturities and strike grids. Add the specified noise in repeated draws, compare naive differences, convex quote fits and constrained probability recovery, and assess tail probabilities and support sensitivity against exact distributions.

Do not silently clip negative density estimates and call them calibrated distributions. Track feasibility, normalization, tail sensitivity and uncertainty across the prescribed grids. Distinguish distribution recovery from smile interpolation.

\newpage

## Required exhibits

Density/CDF panels, call fit and tail error tables, diagnostics for constraints, partial-identification intervals.

## Minimum viable thesis

Two known distributions, three strike grids and noise scenarios, naive versus constrained reconstruction, mass/mean and tail diagnostics. Distinct from D02.03.01, which evaluates interpolation rather than distribution recovery.

## Scope and feasibility

Convex piecewise-linear calls imply a discrete distribution, not a smooth density. Do not interpret Q tail probabilities as physical probabilities. Finite strikes do not identify extreme tails; support constraints and smoothing are assumptions, not market information. Quote noise may cause infeasibility.

**Prerequisites:** Option pricing, numerical differentiation, constrained least squares, linear programming.

**Optional extension:** Use lawful single-date option quotes, compare bid-ask-consistent probability bounds and point estimates.

## Milestones

W1-3: derive identities; W4-6: simulate calls and implement differences; W7-9: constrained fit and tuning; W10-12: tail bounds and sensitivity; W13-16: write and package.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
