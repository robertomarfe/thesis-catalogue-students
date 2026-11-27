---
title: "Volatility Risk Exposure and Expected Equity Portfolio Returns"
subtitle: "Research proposal | A07.04.01"
---

**Asset pricing · Volatility forecasting and tail risk · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

A portfolio that performs poorly when aggregate volatility rises may require compensation even after its market beta is accounted for. The project estimates exposure to unexpected volatility news and tests whether that predetermined exposure is related to future portfolio returns.

## Research question

Are lagged exposures to aggregate volatility innovations associated with future average portfolio excess returns after accounting for market beta and standard factors?

## Economic mechanism

Let $z_t=\log I_t$ for VIX index level $I_t>0$ and $\eta_t=z_t-\widehat E_{t-1}[z_t]$. Use the lagged loading on $\eta_t$ in subsequent cross-sectional excess-return regressions.

## Research design

Build a recursive log-VIX innovation, estimate trailing monthly market and volatility loadings, then price them in subsequent months on a primary FF portfolio panel. Treat the industry panel as a distinct robustness set.

Check the prediction of VIX is trained strictly before the innovation date. Weak loading dispersion and generated regressors matter; report null evidence and avoid a causal interpretation of the estimated slope.

\newpage

## Required exhibits

Beta dispersion/precision plots; Fama-MacBeth price estimates; high-low portfolio return and alpha table; robustness and sample diagnostics.

## Minimum viable thesis

One French test-asset set, recursive volatility innovation, lagged betas, cross-sectional pricing test and joint uncertainty discussion.

## Scope and feasibility

Generated-regressor error, small cross section, weak beta dispersion and collinearity may prevent identification. No causal or individual-stock claim. VIX innovations include expected variance and risk-premium variation; distinguish priced risk from simple contemporaneous association.

**Prerequisites:** Factor models, rolling regressions, Fama-MacBeth, time-series inference, Python.

**Optional extension:** Use daily beta estimation aggregated monthly or compare option-based variance-risk measures after data validation.

## Milestones

W1-3: literature and data; W4-6: innovations/betas; W7-9: cross-sectional tests; W10-12: bootstrap and robustness; W13-16: thesis and code.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
