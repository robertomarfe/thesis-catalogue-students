---
title: "Volatility Targeting in Equity Portfolio Management"
subtitle: "Research proposal | A08.03.02"
---

**Asset pricing · Portfolio choice, behavioral finance and market frictions · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Volatility targeting adjusts market exposure using estimated risk. Its value depends on cash financing, lagged information, trading costs and ex-ante benchmark matching.

## Research question

Does past-only volatility targeting improve risk-adjusted performance and drawdowns versus static equity allocations after matching ex-ante risk and charging realistic costs?

## Economic mechanism

At month end $w_t=\min(c,\sigma^*/\widehat\sigma_t)$. Next-month gross wealth before spread and cost is $w_tR_m+(1-w_t)R_f$.

## Research design

French daily/monthly market and RF, 21/63/252 days, 10/15% targets and 1/1.5/2 caps, fixed costs/spreads; 1990–2004 training, 2005–25 test.

Check target/cap and funding ledger against two hand-computed periods; keep realized equity and cash returns separately, lag volatility at month end, disclose haircut cost approximation and insolvencies. Predeclare static matched-risk rule and borrowing spread; report turnover, downside, CE and paired test uncertainty.

\newpage

## Required exhibits

Weight and forecast volatility time series; realized volatility/target plot; wealth and drawdown; leverage/cost/performance table; paired uncertainty.

## Minimum viable thesis

Market and cash, one target and two caps, fixed equity/cash benchmark, past-only weights and cost-aware evaluation. Distinct from risk parity across multiple assets.

## Scope and feasibility

No use of month t+1 information for w_t; do not set target scale using full test sample. Excess returns may not include cash financing at investor rates; make assumptions explicit. Leverage caps and drawdown paths matter. Index-based synthetic portfolios not executed trades.

**Prerequisites:** Portfolio theory, volatility estimation, Python and backtest discipline.

**Optional extension:** Compare conditional mean forecasts or apply to FF factors with explicit notional/margin conventions.

## Milestones

W1-3: theory/data checks; W4-6: ledger and forecasts; W7-9: baseline; W10-12: stress and costs; W13-16: reproduce/write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
