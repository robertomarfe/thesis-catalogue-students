---
title: "Currency Hedging of US Equity Investments for Euro-Area Investors"
subtitle: "Research proposal | D10.03.02"
---

**Derivatives · International finance, FX and commodities · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

A euro investor holding US equities is exposed both to equity performance and to movements in the euro-dollar exchange rate. A principal hedge does not automatically remove FX exposure from subsequent equity gains, and the optimal hedge depends on covariance and financing carry.

## Research question

When does a quarterly synthetic currency hedge improve the risk-return profile of a euro investor holding US equities? How do hedge ratio, equity-FX covariance and financing carry affect the result?

## Economic mechanism

With $S$ in USD/EUR, unhedged EUR return is $U=(1+R_{US})S_0/S_1-1$.

## Research design

Construct nonoverlapping quarterly US total returns, matched endpoint spot and lagged rate proxies under the prescribed timing. Form forward P&L for fixed ratios 0, 0.5 and 1 and a past-only expanding or rolling benchmark. Evaluate common post-training quarters with costs and hypothetical basis sensitivity.

Audit USD/EUR sign, full-principal identity, common dates, lagged rates and no look-ahead. Retain 60 aligned-quarter target; if unavailable agree a descriptive fixed-ratio scope. No ex-post optimized benchmark.

\newpage

## Required exhibits

Wealth paths, hedge ratio and FX/equity covariance charts, risk-return/ES table, realized carry attribution, cost/basis sensitivity and sample audit. Use same initial capital and quarter boundaries for all portfolios.

## Minimum viable thesis

At least 60 aligned quarters if available, correctly signed forward P&L, fixed hedge ratios and an expanding benchmark, risk/return comparisons and transparent basis/cost scenarios. If data insufficient, fixed-ratio descriptive exercise with no dynamic forecast claim.

## Scope and feasibility

Do not use monthly 3m forward rolls as nonoverlapping contracts. No compounding of market excess return without RF. Report portfolio-research series and proxy rates, not executable currency hedge performance. Separate risk reduction from return enhancement; use paired block bootstrap for volatility differences, no optimized full-sample ratio in OOS comparison.

**Prerequisites:** Portfolio variance, FX forwards, return compounding, basic time-series econometrics and Python.

**Optional extension:** Compare regional stock portfolios, or model rolling monthly actual 1m hedge only with verified tenor-matched daily rates and forward data.

## Milestones

W1-3: theory and data gate; W4-6: align quarterly total returns and verify P&L; W7-10: portfolio and OOS hedge ratios; W11-13: costs, regimes and uncertainty; W14-16: write and reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
