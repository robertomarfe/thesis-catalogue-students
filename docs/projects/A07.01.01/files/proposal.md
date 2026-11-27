---
title: "The Variance Risk Premium and the Predictability of Stock Market Returns"
subtitle: "Research proposal | A07.01.01"
---

**Asset pricing · Volatility forecasting and tail risk · Level 2/3**

**Data:** Empirical design blocked pending authorized access and coverage; not assignable on this design. **Status:** current review draft; supervisor approval pending.

## Motivation

An option-implied variance measure combines expected variation and compensation for variance risk. The difference between risk-neutral and physical forecasts may contain information about expected equity returns. The study must distinguish genuine ex ante variation from a difference constructed using future realized variance.

## Research question

Does an ex ante 30-day variance risk premium proxy help forecast US equity excess returns over 1 and 3 months relative to a historical mean, and how sensitive is the result to the physical variance forecast and sample coverage?

## Economic mechanism

Use the positive convention $VRP_{t,30}=Q_{t,30}-P_{t,30}$, with both legs in 30-calendar-day integrated decimal variance units and $Q_{t,30}\simeq (I_t/100)^2(30/365)$.

## Research design

Construct the matched-SPX variance leg only with authorized price history and adequate coverage. Forecast one- and three-month FF market-minus-bill returns chronologically, and keep the longer broad-market variance proxy as a separately labeled sensitivity, not a replacement.

The matched SPX source remains blocked until rights and actual coverage are confirmed. Short samples may support descriptive results only; long-proxy OOS analysis requires explicit supervisor agreement. No silent source substitution or claim of an intraday replication.

\newpage

## Required exhibits

Variance-leg and VRP time series; descriptive/correlation table; predictive regression and confidence intervals; chronological OOS loss comparison; short matched-SPX versus longer proxy-sample sensitivity. Discuss limitations relative to Bollerslev et al.'s intraday measure rather than claiming exact replication.

## Minimum viable thesis

Reproducible ex ante VRP construction, explicit units/underlying distinction, 1- and 3-month predictive regressions and at least one chronological OOS comparison where sample permits. Null or unstable results are acceptable; no intraday or option-chain subscription required.

## Scope and feasibility

Compare 21 trading-day fixed horizon approximation with calendar-matched baseline, alternative P forecasts, and SPX vs FF variance proxies. Keep forecast tuning inside training and avoid choosing horizons after seeing significance. If matched sample is too short, restrict baseline to descriptive/in-sample results and use longer labeled proxy for OOS; document this before assignment. Check end-of-day alignment and exchange holidays.

**Prerequisites:** Risk-neutral pricing, return and volatility measurement, predictive regressions, time-series forecasting, Python. Short historical coverage is a key supervision checkpoint.

**Optional extension:** Add Goyal valuation predictors or compare VIX to realized variance separately; if reliable intraday data become available, construct a higher-quality RV proxy without changing baseline claims retroactively.

## Milestones

W1-3: study VIX/VRP theory and verify downloads; W4-6: align dates and test physical forecast; W7-10: freeze VRP, regressions and OOS design; W11-13: compare samples, horizon and forecast sensitivity; W14-16: write and reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
