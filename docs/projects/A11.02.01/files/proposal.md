---
title: "The Hansen-Jagannathan Bound and the Volatility of the Pricing Kernel"
subtitle: "Research proposal | A11.02.01"
---

**Asset pricing · Cross-sectional pricing and SDF · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

The Hansen–Jagannathan volatility bound quantifies how variable a pricing kernel must be to price a set of traded excess payoffs. Adding assets can tighten the restriction, but the sample bound also becomes more vulnerable to covariance estimation error. Consumption growth provides an economic benchmark rather than a guaranteed pricing model.

## Research question

How does the minimum SDF volatility implied by US portfolio returns increase as test assets are added, and can a calibrated consumption-based SDF plausibly satisfy the resulting restrictions?

## Economic mechanism

For real excess payoffs $x$, $E[mx]=0$ implies $\operatorname{sd}(m)/E[m]\ge(\mu_x^\top\Sigma_x^{-1}\mu_x)^{1/2}$ when $E[m]>0$ and covariance is nonsingular.

## Research design

Construct complete quarterly real total and bill returns, match the consumption series and apply the original three nested asset menus and CRRA parameter grid. Compare bound, kernel dispersion and actual Euler errors, with rank and sampling diagnostics.

Use identical complete quarters for all nested sets. Report raw covariance spectrum, rank policy, bootstrap and labeled shrinkage sensitivity; never claim an observed constant real bill or infer rejection solely from a sample bound gap.

\newpage

## Required exhibits

HJ bound by asset set, covariance condition numbers and uncertainty, CRRA volatility-versus-gamma plot, pricing errors table, real/nominal conversion and quarterly sample audit. Report all measures in quarterly units or transparently annualized Sharpe, not mixed frequencies.

## Minimum viable thesis

Verified quarterly matched data, derivation and computation for three nested asset sets, comparison with CRRA SDF grid, uncertainty and conditioning checks. No claim of model rejection from bound gap alone without sampling inference.

## Scope and feasibility

Use excess returns of real bill proxy, not known constant real risk-free; bill is nominal before deflation. Singular covariance requires pseudoinverse only with range/finite bound check; distinguish numerical redundancy. Use common sample and uncertainty; larger raw sample bound may reflect overfit. Total consumption is a proxy for utility-relevant consumption; sensitivity to crises and consumption definition only if BEA series verified.

**Prerequisites:** SDF theory, covariance and matrix inversion, portfolio theory, elementary bootstrap and Python.

**Optional extension:** Construct the full HJ mean-SD frontier using gross returns and alternative SDF means, or impose nonnegative state prices via convex optimization.

## Milestones

W1-3: derive bound and confirm data; W4-6: align real returns and unit-test covariance formulas; W7-10: nested assets and CRRA comparison; W11-13: bootstrap/conditioning robustness; W14-16: interpret and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
