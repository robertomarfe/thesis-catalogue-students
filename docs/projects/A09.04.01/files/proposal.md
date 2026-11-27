---
title: "Time-Series Momentum across Asset Classes"
subtitle: "Research proposal | A09.04.01"
---

**Asset pricing · International finance, FX and commodities · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Trend-following strategies across asset classes can diversify equity exposure, but their published returns often already incorporate volatility scaling. Study how sleeve allocation changes realized risk and stress behavior without claiming a new futures-level replication.

## Research question

How diversified are time-series momentum payoffs across asset classes, and how do their market exposures and conditional performance vary in adverse equity market states?

## Economic mechanism

Compare a fixed four-sleeve composite $f_{p,t}=\frac14\sum_j f_{j,t}$ with lagged risk-scaled weights.

## Research design

Use the four prescribed monthly AQR time-series momentum excess-return sleeves and US FF3 benchmark. Form a common sample, compare equal weights and trailing 60-month inverse-volatility weights with stated notional conventions, and assess the fixed 2005--2025 holdout and separately labeled retrospective crisis windows.

Verify four sleeves, monthly units, risk scaling and market benchmark. Use only trailing data in weights and training thresholds, with fixed holdout. No independent futures-position replication claim.

\newpage

## Required exhibits

Factor correlation/variance tables, portfolio comparisons, conditional payoff plot, rolling beta, crisis and sensitivity analysis.

## Minimum viable thesis

Four documented monthly sleeves, common sample, diversification metrics, equal-weight vs risk-scaled comparison, market-conditional evidence and intervals.

## Scope and feasibility

Published strategies may embed leverage and hypothetical costs; no claim of implementable net performance. Do not subtract RF twice. Market-tail states are ex post descriptions. Use source methodology rather than pretending to reconstruct original contracts.

**Prerequisites:** Portfolio theory, futures fundamentals, regression and Python.

**Optional extension:** Compare with separately documented long-run trend-following series; reconstruct signals only with actual contract-level returns and roll rules.

## Milestones

W1-3: TSMOM literature and source; W4-6: panel and methodology audit; W7-9: allocation and risk analysis; W10-12: conditional/robustness tests; W13-16: write and reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
