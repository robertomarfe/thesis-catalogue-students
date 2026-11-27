---
title: "Forward Rates and Time-Varying Bond Risk Premia"
subtitle: "Research proposal | A05.03.02"
---

**Asset pricing · Fixed income and interest rates · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

If expected bond returns share a common factor, a single combination of forward rates may summarize predictive variation across maturities. The project tests that parsimonious restriction and its stability; a tent-shaped coefficient profile is an empirical hypothesis, not a constraint.

## Research question

Does a training-estimated Cochrane-Piazzesi-style common forward factor improve multi-maturity bond risk-premium forecasts, and are its weights and predictive gains stable across time?

## Economic mechanism

Fit $\overline{rx}_{t+12}=a+b^\top f_t+\epsilon_{t+12}$ in training, then use the fitted common factor in maturity-specific regressions.

## Research design

Construct common 1--5 year GSW yields and aged annual excess returns. Estimate weights only on matured 1972--1999 labels subject to actual coverage, freeze them for the fixed holdout, and separately evaluate a predetermined expanding refit. Compare historical mean, slope, PCs and ridge forecasts.

Do not infer a structural factor from a good in-sample fit. Report fixed and expanding results separately, with actual eligible label counts and stability intervals.

\newpage

## Required exhibits

Forward-weight plot, maturity/regime loss table, forecast paths, overlap audit and robustness.

## Minimum viable thesis

One common factor, four maturities, historical-mean and slope benchmarks, fixed holdout and overlap-aware inference.

## Scope and feasibility

Fitted yields and overlapping returns imply measurement and inference caveats. No causal claim or real-time vintage guarantee. Distinct from A05.03.01: focus on common cross-maturity factor, weight stability and transfer rather than general forward predictability.

**Prerequisites:** Fixed income, time-series regression, Python.

**Optional extension:** Compare survey rate expectations or add higher maturities using fixed factor learned on 2-5y only.

## Milestones

W1-3: curves and formulas; W4-6: factor fit; W7-9: frozen/expanding evaluation; W10-12: regimes and inference; W13-16: writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
