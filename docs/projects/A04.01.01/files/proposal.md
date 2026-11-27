---
title: "Expected Economic Growth and the Dynamics of Equity Risk Premia"
subtitle: "Research proposal | A04.01.01"
---

**Asset pricing · Macro-finance and policy risk · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Survey forecasts separate expected output growth from realized economic news. Their incremental predictive content tests conditional expected returns, not whether growth shocks cause equity returns.

## Research question

Do published US real GDP growth forecasts predict future equity excess returns beyond valuation ratios, and does incremental predictive performance survive chronological evaluation?

## Economic mechanism

For survey vintage $q$, define expected growth from mean real GDP levels $EG_q=100[(F_qY_{q+1}/F_qY_q)^4-1]$.

## Research design

GDP-only SPF from 1992; 1992–2007 training and 2008–2025 target test, release-month origins, prior-month valuation ratio, 3-month relative log return and 12-month sensitivity.

Create an origin/release/target-end ledger; reconstruct first three forecasts from the actual workbook, and verify mature training targets at each decision. Compare EG, dp and both on identical origins with a mature historical mean; report effective sample, overlapping h=12 sensitivity, paired loss intervals and pseudo-real-time limitation.

\newpage

## Required exhibits

Vintage alignment ledger, forecast and return plots, regression and OOS loss tables, sensitivity to growth horizon and release lag, complete merge diagnostics.

## Minimum viable thesis

One consistent SPF real-growth forecast measure, release-timed 3-month target, EG/dp regression comparison and historical-mean out-of-sample benchmark, with uncertainty.

## Scope and feasibility

Use actual release dates rather than assigning forecasts to quarter starts; compare lagged forecast-only specifications if vintage valuation inputs unavailable. Revised dp means pseudo-real-time, not strict real-time. Survey levels are expectations, not realizations. Small quarterly samples and nested forecast models require caution; block bootstrap or appropriate adjusted loss test.

**Prerequisites:** Asset pricing, forecasting regressions, date handling and Python pandas/statsmodels.

**Optional extension:** Study survey forecast dispersion or forecast revisions as a separate predictor with a predeclared design.

## Milestones

W1-3: pricing and survey documentation; W4-6: vintage merge; W7-9: baseline regressions; W10-12: chronological forecasts; W13-16: sensitivity and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
