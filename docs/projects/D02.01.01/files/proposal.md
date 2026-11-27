---
title: "The Information Content of the Equity Index Volatility Skew"
subtitle: "Research proposal | D02.01.01"
---

**Derivatives · Vanilla pricing and surfaces · Level 2/3**

**Data:** Empirical design blocked pending authorized access and coverage; not assignable on this design. **Status:** current review draft; supervisor approval pending.

## Motivation

Option-implied skew and variance describe different aspects of the risk-neutral return distribution. The empirical question is whether the skew statistic adds information about physical downside events beyond the level of implied volatility. Risk-neutral asymmetry is not itself a probability forecast, and a historical series can change meaning when the provider revises its methodology.

## Research question

Does a consistently defined equity index option-skew measure improve forecasts of downside equity returns beyond the VIX?

## Economic mechanism

Let $Y_{t+1}$ indicate a next-month return below the fixed threshold. Compare the logit probability $\Pr(Y_{t+1}=1\mid I_t,z_t)$ with and without SKEW $z_t$, at given VIX $I_t$. These are physical event probabilities, not risk-neutral moments.

## Research design

Conditional on rights and a consistent SKEW methodology, align monthly closing SKEW and VIX with next-month compounded French broad-market returns. Use a fixed downside threshold of -5% and a chronological 60/20/20 split. The exact source vintage, calendar, coverage and event count must pass before assignment.

Do not begin an empirical claim before the source vintage and use permission pass. Freeze the -5% event and chronological split; retain all missing labels, compare common origins and discuss event scarcity rather than adjusting the threshold after inspection.

\newpage

## Required exhibits

Data audit, index correlation and event plot, coefficient and forecast-score tables, calibration curve and event-count table.

## Minimum viable thesis

One consistently defined licensed skew series, VIX and market proxy; documented event count and chronological score comparison. If unavailable, simulate Gaussian and asymmetric Q mixtures with P tail scenarios, label exercise as non-empirical and obtain supervisor approval for redesign.

## Scope and feasibility

The October 5, 2026 Cboe consultation proposed methodology changes and a restated history from 2013; confirm final decision before download. Do not splice legacy and new histories or treat back-calculated values as contemporaneous observations. FF market return is a proxy for SPX. Rare events limit statistical power; no significant incremental effect required.

**Prerequisites:** Option pricing, logistic regression, probability, time-series validation and Python.

**Optional extension:** If lawful strike-level option data become available, compare third-moment index with fixed-delta skew on matched expiries.

## Milestones

W1-3: validate index history and theory; W4-6: align returns and audit events; W7-9: estimate nested models; W10-12: chronological scores and robustness; W13-16: interpret and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
