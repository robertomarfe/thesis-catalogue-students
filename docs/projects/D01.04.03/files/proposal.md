---
title: "Model Complexity versus Pricing Accuracy in Modern Option Pricing"
subtitle: "Research proposal | D01.04.03"
---

**Derivatives · Vanilla pricing and surfaces · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Additional parameters reduce an in-sample pricing objective only when they provide flexibility in the relevant directions. They can also increase numerical cost and estimation uncertainty. This project evaluates model complexity through three distinct outcomes: held-out price accuracy, stability of parameters and computation time, rather than treating the best fit as the best model.

## Research question

When is added pricing-model complexity justified by held-out surface accuracy, parameter stability and computational cost rather than in-sample fit alone?

## Economic mechanism

For parameter vector $\vartheta$, fit training prices using a common weighted loss $\sum_i w_i[C_i(\vartheta)-C_i^{obs}]^2$. Report held-out errors, parameter uncertainty and timing separately; adding parameters does not establish identification.

## Research design

Construct independent clean and noisy panels from Black–Scholes, Merton and Heston. Compare three fitted model families using frozen training/validation/holdout contracts, including a withheld maturity. Match numerical tolerances and record runtime, failed starts and noise-free versus noisy targets.

Record noise draws, holdouts, solver starts and comparable timing rules before fitting. Separate nested limits, recovery under correct specification and prediction under misspecification. Rank models using predeclared metrics, not whichever metric favors one model.

\newpage

## Required exhibits

Model/DGP error matrix, price accuracy-versus-runtime plot, parameter stability and failure counts, held-out maturity errors.

## Minimum viable thesis

Three models, two truth DGPs, frozen holdouts, matched accuracy targets, multistart and runtime report.

## Scope and feasibility

Use comparable optimizer budgets and recorded tolerances; no universal model ranking from selected DGPs. Bid/ask perturbations may create arbitrage; document cleaning and use clean truth for independent scoring. Separate extrapolation and interpolation.

**Prerequisites:** Derivative pricing, numerical integration, constrained optimization, statistics.

**Optional extension:** Add a prespecified SVI slice baseline or an extra advanced model, distinguishing static surface fit from dynamic pricing.

## Milestones

W1-3: models and objectives; W4-6: independent pricers; W7-9: calibration; W10-12: perturbation and holdout; W13-16: report.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
