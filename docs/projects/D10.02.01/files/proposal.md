---
title: "Commodity Price Risk and the Minimum-Variance Hedge Ratio"
subtitle: "Research proposal | D10.02.01"
---

**Derivatives · International finance, FX and commodities · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

WTI and Brent price changes often co-move, but regional supply and delivery conditions can create substantial basis risk. A statistical Brent spot proxy may reduce WTI exposure; it is not a claim about a self-financing futures hedge.

## Research question

How much does a Brent spot-proxy hedge reduce WTI price risk, and how stable is the estimated minimum-variance hedge ratio across horizons and market regimes?

## Economic mechanism

For a long WTI exposure and a short Brent proxy, $\Delta V=\Delta S_W-h\Delta S_B$ in USD per barrel.

## Research design

Align the specified daily WTI and Brent spot prices on valid common endpoints. Form nonoverlapping weekly and monthly dollar changes; estimate rolling and expanding hedge ratios using the prescribed windows and evaluate on the fixed holdout. Compare no hedge, unit hedge and minimum-variance proxy.

Verify common observed endpoints, barrel units, no forward fill and past-only estimation at both horizons. Report basis changes, held-out risk reduction and negative results.

\newpage

## Required exhibits

Aligned price panel, basis and hedge ratio plots, in-sample versus OOS variance reduction, regime and horizon tables, discussion of physical basis and implementation gaps.

## Minimum viable thesis

Two spot series, two horizons, rolling minimum-variance and unit hedge benchmarks, honest held-out variance reduction and basis diagnostics.

## Scope and feasibility

Never treat Brent spot as a traded WTI futures contract; no roll return, margin or funding claim. Use price changes, not logs, as primary specification; handle date matching and endpoint holiday gaps explicitly. Report negative OOS hedge effectiveness if found.

**Prerequisites:** Derivatives fundamentals, covariance and regression, basic time series and Python.

**Optional extension:** If actual contract-level futures settlements become available, specify expiry, roll timing, contract size and collateral before a separate hedge evaluation.

## Milestones

W1-3: hedge theory and units; W4-6: align oil prices and construct changes; W7-9: fit rolling hedges; W10-12: holdout and regime tests; W13-16: inference, interpretation and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
