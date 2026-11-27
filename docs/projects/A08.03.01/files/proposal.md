---
title: "Risk Parity versus Minimum-Variance Portfolios"
subtitle: "Research proposal | A08.03.01"
---

**Asset pricing · Portfolio choice, behavioral finance and market frictions · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Risk parity allocates component risk rather than capital, potentially balancing exposures without mechanically minimizing total variance.

## Research question

Does equal risk contribution deliver more stable risk allocation than minimum variance, and at what cost in realized volatility and turnover?

## Economic mechanism

For variance $v=w^\top\Sigma w$, normalized risk contribution is $RC_i=w_i(\Sigma w)_i/v$.

## Research design

30 industries, trailing 60 months, 1990–2025 target; equal weight, inverse vol, ERC and GMV; same covariance, monthly drift and costs.

Check contribution sum, positive budget and ERC residual on diagonal and correlated SPD matrices; report KKT for GMV and eigenvalues. Compare four methods with common dates/covariance, cost drift and ex-ante contributions plus held-out realized contribution estimates and uncertainty.

\newpage

## Required exhibits

Weight/risk contribution charts, constraint and solver residuals, performance and transaction-cost tables, sensitivity plots.

## Minimum viable thesis

Four portfolios on same long-only industry sample, validated ERC and GMV, drift-corrected backtest and contribution analysis.

## Scope and feasibility

Positive definite covariance and solver accuracy checked. ERC with additional caps need not achieve exact equal risk; baseline only long-only. Industry portfolios overlap underlying economy, not distinct asset classes. Risk parity need not beat minimum variance in volatility.

**Prerequisites:** Linear algebra, convex optimization, portfolio theory, returns.

**Optional extension:** Add synthetic constant-maturity bond allocation and inflation scenarios; volatility targeting with stated leverage/funding.

## Milestones

W1-3: risk contributions; W4-6: solver/simulation; W7-9: backtest; W10-12: robustness; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
