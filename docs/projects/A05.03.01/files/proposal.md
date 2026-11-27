---
title: "The Predictability of Government Bond Excess Returns"
subtitle: "Research proposal | A05.03.01"
---

**Asset pricing · Fixed income and interest rates · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Predictable variation in bond excess returns is evidence about time-varying compensation for bearing duration risk. The experiment asks whether forward rates improve real-time-feasible forecasting over simple alternatives, not whether a regression fitted on the whole sample is significant.

## Research question

Can forward rates predict one-year government zero-coupon bond excess returns out of sample, relative to historical mean and slope predictors?

## Economic mechanism

With $p_t(n)=-ny_t(n)$, a one-year log excess return is $rx_{t+12}^{(n)}=p_{t+12}(n-1)-p_t(n)-y_t(1)$.

## Research design

Use the monthly 1--5 year GSW zero panel, expanding training with only matured annual returns, and historical mean, slope and forward/CP predictors. Compare common-sample OOS performance and annual nonoverlapping robustness.

Focus on predictive gains of forward information rather than the common-factor restriction in A05.03.02. Report overlap and latest-vintage pseudo-OOS limitations explicitly.

\newpage

## Required exhibits

Price/return construction tests; forward regression table; CP loading plot; OOS accuracy and sample-origin audit.

## Minimum viable thesis

GSW 1-5Y, historical mean, slope and forward/CP model; rolling-origin evaluation with matured labels and overlap-aware inference.

## Scope and feasibility

Do not use yield changes as returns or constant-maturity yield as coupon bond return. Last available estimate may be revised; overlapping outcomes and generated CP factor require robust inference. No full-sample predictor construction in OOS.

**Prerequisites:** Fixed income mathematics, regressions, HAC, Python.

**Optional extension:** Add macro predictors using actual release dates; compare real yields over available TIPS sample separately.

## Milestones

W1-3: fixed income and paper; W4-6: returns/forwards; W7-9: regressions; W10-12: OOS and inference; W13-16: replicate and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
