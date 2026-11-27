---
title: "The Term Structure of Equity Yields: Evidence from Synthetic Dividend Strips"
subtitle: "Research proposal | A06.02.01"
---

**Asset pricing · Consumption-based asset pricing and equity term structures · Level 2/3**

**Data:** Empirical design conditional on actual access and coverage. **Status:** current review draft; supervisor approval pending.

## Motivation

The maturity profile of equity valuation reveals whether short and distant dividends are discounted differently. Synthetic strip estimates extend the horizon coverage, but their common estimation model constrains interpretation.

## Research question

What are the main level, slope and curvature patterns of US aggregate equity yields, and how do they differ in recessions versus expansions? Does subtracting nominal bond yields change the economic interpretation of the slope?

## Economic mechanism

For positive dividend normalization $D_t$, let $P_t^{(n)}$ price the dividend at maturity $n$. Define $e_t(n)=-n^{-1}\log(P_t^{(n)}/D_t)$.

## Research design

Verify GKK archive and Eq.32/33, full aggregate 1–15 grid with matched GSW nominal zero yields and ex post recession episodes; conditional data access.

Verify archive/version and Eq.32/33, complete 1-15 annual maturity grid, positive dividend normalization and decimals, exact common month-end GSW SVENY, not par yields. Report common sample, model-implied caveat, slope and fixed curvature definition, centered PCA with sign convention and recession episode counts. Inference conditional on estimated curves; no independent validation of the underlying GKK estimator.

\newpage

## Required exhibits

Maturity moment table; yield and forward-yield curve plots; slope time series with recession shading; factor-loading and variance-explained chart; conditional means and confidence intervals. Clearly label every series 'model-implied' and explain expected cash-flow growth versus discount-rate variation.

## Minimum viable thesis

Verified GKK aggregate file, maturity profiles, slope/PCA analysis and matched bond and recession comparison; no replication of GKK estimation required. If unavailable, pause or redesign as an explicitly synthetic model exercise, not as observed-market evidence.

## Scope and feasibility

Use alternative slope 10Y-1Y, curvature at a different middle maturity, and pre/post-2004 sample comparison if supported. Check yield definitions and compounding before subtracting bond yields. Inference conditional on estimated GKK inputs does not include first-stage model estimation uncertainty. PCA uses full sample for description only, not OOS claims.

**Prerequisites:** Asset pricing SDF, bond yields, time-series statistics and PCA, Python. No licensed dividend strip data or full affine estimation required.

**Optional extension:** Compare a small prespecified selection of GKK characteristic portfolios with positive dividends, or relate slopes to lagged macro forecasts; avoid a full 102-portfolio search without multiplicity control.

## Milestones

W1-3: read GKK theory/definitions and verify download; W4-6: align yields, bonds and recession dates; W7-10: moments, PCA and forward curves; W11-13: conditional comparisons and episode sensitivity; W14-16: write and archive code/data provenance.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
