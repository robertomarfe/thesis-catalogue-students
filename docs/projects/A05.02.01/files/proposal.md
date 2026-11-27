---
title: "Modeling and Forecasting the Yield Curve with the Dynamic Nelson-Siegel Model"
subtitle: "Research proposal | A05.02.01"
---

**Asset pricing · Fixed income and interest rates · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

A yield curve evolves through persistent changes in level, slope and curvature. Dynamic Nelson-Siegel summarizes that shape in a small factor vector. The test is whether forecasting these factors adds information relative to the current observed yield at the same maturity.

## Research question

Does dynamic Nelson-Siegel improve monthly nominal zero-yield forecasts at 1, 3 and 12 months relative to a no-change forecast, and at which maturities and horizons does it help?

## Economic mechanism

Set $z=\lambda\tau$, $\ell(z)=(1-e^{-z})/z$. Then $y_t(\tau)=L_t+S_t\ell(z)+C_t[\ell(z)-e^{-z}]$.

## Research design

Construct the prescribed monthly GSW zero-yield panel. Fix baseline decay in inverse years and estimate cross-sectional factors; forecast them using training-only AR dynamics at 1, 3 and 12 months. Compare no-change on identical dates and maturities, with any alternative decay selected before final evaluation.

Freeze decay or select it only on training data. A negative OOS result is informative. Do not describe a fitted DNS model as automatically arbitrage-free or an implementable trading rule.

\newpage

## Required exhibits

Average curve and factor loading figure; factor and residual diagnostics; RMSE/MAE heatmap by maturity/horizon; comparative forecast plots and loss-difference intervals; prespecified sample sensitivity table. Separate curve fit quality from dynamic forecast performance.

## Minimum viable thesis

One consistent monthly zero-yield panel, fixed-lambda DNS, AR factors, no-change benchmark, common-sample 1/3/12-month forecast table with uncertainty and interpretation. DNS need not outperform.

## Scope and feasibility

No lambda or VAR lag selection using OOS scores; all models receive identical information sets. Compare rolling window and ECB zero curves only if conventions are aligned. Acknowledge GSW revisions and fitted-curve structure; do not claim exact real-time forecasting on revised histories.

**Prerequisites:** Fixed income, linear regression, AR/VAR basics, time-series validation, Python. No bond transaction database required.

**Optional extension:** Compare VAR factors, an arbitrage-free Nelson-Siegel formulation or portfolio duration-risk forecast implications; avoid expanding to return predictability before baseline passes.

## Milestones

W1-3: derive loadings and acquire GSW; W4-6: clean monthly curves and validate fits; W7-10: implement recursive forecasts and benchmarks; W11-13: evaluate loss differences and stability; W14-16: write and reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
