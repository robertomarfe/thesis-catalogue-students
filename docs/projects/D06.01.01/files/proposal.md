---
title: "Asian Option Pricing and the Value of Averaging"
subtitle: "Research proposal | D06.01.01"
---

**Derivatives · Numerical pricing and exotics · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Averaging reduces exposure to any single observation, but moving the averaging dates also changes expected levels when carry is nonzero. This project separates monitoring frequency from averaging window and asks how both price and hedge sensitivities differ from terminal exposure.

## Research question

How do the averaging window, monitoring frequency and volatility affect arithmetic and geometric Asian call prices and their hedge sensitivities relative to a European option?

## Economic mechanism

For $m$ future fixings, $A=m^{-1}\sum_j S_{t_j}$ and $G=\exp(m^{-1}\sum_j\log S_{t_j})$. Although $A\ge G$ pathwise, neither has a universal call-price ranking relative to a European option.

## Research design

Compare full-year and final-quarter schedules at 4, 12 and 52 fixings, holding payment date fixed. Use the prescribed strikes and volatilities, analytic geometric and independent arithmetic references, and paired delta/vega bumps.

Change frequency and window separately. Use union-grid draws where practical because grids are not nested. Preserve payment time; do not call a finite fixing grid a continuous average.

\newpage

## Required exhibits

Analytical derivation, verification and confidence interval table, price/Greek panels and averaging-window comparison, documented payoff and fixing schedules.

## Minimum viable thesis

Validated geometric and arithmetic pricing, two windows and at least three fixing frequencies, delta and vega analysis, interpretation of averaging versus terminal exposure.

## Scope and feasibility

Use exact time conventions, same maturity and payoff units; note that changing averaging dates changes expected level at nonzero carry. Distinguish price sensitivity at initiation from after some fixings are observed. Avoid calling discrete results continuous-limit values without a convergence test.

**Prerequisites:** Lognormal distributions, BSM, Monte Carlo and Python. No external data required.

**Optional extension:** Analyze pricing after partial fixing or introduce a floating strike; do not duplicate D05.01.02's algorithm ranking.

## Milestones

W1-3: derive geometric price; W4-6: code and validate MC; W7-10: monitoring and window experiments; W11-13: Greek analysis; W14-16: robustness and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
