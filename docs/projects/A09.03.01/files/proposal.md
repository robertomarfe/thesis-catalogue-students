---
title: "Value and Momentum Everywhere: Common Risk or Diversification?"
subtitle: "Research proposal | A09.03.01"
---

**Asset pricing · International finance, FX and commodities · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Value and momentum appear in several asset classes, but published factor portfolios may share common risks despite different underlying assets. The original paper's factor data allow a focused study of dependence and diversification without pretending to reconstruct security-level positions.

## Research question

How much of cross-asset value and momentum variation is explained by common style factors, and does combining the two styles reduce portfolio risk beyond diversification within either style alone?

## Economic mechanism

For style sleeves $f_t$ and a training covariance $\Sigma$, the variance of a fixed composite is $w^\top\Sigma w$.

## Research design

Verify the original AQR workbook and form a common panel of at least three genuinely distinct asset classes with both styles. Freeze the first 60% of common dates for training. Compare within-style and cross-style dependence, train-only PCA and fixed or prespecified scaled portfolios on the holdout.

Inspect workbook tabs and exact periods; preserve common dates and no imputation. Fit all scales/loadings on training. Report sleeves, overlap, risk normalization and holdout uncertainty.

\newpage

## Required exhibits

Data coverage matrix, correlation heatmaps by style, PCA loadings and OOS variance share, portfolio risk/Sharpe table, cumulative research-factor P&L and covariance attribution. No compounded wealth for zero-cost spreads without a specified capital account.

## Minimum viable thesis

Verified original AQR factor workbook, at least three asset classes and both styles, matched sample, correlation/PCA and portfolio diversification exercise with frozen OOS protocol; robust interpretation of risk scaling and limited replication.

## Scope and feasibility

Avoid including a global aggregate as both component and benchmark. Use leave-one-class-out factors to avoid mechanical self-spanning; compare different covariance windows and scale choices. Report dated sample and no claim of current performance. Correlation/PCA is not causal or proof of priced risk; provider returns may not include all implementation costs.

**Prerequisites:** Factor investing, covariance matrices, PCA, portfolio mathematics and Python.

**Optional extension:** Use separately verified updated AQR multi-asset datasets for temporal extension; harmonize style definitions rather than splice incompatible series.

## Milestones

W1-3: literature and workbook gate; W4-6: clean factor matrix and reproduce descriptive statistics; W7-10: PCA and portfolio tests; W11-13: leave-one-out and uncertainty; W14-16: write and document.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
