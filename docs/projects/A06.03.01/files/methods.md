---
title: "Focused methods — Equity Yield Slopes and the Sensitivity of Equity Portfolios to Interest Rates"
subtitle: "A06.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

Let $s_{i,t-1}=e_{i,t-1}(10)-e_{i,t-1}(1)$ and $\widetilde s_{i,t-1}$ be its within-date centered value.

Use asset and date effects in the primary regression, a slope main effect, and $\widetilde s_{i,t-1}\Delta b_t(10)$ as the differential rate-exposure regressor. Include relative portfolio market loadings; common market and rate main effects are collinear with date effects. Check design rank; the pooled asset-FE model without date effects is a secondary diagnostic. A coefficient times .01 gives the interaction sensitivity per 100bp times the slope difference in decimal units. Full-sample generated GKK yields prevent live forecasting claims.

## Research checks

Prespecify pooled asset-FE diagnostic separately from primary time-FE specification. In latter omit common dy and market main effects, interact market with portfolio indicators as appropriate, center lagged slopes within date and check rank; include slope main effect, joint month block inference and exact t-1 availability. Require >=4 exactly mapped styles and scale effects per 100bp. Do not silently treat helper output as the primary panel test.
