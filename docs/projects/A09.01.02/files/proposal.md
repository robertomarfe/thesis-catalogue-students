---
title: "International Diversification and Time-Varying Market Integration"
subtitle: "Research proposal | A09.01.02"
---

**Asset pricing · International finance, FX and commodities · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

International equity diversification can weaken precisely when global volatility rises. Separate changes in realized co-movement from changes in portfolio risk and from stronger claims about integration of financial markets.

## Research question

How have correlations, common-factor exposures and the realized diversification benefits of nonoverlapping developed equity regions changed over time and across volatility regimes?

## Economic mechanism

For four disjoint regions and fixed weights $w$, $\operatorname{Var}(w^\top R_t)=w^\top\Sigma w$.

## Research design

Use the four prescribed nonoverlapping developed regions and the Developed factor series as an external reference, not a fifth holding. Reconstruct USD total returns, use trailing 60-month windows and compare monthly rebalanced equal weights with individual regions. Freeze a high-volatility threshold in training.

Verify the four disjoint constituents and common USD RF. Exclude the overlapping Developed index from portfolio holdings. Record the rolling/regime timing, variance decomposition and sample dependence.

\newpage

## Required exhibits

Regional data dictionary, rolling correlation and beta plots, PCA diagnostics, diversification and regime tables with uncertainty and portfolio accounting.

## Minimum viable thesis

Four disjoint regions, common monthly sample, rolling comovement measures, equal-weight diversification benchmark and regime comparison.

## Scope and feasibility

Global index overlaps regional assets; leave-one-out benchmark is an equal-weight proxy, not a market-cap global index. USD returns mix currency and local equity risk. Do not equate correlation with market integration, or include overlapping Developed alongside its regions in the portfolio.

**Prerequisites:** Portfolio theory, factor regressions, PCA, time-series inference and Python.

**Optional extension:** Use documented local-currency or emerging-market return series to study currency contributions and developed/emerging diversification separately.

## Milestones

W1-3: diversification theory and region definitions; W4-6: panel and return construction; W7-9: rolling factor/covariance analysis; W10-12: portfolio and regime results; W13-16: robustness and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
