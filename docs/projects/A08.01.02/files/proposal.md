---
title: "Covariance Shrinkage and Portfolio Performance"
subtitle: "Research proposal | A08.01.02"
---

**Asset pricing · Portfolio choice, behavioral finance and market frictions · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

GMV avoids noisy means but can still amplify covariance noise. Shrinkage trades bias for stability and should be judged on subsequent returns.

## Research question

Does Ledoit-Wolf covariance shrinkage improve out-of-sample global minimum-variance portfolio risk and turnover relative to sample covariance and equal weighting, and how does performance depend on estimation-window length?

## Economic mechanism

For sample covariance $S$, shrink toward scaled identity: $\widehat\Sigma=(1-a)S+a\operatorname{tr}(S)I/N$.

## Research design

French 30 industries value-weighted, fixed universe, 60/120-month lookbacks and common start after 120 months; sample and shrinkage GMV, equal weights.

Document shrinkage target, intensity and denominator; compare eigenvalues, condition numbers, KKT, weights and predicted risk on common origins. Same costs and drift, equal weight and sample GMV; report singular windows and predefined fallback, compare paired net OOS variance/turnover and block intervals.

\newpage

## Required exhibits

Rolling condition numbers and shrinkage intensity; weight-concentration chart; cumulative net wealth, drawdown and volatility plots; risk/turnover/Sharpe table with bootstrap differences; cost and lookback sensitivity. Explain why equal weighting is a demanding benchmark and not a straw man.

## Minimum viable thesis

Long-only GMV using sample and Ledoit-Wolf covariance plus equal weight, chronological backtest, two lookbacks, risk and turnover metrics, and a cost sensitivity table. Weak shrinkage gains remain a valid result.

## Scope and feasibility

Do not invert singular covariance silently: solve constrained QP, document numerical ridge only as separate benchmark. Keep identical asset universe, constraints and OOS sample; include initial allocation costs consistently or state exclusion. Do not use future returns in covariance estimates or choose cost rate by performance. Industry portfolios are published research portfolios, not directly tradable funds; backtest ignores implementation frictions beyond stylized costs.

**Prerequisites:** Matrix algebra, covariance estimation, optimization, portfolio return arithmetic, Python/SciPy/scikit-learn. No stock-level histories needed.

**Optional extension:** Compare alternative shrinkage targets or exponentially weighted covariance, or use a small verified ETF universe with explicit data availability; no need to estimate expected returns.

## Milestones

W1-3: derive GMV and shrinkage, download industries; W4-6: validate data and QP/backtest accounting; W7-10: run rolling comparison with frozen choices; W11-13: bootstrap risk, costs and concentration; W14-16: write and reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
