---
title: "Inflation Risk and the Cross-Section of Equity Returns"
subtitle: "Research proposal | A04.02.01"
---

**Asset pricing · Macro-finance and policy risk · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Inflation changes purchasing power and may also be associated with cash-flow or discount-rate news. Comparing nominal and real exposures with a market control separates accounting from descriptive cross-sectional differences.

## Research question

Which industry and characteristic portfolios have the strongest nominal and real return exposure to unexpected CPI inflation, and is the cross-sectional relation between inflation beta and average excess return robust to market beta?

## Economic mechanism

With quarterly average CPI $I_q$, let $\pi_q=I_q/I_{q-1}-1$ and $\widehat\pi_q=(1+f_{q-1}/100)^{1/4}-1$. The surprise is $u_q=\pi_q-\widehat\pi_q$.

## Research design

Quarterly-average SA CPI and preceding SPF vintage; separately compounded industry, characteristic, market and bill returns; 1985–2025 target, fixed pre/post-2000 split, joint inference.

Hand-check one quarterly-average CPI realization and one forecast error from the prior vintage; compound market, portfolio and bill legs separately. Estimate nominal and real exposures on matched quarters and jointly bootstrap quarters, re-estimating both stages. Report common sample, rank, regime split and revised-CPI caveat.

\newpage

## Required exhibits

Matched forecast/realization panel, innovation figure, portfolio beta and hedge tables, cross-sectional scatterplot and joint intervals, regime diagnostics.

## Minimum viable thesis

One coherent quarterly CPI innovation measure, industry portfolio exposures with market control, nominal/real distinction, joint inference and regime robustness.

## Scope and feasibility

Match CPI quarterly-average versus end-quarter and annualized-rate convention exactly; do not replace forecast errors with raw inflation. Revised realized CPI is retrospective; actual release dates define expectation timing. Portfolio exposures are not causal or a proof of priced inflation risk. Avoid independent-asset standard errors for correlated portfolio returns.

**Prerequisites:** Asset pricing, macroeconomic data, regression, time-series inference and Python.

**Optional extension:** Compare expected inflation and surprise effects separately or use PCE forecasts with matched realized PCE definition.

## Milestones

W1-3: inflation and risk pricing theory; W4-6: survey/CPI timing and quarterly returns; W7-9: exposure estimates; W10-12: cross-section and regimes; W13-16: inference and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
