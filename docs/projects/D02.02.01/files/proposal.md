---
title: "SVI versus SABR: A Comparative Study of Implied Volatility Surface Fitting"
subtitle: "Research proposal | D02.02.01"
---

**Derivatives · Vanilla pricing and surfaces · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

A flexible parametric smile can interpolate liquid strikes yet behave poorly where quotes are sparse. SVI and SABR encode shape differently and can be compared under the same quote information and noise. The goal is to evaluate the fit–stability trade-off rather than claim that either raw slice parameterization produces a globally arbitrage-free surface.

## Research question

Which of raw SVI and lognormal SABR provides more stable and accurate smile estimates when quotes are sparse or noisy? Does the ranking change with maturity, asymmetry and the loss function?

## Economic mechanism

Write $k=\log(K/F)$ and $w=T I^2$ for implied total variance. Raw SVI fits $w=a+b[\rho(k-m)+\sqrt{(k-m)^2+s^2}]$; even positive fitted variance need not give convex call prices.

## Research design

Generate synthetic Heston smiles with mild and strong asymmetry at four maturities. Fit raw SVI and lognormal SABR on sparse grids with predetermined noise draws; retain interior and wing strikes as untouched tests. Compare fit in IV and price space and inspect arbitrage restrictions.

Freeze skew regimes, sparsity, noise scales and held-out wing strikes. Compare equal computational budgets and report invalid inversions, failed fits and finite-grid arbitrage rather than claiming smoothness implies absence of arbitrage.

\newpage

## Required exhibits

True versus fitted smile panels, held-out error distributions in vol points and price units, parameter stability and optimizer failure tables, butterfly/calendar diagnostic heatmaps and timing. A reproducible synthetic quote generator and frozen train/test splits.

## Minimum viable thesis

Two calibrated smile families, verified pricing reference, at least two maturities and skew regimes, sparse/noisy train versus untouched test comparisons, explicit arbitrage and failure diagnostics. No need for a globally arbitrage-free surface or live market data.

## Scope and feasibility

Use a common finite strike domain, tolerances and optimizer budget; ensure total variance positive, forward ATM limits and put-call parity. Distinguish grid-based diagnostics from global arbitrage guarantees. Include price weighting sensitivity and one alternative Heston parameter set never used for tuning. No inference about actual market fitting performance from synthetic quotes alone.

**Prerequisites:** Black pricing, stochastic calculus, numerical optimization and Python SciPy. Familiarity with Heston characteristic functions helpful; no option database required.

**Optional extension:** Implement SSVI cross-maturity constraints or repeat with a legally accessible dated option chain; state data provenance and compare with the synthetic experiment rather than conflating them.

## Milestones

W1-3: derive smile parametrizations and select scenarios; W4-6: implement and test pricing/inversion and optimizers; W7-10: run frozen calibration and held-out experiments; W11-13: robustness and diagnostics; W14-16: interpret, document and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
