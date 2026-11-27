---
title: "Historical Stress Paths and the Performance of Model-Based Option Hedges"
subtitle: "Research proposal | D04.02.02"
---

**Derivatives · Hedging and volatility derivatives · Level 2/3**

**Data:** Empirical design blocked pending authorized access and coverage; not assignable on this design. **Status:** current review draft; supervisor approval pending.

## Motivation

Observed equity stress paths provide realistic sequences of price changes even without historical option quotes. Replaying hypothetical pricing and hedging rules on these paths isolates the effect of path behavior, but does not establish the returns of a traded options strategy.

## Research question

How do BSM delta-hedging errors on observed index paths differ from errors on simulated GBM paths under the same synthetic pricing and rebalancing rules?

## Economic mechanism

Rebase observed index closes as $S_i=100I_i/I_0$; estimate inception volatility from returns preceding the window.

## Research design

Acquire authorized SP500 history, build nonoverlapping 63-session windows after the 252-day warmup, and compare fixed-inception and rolling-lagged BSM hedges with matched GBM controls. Stress labels are ex post only.

Check actual permissions, warmup and complete sessions before assignment. Report eligible windows and separate historical sampling uncertainty from simulation error. If access fails, defer or approve a retitled simulated stress study; no silent substitution.

\newpage

## Required exhibits

Historical-window audit, representative paths and hedge ledgers, residual quantiles, stress versus GBM comparison and robustness table.

## Minimum viable thesis

Observed stock-price replay plus GBM reference and two hedge rules; no historical options needed. S-class denotes synthetic option pricing, but SP500 input is required for this title. Distinct from D04.02.01's two-asset volatility hedge.

## Scope and feasibility

Price index is not a directly traded asset, dividends, financing and option prices are assumed, and no actual historical option P&L is measured. Stress classification is retrospective, not a trading signal. Small nonoverlapping sample limits tail inference; overlapping windows only as sensitivity with block resampling.

**Prerequisites:** BSM and Greeks, simulation, time-series cleaning, portfolio accounting.

**Optional extension:** Add a self-contained dividend-yield scenario or lawful historical option snapshots for separate empirical validation.

## Milestones

W1-3: derive cash ledger and validate source; W4-6: GBM checks and windows; W7-9: replay and comparison; W10-12: stress/cost robustness; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
