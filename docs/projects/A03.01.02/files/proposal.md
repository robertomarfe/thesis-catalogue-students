---
title: "The Risk-Free Rate Puzzle under Time-Additive Utility"
subtitle: "Research proposal | A03.01.02"
---

**Asset pricing · Consumption-based asset pricing and equity term structures · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

The mean and variability of real safe rates test both impatience and the dynamics of marginal utility. Predictable growth can generate conditional rate variation even with constant preferences.

## Research question

Can time-additive power utility with plausible risk aversion and discounting reproduce both the mean and time variation of real short rates given observed US consumption growth?

## Economic mechanism

If $g_{t+1}=\mu+\phi(g_t-\mu)+\sigma\epsilon_{t+1}$ is conditionally Gaussian, then $\log R_{f,t}=-\log\beta+\gamma E_t[g_{t+1}]-\gamma^2\sigma^2/2$.

## Research design

Same quarterly inputs as the joint equity puzzle; compare iid and stationary AR(1) conditional rate moments and parameter frontier, using only contiguous lags.

Provide calendar-aware pair counts and separate fitted conditional rate mean/SD from ex-post real bill mean/SD; test the Gaussian formula by quadrature. Derive beta frontier, retain beta outside (0,1) as inadmissible, and include uncertainty in AR persistence and conditional variance; a rate-volatility mismatch need not imply rejection solely of gamma.

\newpage

## Required exhibits

Consumption moments, implied rate contour plots, discount-factor feasibility frontier, model/data moments table, AR(1) predicted rate and empirical proxy plots.

## Minimum viable thesis

Derivation, iid and conditional mean cases, documented quarterly consumption/bill dataset and rate-moment/parameter frontier analysis.

## Scope and feasibility

Check aggregation and revised data; include alternative sample excluding pandemic quarters, and optional verified TIPS yields as longer-maturity context only. Ex post proxy variance includes unexpected inflation and rolling-rate uncertainty; cannot interpret difference as exact model rejection. Constant iid conditional variance cannot generate rate variation. Do not optimize all parameters merely to hit moments.

**Prerequisites:** Expected utility, macro-finance, lognormal moments and time-series regression.

**Optional extension:** Compare with recursive preferences or time-varying consumption uncertainty after baseline; avoid duplicating A03.01.01's equity premium target.

## Milestones

W1-3: derive SDF and rate; W4-5: data and units; W6-8: consumption models; W9-12: parameter grid and moment uncertainty; W13-16: robustness and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
