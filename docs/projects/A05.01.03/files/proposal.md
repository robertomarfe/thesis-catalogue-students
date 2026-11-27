---
title: "Interest Rate Volatility and the Performance of Affine Term Structure Models"
subtitle: "Research proposal | A05.01.03"
---

**Asset pricing · Fixed income and interest rates · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

A conditional mean model can fit average rate movements but miss state-dependent fluctuations. This matters for risk management across maturities. Compare the variance forecasts implied by constant and level-dependent diffusion coefficients against a flexible statistical benchmark on the same eligible rate history.

## Research question

Does level-dependent short-rate volatility improve conditional variance forecasts and account for the state dependence of Treasury yield changes?

## Economic mechanism

For CIR under $\mathbb P$, with $a=e^{-\kappa h}$, $\operatorname{Var}_t(r_{t+h})=\eta^2[r_ta(1-a)+\theta(1-a)^2/2]/\kappa$.

## Research design

Align weekly DTB3 and GSW observations, using elapsed year fractions and strictly positive contiguous CIR episodes. Fit both exact transitions on a common sample, compare rolling variance or GARCH, and assess state-dependent variation of two or more yield changes. Retain a separate full-sample Gaussian diagnostic.

Use identical dates for comparisons, rate-bin diagnostics and a predeclared mean/variance scoring convention. Distinguish this variance-target experiment from A05.01.01 density forecasting.

\newpage

## Required exhibits

Transition estimates, conditional variance curves, forecast losses and rate-bin diagnostics, yield residual variance/rank table and exclusion report.

## Minimum viable thesis

Common-positive sample exact-transition Vasicek/CIR, conditional variance forecasts against rolling benchmark, rate-bin and two-maturity yield-volatility diagnostics.

## Scope and feasibility

CIR near zero can be problematic with noisy bill quotes; no silent clipping or shifting. Actual rate innovations are not observed; squared forecast residuals are noisy proxies and mean-model misspecification matters. Empirical yield loadings are not Q pricing parameters. Distinct from A05.01.01 transition fit and A05.01.02 rank-one mean reconstruction.

**Prerequisites:** Stochastic processes, likelihood, fixed income and time-series forecasting.

**Optional extension:** Estimate a two-factor model or a shifted square-root process with shift selected on training only; compare likelihood and conditional variance.

## Milestones

W1-3: derive conditional moments; W4-6: align rates and curves; W7-9: fit and validate transitions; W10-12: forecast and cross-maturity diagnostics; W13-16: write and audit.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
