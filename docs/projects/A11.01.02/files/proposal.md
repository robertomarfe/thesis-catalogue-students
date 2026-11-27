---
title: "From Factor Betas to Stochastic Discount Factors"
subtitle: "Research proposal | A11.01.02"
---

**Asset pricing · Cross-sectional pricing and SDF · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Beta pricing and a linear stochastic discount factor are often presented as different empirical approaches. Under a common normalization and weighting matrix they can be two parameterizations of the same restrictions. Differences in estimates may instead reflect constraints, weights or the treatment of traded factors.

## Research question

When do beta-pricing and linear SDF estimators produce identical pricing errors, and how do weighting and traded-factor restrictions change the conclusions on common test assets?

## Economic mechanism

With $B=\operatorname{Cov}(x,f)\Sigma_f^{-1}$ and $\lambda=\Sigma_f b$, $E[mx]=\mu_x-B\lambda$ for $m=1-b^\top(f-E[f])$.

## Research design

Use the original common monthly FF3, 25 size/value and 30 industry panels over 1965–2025. Compare the two representations with identical inputs and weights, then impose the traded-factor premium restriction and examine uncertainty and conditioning.

Use identical sample conventions for both representations and common WLS weights; verify error equivalence before varying weights. Separate free versus traded lambda, report rank, sign diagnostics and joint date-block refits.

\newpage

## Required exhibits

Algebraic proof and unit tests, matched residual table, lambda and b estimates, pricing RMSE/weighted loss and bootstrap intervals, rank and SDF-sign diagnostics.

## Minimum viable thesis

Two representations derived and verified, FF3 on two portfolio panels, matched weighting, traded/free lambda and uncertainty diagnostics.

## Scope and feasibility

Do not compare unlike weighting matrices, means or sample periods as a test of equivalence. Estimated traded factors may be misspecified. No claim that a normalized linear SDF is a positive equilibrium pricing kernel. Distinct from A11.02.01 HJ bound and A01.02.01 model selection.

**Prerequisites:** Asset pricing, linear algebra, covariance estimation, regression and basic GMM.

**Optional extension:** Compare the GMM implementation with a two-pass estimator using identical moment restrictions; discuss generated-beta and weak-factor inference.

## Milestones

W1-3: derivations; W4-6: simulation and data tests; W7-9: matched empirical estimators; W10-12: weights and bootstrap; W13-16: diagnostics and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
