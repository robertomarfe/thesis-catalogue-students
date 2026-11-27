---
title: "Equity Yield Curves across Investment Styles"
subtitle: "Research proposal | A06.02.02"
---

**Asset pricing · Consumption-based asset pricing and equity term structures · Level 2/3**

**Data:** Empirical design conditional on actual access and coverage. **Status:** current review draft; supervisor approval pending.

## Motivation

Style differences in equity valuation may vary substantially by horizon. A matched pair comparison avoids confounding the characteristic contrast with different dates and maturity coverage.

## Research question

How do the level, slope and cyclicality of model-implied equity yields differ between high and low characteristic portfolios, especially value and growth?

## Economic mechanism

For an exactly matched high/low style pair define $\Delta e_t(n)=e_{H,t}(n)-e_{L,t}(n)$.

## Research design

GKK exact high/low value-growth pair, matched 1/5/10 core and paired curve/slope analysis; additional styles only with validated labels.

Require positive-dividend portfolio IDs and validated exact high/low style crosswalk with common 1/5/10y dates; report both individual curves and paired differences/slope, joint calendar-block intervals and sensitivity across regimes. Keep matched weighting, units and vintage. If exact pair not verified, stop rather than substitute FF labels.

\newpage

## Required exhibits

Portfolio crosswalk; mean term structures; slope time series and paired uncertainty; regime comparison; documentation of model dependence.

## Minimum viable thesis

One verified value-growth pair, common 1/5/10y grid, paired curve/slope comparison, inference and clear model-implied caveat; conditional on archive. Distinct from aggregate A06.02.01 and theoretical duration A06.03.02.

## Scope and feasibility

GKK curves are estimated from a shared model, not independent observed strip quotes. Common sample, same units and vintage are essential. Bootstrap treats curves as given and omits estimation uncertainty of the underlying GKK model; acknowledge. Do not equate equity yields with expected returns or pure duration.

**Prerequisites:** Asset pricing, term structures, time-series statistics and Python.

**Optional extension:** Compare multiple anomaly pairs with multiple-testing controls; add model-provided cash-flow/return decomposition only if available.

## Milestones

W1-3: literature/archive gate; W4-6: crosswalk and baseline; W7-9: paired term structures; W10-12: regimes/robustness; W13-16: writing and replication.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
