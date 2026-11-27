---
title: "Economic Policy Uncertainty and Equity Market Risk"
subtitle: "Research proposal | A04.04.01"
---

**Asset pricing · Macro-finance and policy risk · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

News-based economic policy uncertainty may predict future risk beyond persistence and option prices. The question is incremental information under realistic publication timing, not whether uncertainty structurally causes volatility.

## Research question

Does economic policy uncertainty improve forecasts of future equity market variance beyond lagged variance and VIX?

## Economic mechanism

For daily log market returns in month $t+1$, use $V_{t+1}=\sum_{d\in t+1}r_d^2$. A VIX reading $v_t$ in index points yields proxy $(v_t/100)^2/12$.

## Research design

US daily total market (Ken French library) returns, VIX last common session, lagged news EPU; train through 2004, validation 2005–09, test 2010–25; common positive rows and paired losses.

Freeze lag and return-calendar coverage; use only published EPU and VIX at origin, report conservative extra-lag sensitivity. Match forecast horizon, positive variance units and common origins; train smearing only on mature outcomes; compare paired QLIKE/MSE and crisis sensitivity, no causal claim.

\newpage

## Required exhibits

Data lineage, uncertainty and variance plots, coefficient tables, OOS score and cumulative loss plots, stability checks.

## Minimum viable thesis

Common data sample, news EPU nested forecasting test, VIX/lagged variance benchmark, QLIKE and timing sensitivity. Distinct from A10.04.01's model-interpretability question.

## Scope and feasibility

News-based EPU and composite EPU differ; do not mislabel composite as purely news. EPU may be revised and reconstructed before publication; label pseudo-OOS. Neither predictor importance nor lagged correlation identifies policy shocks. Copyright/citation conditions require review before redistribution.

**Prerequisites:** Volatility proxies, predictive regression, forecast evaluation, Python.

**Optional extension:** Evaluate ALFRED vintage availability or sector-specific uncertainty indices with predeclared multiple-test control.

## Milestones

W1-3: theory and data definitions; W4-6: merge and timing; W7-9: nested forecasts; W10-12: scores and sensitivity; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
