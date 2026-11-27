---
title: "Financial Stress and the Stock-Bond Correlation"
subtitle: "Research proposal | A04.04.02"
---

**Asset pricing · Macro-finance and policy risk · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Financial stress can change the joint distribution of stock and bond returns. A correlation shift alone does not establish whether a fixed allocation becomes riskier, because marginal variances also move.

## Research question

Does the stock-bond return correlation vary with prior financial stress, and does that variation change the diversification benefit of a fixed stock-bond portfolio?

## Economic mechanism

For simple holding returns and fixed stock weight $w$, portfolio variance is $w^2\sigma_S^2+(1-w)^2\sigma_B^2+2w(1-w)c_{SB}$, with conditional covariance $c_{SB}$.

## Research design

US total market (Ken French library) and GSW 5-year aging zero monthly net returns; prior released STLFSI4, fixed threshold >0, training quantile robustness; 36/60-month diagnostics, 2/10-year robustness.

Use a release ledger or explicitly pseudo-real-time extra lag; set threshold from fixed rule or past data. Compute exact aging bond return and nominal equity total return; report regime counts, marginal variances, covariance and 2*w_s*w_b*cov contribution with date-block inference and fixed-weight risk decomposition.

\newpage

## Required exhibits

Data construction audit; correlation and covariance plots; regime return/risk table; maturity and threshold robustness; diversification comparison.

## Minimum viable thesis

Monthly market and 5y synthetic zero returns, lagged stress, conditional risk and paired block inference. Distinct from macro inflation hedge A04.02.02.

## Scope and feasibility

Synthetic zero returns are not traded bond-index returns. Stress includes financial prices, so association is not causal; use lagged measures, revised-vintage caveat and fixed definitions. Avoid very small stress regimes and overlapping-window naive t-tests.

**Prerequisites:** Fixed income, covariance estimation, time-series econometrics and Python.

**Optional extension:** Inflation and policy regime interactions or bivariate DCC-GARCH, with strictly past-only forecasting.

## Milestones

W1-3: theory/source checks; W4-6: build return panel; W7-9: conditional estimates; W10-12: robustness and portfolio risk; W13-16: write/reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
