---
title: "Forecasting the Yield Curve: Econometric Models versus Machine Learning"
subtitle: "Research proposal | A05.02.03"
---

**Asset pricing · Fixed income and interest rates · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Flexible forecasting methods may learn nonlinear relations across the yield curve, but their apparent advantage can arise from extra information or leakage. Evaluate incremental predictive value relative to strong econometric benchmarks at the same origins, maturities and horizons.

## Research question

Does machine learning improve multi-horizon US yield-curve forecasts relative to random walk, autoregressive factors and dynamic Nelson-Siegel, after honest temporal validation?

## Economic mechanism

For a common held-out loss, $R^2_{\mathrm{OOS}}=1-\sum e_{\mathrm{model}}^2/\sum e_{\mathrm{RW}}^2$.

## Research design

Use the prescribed six GSW maturities, fixed training, temporal tuning and final evaluation windows. Compare random walk, factor AR/DNS and ridge or shallow tree with predeclared lagged features. Tune separately by horizon using only matured target labels, then freeze the tuning rule.

Implement a strong DNS baseline independently before ML. Lock temporal validation and data features, log all tuning choices and missing outcomes, and never select the final model using the final test loss.

\newpage

## Required exhibits

Curve fit residual table; forecast error matrix; cumulative loss plot; tuning log; maturity/horizon robustness.

## Minimum viable thesis

GSW curve, random walk, AR/DNS and ridge or shallow tree, 1/3/12-month forecasts and locked temporal evaluation. Distinct from A05.02.01 DNS-only study.

## Scope and feasibility

No random train/test split, full-sample scaling or future factor estimation. GSW yields are fitted not transactions. Overlapping forecast errors and common shocks require time-series inference. ML complexity must be limited; record failures and null improvement.

**Prerequisites:** Fixed income, econometrics, regression/ML, Python and sklearn.

**Optional extension:** European AAA curve as external evaluation; compare forecasts of synthetic bond returns separately.

## Milestones

W1-3: theory and design; W4-6: curves and benchmarks; W7-9: ML and tuning; W10-12: locked evaluation; W13-16: documentation and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
