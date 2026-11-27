---
title: "Wrong-Way Risk and Credit Valuation Adjustment"
subtitle: "Research proposal | D09.04.02"
---

**Derivatives · Credit risk and incomplete markets · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Standalone exposure and default probabilities are insufficient to determine a counterparty loss when the two risks depend on one another. Isolate the contribution of a specified joint distribution at fixed marginals, rather than changing both the intensity level and dependence.

## Research question

How much can wrong-way dependence alter unilateral CVA when the standalone default probabilities and exposure dynamics are held fixed?

## Economic mechanism

A unilateral grid CVA is $(1-R)\sum_j\mathbb E^{\mathbb Q}[D(t_j)V_{t_j}^+\mathbf 1_{\{t_{j-1}<\tau\le t_j\}}]$.

## Research design

Use the current three-year forward and terminal-shock Gaussian copula, the specified hazard and correlation grids, common random draws and monthly/weekly rounding. Validate the independent grid benchmark and fixed default/exposure marginals; evaluate dependence-only changes and paired uncertainty.

Check marginal survival at all grid dates, exposure distributions, paired loss differences and grid refinement; distinguish dependence from changes in hazard or recovery. Contrast long and short forwards. A common latent horizon across maturities is a possible redesign, not part of the current frozen scope.

\newpage

## Required exhibits

Survival and EPE checks, CVA by rho in bp of notional, exposure-at-default and paired MC interval plots, grid convergence.

## Minimum viable thesis

Independent-CVA benchmark and fixed-marginal dependence sensitivity for one forward, with sign convention, marginal checks and confidence intervals.

## Scope and feasibility

Latent terminal shock construction is an ex-ante joint law, not an adapted intensity or a dynamic trading model; no claim about real counterparty correlations. Conditional exposure at default differs from EPE. No bilateral DVA, collateral or funding; use the same closeout convention.

**Prerequisites:** Risk-neutral pricing, copulas, credit risk, probability and MC.

**Optional extension:** Replace the copula with a Cox intensity driven by adapted market states, recalibrating deterministic baseline to preserve marginal survival before comparing.

## Milestones

W1-3: CVA derivation and dependence design; W4-6: analytic exposure and survival checks; W7-9: paired simulation; W10-12: grid and rare-event tests; W13-16: documentation and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
