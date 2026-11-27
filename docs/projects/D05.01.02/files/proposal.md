---
title: "Quasi-Monte Carlo Methods for Path-Dependent Options"
subtitle: "Research proposal | D05.01.02"
---

**Derivatives · Numerical pricing and exotics · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Even a simple diffusion generates high-dimensional integration problems when payoffs depend on many observations. Low-discrepancy sampling changes the integration design; bridge ordering changes which Gaussian coordinates represent important path variation. The thesis evaluates both mechanisms while preserving the payoff and observation dates.

## Research question

When do scrambled Sobol sequences and Brownian bridge ordering improve the accuracy and runtime of Asian option pricing compared with plain Monte Carlo?

## Economic mechanism

For $a<t<b$, $W_t$ conditional on $W_a,W_b$ is normal with mean $[(b-t)W_a+(t-a)W_b]/(b-a)$ and variance $(t-a)(b-t)/(b-a)$. Ordering does not change the Brownian law.

## Research design

Compare IID Monte Carlo, scrambled Sobol with chronological increments, and scrambled Sobol with bridge ordering for 12, 52 and 252 fixings. Use powers of two and at least 24 independent randomizations, with geometric and independent arithmetic references.

Check Gaussian covariance before pricing. If reference uncertainty prevents ranking, increase the reference budget or label the result unresolved. The exercise measures integration error, not continuous-monitoring discretization.

\newpage

## Required exhibits

Validated generators, reference precision table, estimator RMSE and timing curves, convergence slopes with caveats and reproducible seed list.

## Minimum viable thesis

All three estimators, exact geometric benchmark and independently validated arithmetic reference, two monitoring dimensions and three sample budgets with replicated error/timing analysis.

## Scope and feasibility

Use independent randomizations, same hardware and repeated timing; avoid ordinary IID confidence intervals for low-discrepancy samples. Clip inverse-CDF endpoints only by a documented machine-precision rule. Report deep OTM cases with rare positive payoffs separately. The exercise compares integration error, not market accuracy or discretization of continuous monitoring.

**Prerequisites:** Monte Carlo, multivariate normals, Python SciPy qmc and numerical benchmarking. No market data required.

**Optional extension:** Combine RQMC with control variates or PCA path construction; baseline must isolate sampling and coordinate-ordering effects.

## Milestones

W1-3: study Sobol and bridge; W4-6: implement and test path generators; W7-10: run benchmarks; W11-13: dimension and payoff sensitivity; W14-16: document and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
