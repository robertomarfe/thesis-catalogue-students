---
title: "Backtest Overfitting and the Illusion of Predictability"
subtitle: "Research proposal | A10.04.02"
---

**Asset pricing · Predictability and machine learning · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

The best-looking backtest from many candidates can appear profitable even under no predictability. The experiment separates legitimate model selection on past validation data from invalid repeated selection on final outcomes.

## Research question

How does the number of candidate predictive models affect apparent OOS performance under a no-predictability null, and how much does nested temporal validation reduce the gap between reported and independent test performance?

## Economic mechanism

Even if conditional mean is constant, the maximum of many noisy development or test scores is upward biased relative to a fixed candidate.

## Research design

Simulate T=600, 300/150/150 dates, 10/50/200 nested candidate sets, iid and conditional-variance constant-mean nulls, AR(1) predictors with phi .8, at least 300 paired replications. Real French lagged-factor illustration remains mandatory absent explicit redesign.

Perturb immature/final targets and ensure development winner is unchanged. Check nested candidate membership, paired common draws, strict boundary purge and same benchmark dates. Oracle never used in deployable policy. Real illustration remains required under original scope.

\newpage

## Required exhibits

Distribution of apparent versus fresh-test OOS R2 by M, selection gap and MC uncertainty plots, false-discovery proxy (positive reported score under null, not formal p-value), real example cumulative loss table, transparent split/seed and candidate registry.

## Minimum viable thesis

One iid and one conditional-variance null, at least three model search sizes, honest versus reused holdout with paired uncertainty, and one real-data illustration. Simulation is core; if real file unavailable, retain synthetic result and explicitly revise empirical scope.

## Scope and feasibility

Preserve predictor persistence and return volatility clustering under alternative null, no return-feature forward leakage. Avoid comparing selectors on different dates or model menus. Define selection on development versus nested training folds precisely; use equal test length and independent seeds. Report if honest selection still underperforms mean; inference about statistical false rejections requires explicit tests, not positive scores alone.

**Prerequisites:** Predictive regressions, Monte Carlo, time-series dependence, Python and basic multiple testing.

**Optional extension:** Add stationary bootstrap reality-check or multiple-testing adjustment on prespecified strategy returns; validate test size with simulations before use.

## Milestones

W1-3: selection-bias theory and preregister grid; W4-6: implement nulls and forecast unit tests; W7-10: run paired experiments and real example; W11-13: dependence and uncertainty; W14-16: write and archive reproducible registry.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
