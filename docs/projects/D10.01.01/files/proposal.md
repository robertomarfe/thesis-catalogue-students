---
title: "Modeling Commodity Spot Prices with Mean-Reverting Processes"
subtitle: "Research proposal | D10.01.01"
---

**Derivatives · International finance, FX and commodities · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Mean reversion is a natural feature of commodity-price models, but persistence is difficult to estimate and may not translate into better forecasts. Compare a physical-measure mean-reverting log-price model with a random walk, using the actual information available at each forecast origin.

## Research question

Does a mean-reverting log-spot model improve out-of-sample WTI monthly price forecasts relative to a random walk, and is any gain robust to horizon, regime and estimation window?

## Economic mechanism

For $x_t=\log S_t$, use $dx_t=\kappa(\mu-x_t)dt+\sigma dW_t^{\mathbb P}$ with $\kappa>0$.

## Research design

Use the specified monthly WTI spot averages, audited calendar and release lag. Fit the exact OU transition with expanding and 120-month rolling windows, benchmark against a random walk, and compare 1-, 3- and 12-month forecasts from identical origins. Separate zero-lag descriptive sensitivity.

Audit positivity, complete monthly dates, release lag and actual targets. Verify OU transition and random-walk limit on artificial data, report inadmissible fits and paired loss comparisons.

\newpage

## Required exhibits

Price series and parameter stability figures, half-life and uncertainty table, forecast paths and OOS loss comparison, forecast horizon/sample audit. Report log forecast versus expected level distinctly.

## Minimum viable thesis

Verified monthly spot series; OU versus random walk at 1,3,12 months with chronological evaluation, regime/rolling stability and defensible interpretation of weak or no mean reversion. Report actual forecast origin and data availability.

## Scope and feasibility

Check OU exact transition and AR forecast against simulated known parameters; test alternate sample endpoints, release lag, drift and block length for overlapping losses. If nonpositive monthly observations exist, report and use a level-model sensitivity rather than silently drop/shift; negative futures settlement is not identical to spot measure. No derivative calibration inference from P estimates.

**Prerequisites:** Stochastic processes, AR models, forecasting and Python statsmodels/SciPy. No futures dataset required.

**Optional extension:** Add a two-factor spot model or a futures/convenience-yield analysis only with a separately verified matched futures panel.

## Milestones

W1-3: verify EIA series, derive exact transition; W4-6: estimation and simulation unit tests; W7-10: OOS forecasts and loss inference; W11-13: rolling/stress sensitivities; W14-16: interpret and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
