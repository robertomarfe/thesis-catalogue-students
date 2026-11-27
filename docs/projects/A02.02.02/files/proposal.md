---
title: "Financial Conditions and Time-Varying Expected Equity Returns"
subtitle: "Research proposal | A02.02.02"
---

**Asset pricing · Predictability and machine learning · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Financial-conditions indices aggregate many signals and may describe risk-bearing capacity. But revisions and asynchronous release dates can manufacture apparent predictive content. The empirical contribution is a transparent availability-aware comparison, not a causal claim about monetary policy.

## Research question

Do financial-conditions indices provide incremental out-of-sample information about aggregate equity excess returns beyond standard valuation predictors?

## Economic mechanism

The Euler restriction $E_t[m_{t+1}r^e_{t+1}]=0$ permits time-varying expected excess returns through conditional covariance with the SDF.

## Research design

Use Goyal and weekly NFCI, train through 1999, validate 2000–2009 and test 2010–2025. Keep actual releases at each origin or lag prior-month latest revised NFCI with no forward fill beyond one month. ANFCI only robustness; FF3 optional cross-check.

Assert availability timestamp <= origin for every observation. Perturb all post-origin NFCI observations and ensure features do not change. Check holidays, missing weeks, release lag and common sample. Flag revised values.

\newpage

## Required exhibits

Timing diagram, predictor correlations, coefficient and forecast tables, cumulative squared-error difference plot and stability analysis.

## Minimum viable thesis

NFCI and valuation predictors, historical mean benchmark, one chronological forecast test, timing audit, coefficient uncertainty and sensitivity to lags. Null results acceptable.

## Scope and feasibility

Current revised NFCI histories are pseudo-real-time, not authentic vintages; seek ALFRED vintages for extension. Do not use future index revisions or test-set selection to claim tradability. Limit multiple predictors and distinguish aggregate forecasting from BAB funding mechanism.

**Prerequisites:** Asset pricing, predictive regressions, HAC, Python.

**Optional extension:** Use historical vintages and compare NFCI with GZ excess bond premium under a precommitted model set.

## Milestones

W1-3: theory and vintage audit; W4-6: construct monthly data; W7-9: regressions; W10-12: forecasts and uncertainty; W13-16: robustness and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
