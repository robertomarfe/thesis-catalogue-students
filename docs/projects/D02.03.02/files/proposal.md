---
title: "Calendar-Spread Arbitrage and the Construction of Volatility Surfaces"
subtitle: "Research proposal | D02.03.02"
---

**Derivatives · Vanilla pricing and surfaces · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Implied-volatility surfaces are typically fitted to separate expiries, although their option prices must also be consistent through time. Noisy quotes can violate both butterfly and calendar restrictions. Joint price constraints can improve consistency at the expense of fit; the study measures that cost and tests whether it improves recovery of the clean generating surface.

## Research question

What fit and stability costs arise from enforcing calendar and strike no-arbitrage restrictions on noisy multi-expiry option quotes?

## Economic mechanism

At normalized strike $x=K/F_T$, $c=C/(D_TF_T)$ must be nondecreasing in maturity under the stated martingale assumptions and convex in $x$. Fixed raw-strike IV monotonicity is not the test.

## Research design

Generate a five-expiry panel on a common normalized-strike grid with deterministic rates and dividends. Inject controlled noise and missing cells, then compare independent smooth slices and a jointly constrained fit. Verify interpolation and investigate the artificial finite tail anchor.

Use normalized strikes and identical forward inputs before assessing calendars. Distinguish observed masks, withheld truth and artificial tail anchors; check between-node restrictions and report solver slacks and adjustment cost.

\newpage

## Required exhibits

Quote and fit surfaces, violation heatmaps, residuals and held-out RMSE, constraint slack/solver status and interpolation diagnostics.

## Minimum viable thesis

One clean truth, three noise levels, unconstrained versus jointly constrained fits on five maturities, checked constraints and held-out comparisons.

## Scope and feasibility

Use common x-grid and explicit convex-order assumptions. A finite grid proof is not a claim about arbitrary extrapolation; test tail sensitivity and do not infer a smooth risk-neutral density from piecewise-linear prices. Unlike D02.03.01, enforce consistency jointly across maturities.

**Prerequisites:** BSM and implied volatility, convexity, constrained optimization, numerical Python.

**Optional extension:** Fit SSVI with sufficient no-arbitrage parameter restrictions and compare computational cost and wing behavior with the constrained grid.

## Milestones

W1-3: normalized pricing restrictions; W4-6: quote generator and tests; W7-9: constrained optimizer; W10-12: held-out/noise study; W13-16: interpolation audit and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
