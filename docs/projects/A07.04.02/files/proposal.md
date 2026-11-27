---
title: "Are Equity Factor Premia Compensation for Crash Risk?"
subtitle: "Research proposal | A07.04.02"
---

**Asset pricing · Volatility forecasting and tail risk · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Risk compensation is often motivated by poor payoffs in states where marginal utility is high. Severe market downturns provide an imperfect empirical proxy for such states. This thesis asks whether a predetermined measure of crash exposure helps explain subsequent return differences, rather than interpreting same-sample crashes as proof of a premium.

## Research question

Do factor strategies with worse payoffs in market crashes earn higher average excess returns, and is the relation robust to ordinary market beta and sampling uncertainty?

## Economic mechanism

For a past-estimated lower quantile $c_t$, define $D_t=\mathbf1_{\{r_{M,t}^e<c_t\}}$. Crash exposure may be defined from conditional residual payoffs after removing ordinary market beta; the cutoff must be known before the return is realized.

## Research design

Use the prescribed factor set descriptively and a larger portfolio cross section for pricing tests. Estimate exposures from past data, compare held-out sorts and cross-sectional returns, and resample dates jointly while retaining the influence of sparse crash observations.

Do not infer compensation from contemporaneous bad payoffs alone. Predetermine thresholds, retain sparse-event limitations and report alternative measures and noncrash placebo states. Factor spreads and long-only portfolio excess returns require different RF treatment.

\newpage

## Required exhibits

Crash event counts and payoff table; exposure estimates; portfolio return contrasts; joint uncertainty and leave-crisis-out diagnostics.

## Minimum viable thesis

Prespecified factor and portfolio set, rolling crash-exposure measure, held-out return contrasts and joint bootstrap.

## Scope and feasibility

Avoid post hoc crash definition and same-sample sorting. Tail observations sparse; do not equate negative crash exposure with proof of priced crash risk. Account for overlapping portfolios and model uncertainty.

**Prerequisites:** Factor pricing, tail measures, regression, bootstrap, Python.

**Optional extension:** Compare downside beta, coskewness and crash exposure as competing risk measures on common assets.

## Milestones

W1-3: theory and sample; W4-6: event/exposure design; W7-9: held-out tests; W10-12: uncertainty; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
