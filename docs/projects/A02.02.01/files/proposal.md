---
title: "Interest Rates and the Predictability of Stock Market Excess Returns"
subtitle: "Research proposal | A02.02.01"
---

**Asset pricing · Predictability and machine learning · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Interest rates may proxy discount-rate variation or monetary conditions, but an in-sample association does not establish incremental forecasting value. The key comparison is against a valuation-only model using the same origins, return definition and timing.

## Research question

Do short rates and the term spread add out-of-sample information about monthly equity excess returns beyond a dividend-price benchmark and the historical mean?

## Economic mechanism

$E_t[r^e_{t+1}]=a+b\,dp_t+c\,i^{3m}_t+d\,(i^{10y}_t-i^{3m}_t)$ is a predictive specification, not a policy-shock regression.

## Research design

Use Goyal monthly excess returns, dp and FRED GS10/TB3MS, proposed 1965–2025, training through 1994 and expanding evaluation from 1995. Lag yields one month. One-month primary and matured 12-month secondary comparisons.

First three forecasts recomputed by hand; no forward fill from later observations; exact common evaluation origin list; risk-free and yield units checked separately. Negative OOS R2 retained.

\newpage

## Required exhibits

Timed data panel, predictor and regression tables, OOS forecasts and loss plots, incremental value of rates and regime sensitivity with intervals.

## Minimum viable thesis

Three prespecified predictor models and historical mean, common monthly sample and expanding forecast evaluation with uncertainty and stability checks.

## Scope and feasibility

Do not substitute yield changes for rate levels without separate specification. Do not infer causality from slope signs. Avoid future macro revisions as real-time information and incomplete overlapping labels in estimation. Distinct from A02.01.01 valuation-focused and A02.01.02 long-horizon inference-focused designs.

**Prerequisites:** Time-series econometrics, bond yields, equity risk premia and Python.

**Optional extension:** Compare nominal versus real rate proxies using appropriately dated expected inflation, or examine a fixed predeclared allocation rule.

## Milestones

W1-3: theory and predictor definitions; W4-6: panel and timing tests; W7-9: forecast implementation; W10-12: OOS and regime diagnostics; W13-16: robustness and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
