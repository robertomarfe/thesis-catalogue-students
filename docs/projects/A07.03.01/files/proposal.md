---
title: "Skewness Risk and the Cross-Section of Equity Returns"
subtitle: "Research proposal | A07.03.01"
---

**Asset pricing · Volatility forecasting and tail risk · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

A linear market model ignores exposure to the square of market shocks. If marginal utility is sensitive to extreme aggregate outcomes, such nonlinear exposures may be relevant for expected returns. The empirical difficulty is estimating third-moment-related quantities reliably before observing the return to be explained.

## Research question

Do lagged market coskewness exposures have incremental explanatory power for subsequent portfolio returns beyond standard market beta and factors?

## Economic mechanism

Center market excess returns as $x=r_M^e-\bar r_M^e$ and set $z=x^2-\operatorname{Proj}_{(1,x)}x^2$. The coefficient on $z$ measures quadratic exposure orthogonal to linear market variation within the estimation window.

## Research design

Match daily and monthly portfolio definitions, estimate lagged exposures on trailing daily observations and compare monthly cross-sectional models. Retain a beta-only benchmark, predeclared scaling and a separate portfolio-sort diagnostic.

Do not remove extreme days based on their effect on significance. Verify that the daily and monthly portfolio labels match, that the market is excess return, and that generated-regressor uncertainty is recognized.

\newpage

## Required exhibits

Exposure distributions and correlations, Fama-MacBeth slopes, sorted portfolio returns, alpha and uncertainty tables, common-date robustness.

## Minimum viable thesis

One daily/monthly test-asset panel, lagged beta/coskewness estimation, monthly cross-sectional prices and beta-only comparison with robust inference.

## Scope and feasibility

Portfolio-level cross-section is small and overlapping stocks create dependence; no individual-stock pricing claim. Daily third moments noisy and driven by outliers; winsorization, if used, based on past data and clearly changes the estimand. Cross-sectional significance not proof of a structural SDF. Distinct from downside beta and option-implied skew theses.

**Prerequisites:** Factor pricing, regression, higher moments, bootstrap and Python.

**Optional extension:** Use open-source characteristic portfolios for a different cross-section or evaluate polynomial SDF distance on held-out assets.

## Milestones

W1-3: derive quadratic SDF; W4-6: prepare panels and exposures; W7-9: cross-sectional tests; W10-12: bootstrap and alternative panels; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
