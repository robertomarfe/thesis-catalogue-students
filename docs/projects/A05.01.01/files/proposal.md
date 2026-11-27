---
title: "Gaussian and Square-Root Interest Rate Models: Theory and Empirical Performance"
subtitle: "Research proposal | A05.01.01"
---

**Asset pricing · Fixed income and interest rates · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Short-rate models differ in the support and conditional dispersion of their innovations. A square-root diffusion can accommodate state-dependent volatility, whereas a Gaussian diffusion allows negative rates. The economic question is whether the richer distribution improves predictive density on an identical observed proxy, not whether a model can price bonds after an unrelated calibration.

## Research question

Do square-root rate innovations improve the fit and predictive distribution of US short-rate proxies relative to Gaussian mean reversion?

## Economic mechanism

Under the physical measure $\mathbb P$, compare $dr=\kappa(\theta-r)dt+\sigma dW$ with $dr=\kappa(\theta-r)dt+\eta\sqrt r\,dW$.

## Research design

Use the documented DTB3 discount-basis proxy, positive-rate training and test periods, and exact transition likelihoods. Evaluate density forecasts on the same eligible observations; examine the unsupported low-rate regime separately. Illustrative pricing curves use independently specified risk-neutral parameters.

Compare held-out log scores, PIT calibration and parameter uncertainty on identical positive observations. Record optimizer failures and missing months. Distinct from A05.01.03: primary target is the whole conditional density, not conditional variance alone.

\newpage

## Required exhibits

Parameter, fit and forecast score tables, density/QQ plots, conditional variance and PIT diagnostics, simulation comparisons and illustrative affine yield curves.

## Minimum viable thesis

Two exact P transition estimators on a verified positive-rate sample, held-out density comparison, simulated rate moments and a clear P/Q distinction with illustrative curves.

## Scope and feasibility

Try alternative start dates and monthly average proxy only as robustness (not exact point observation); compare crisis regimes and discretization of monthly intervals. CIR noncentral chi-square likelihood at zero needs explicit treatment; report unsupported observations. Real bill maturities differ from instantaneous short rate; no direct estimation of market price of risk.

**Prerequisites:** Stochastic calculus, likelihood, noncentral chi-square distributions, numerical optimization and Python SciPy.

**Optional extension:** Jointly estimate risk-neutral parameters using GSW zero yields under a measurement-error specification; separate from baseline.

## Milestones

W1-3: derive transitions and bond formulas; W4-6: acquire and transform rates; W7-9: MLE and simulation; W10-12: holdout and stress analysis; W13-16: Q illustrations and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
