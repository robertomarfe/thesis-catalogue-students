---
title: "Testing Euler Equations with Generalized Method of Moments"
subtitle: "Research proposal | A11.03.01"
---

**Asset pricing · Cross-sectional pricing and SDF · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Consumption Euler equations can be weakly informative about preference parameters even when a numerical optimizer converges. Moment selection, weighting and identification are therefore part of the economic question, rather than nuisance implementation details.

## Research question

How sensitive are estimated CRRA preference parameters and Euler pricing errors to the selection of test assets, conditioning instruments and GMM weighting matrices? Do weakly informative moments explain instability?

## Economic mechanism

For $m=\beta g_c^{-\gamma}$, define $g(\theta)=E[z_t(m_{t+1}R_{t+1}-1)]$ for gross unit-price assets, with zero price for excess payoffs.

## Research design

Align quarterly consumption and real gross returns; retain the original bill, market and fixed-industry moment sets, lagged market instrument and preference bounds. Compare identity and two-step HAC weighting, multistart convergence, profiles and Jacobian rank.

Use quarterly parameters and same-quarter consumption/payoffs; preserve the original broad bounds and fixed moments. Report scaling, HAC bandwidth, effective rank and convergence. Validate independently on a designed simulation before empirical estimation; do not select moments after viewing rejection.

\newpage

## Required exhibits

Moment and Jacobian diagnostics, objective profile/contours, estimates with conditional inference caveats, pricing errors by asset/instrument and weighting matrix comparison; J table where defensible. Reproducible code and real return alignment test.

## Minimum viable thesis

Small overidentified CRRA GMM with verified data, two weight schemes and two fixed moment sets, simulation sanity check, profile/Jacobian and pricing-error diagnostics; valid conclusions possible even if standard asymptotics fail.

## Scope and feasibility

Bill proxy is ex-post real return, not a known real risk-free rate. No division by beta-normalized scale without retaining identifying gross moment. Verify moment count, positive-semidefinite HAC covariance and Jacobian rank; pseudoinverse/regularization changes usual J reference distribution. Document revised consumption and quarterly timing, crisis sensitivity, and no selection of moments based on rejection.

**Prerequisites:** CRRA utility and SDFs, nonlinear optimization, GMM/HAC, matrix algebra and Python SciPy/statsmodels.

**Optional extension:** Compare a parsimonious linear-factor SDF under identical moment sets, or weak-identification-robust inference after core completion.

## Milestones

W1-3: derive moments and data gate; W4-6: validate real returns and synthetic GMM; W7-10: estimate baseline and expanded moments; W11-13: profiles, inference and robustness; W14-16: write and reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
