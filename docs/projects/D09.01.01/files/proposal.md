---
title: "The Merton Model and the Economics of Corporate Default"
subtitle: "Research proposal | D09.01.01"
---

**Derivatives · Credit risk and incomplete markets · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Leverage gives creditors a nonlinear claim on firm assets. The same probability of default need not imply the same borrowing cost, because severity and the price of risk enter debt valuation. Study these distinctions in a transparent terminal-default economy before introducing contractual complexity.

## Research question

How do leverage, asset volatility and debt maturity jointly determine physical default probabilities, risk-neutral debt values and equity leverage? When do default probability and credit spread move differently?

## Economic mechanism

Equity and debt pay $E_T=(V_T-F)^+$ and $B_T=\min(V_T,F)$, respectively; $s=-T^{-1}\log(B_0/F)-r$.

## Research design

Use the prescribed leverage, volatility and maturity grid with separate physical and pricing drifts. Compare analytical equity and debt values to independent simulations, and construct approximately equal physical-PD cases before comparing spreads.

Verify asset-value conservation, the upper bound on debt and probability intervals. Report simulation uncertainty in rare-default cases and physical-drift sensitivity separately from risk-neutral pricing. Keep all other parameters fixed in each comparative static.

\newpage

## Required exhibits

Credit spread and default-probability heatmaps; term structure plots by leverage; equity volatility table; analytical versus simulation check with confidence intervals; matched-PD comparison. Interpret deviations between risk-neutral and physical measures.

## Minimum viable thesis

Correct structural formulas and independent verification, comparative statics on leverage and volatility at several maturities, distinction between P and Q, and quantitative implications. No empirical validation claim is necessary.

## Scope and feasibility

Check equity plus debt equals firm assets and debt price <= risk-free promised payoff, default probability in [0,1], monotonicities for fixed remaining parameters. Vary physical drift separately from pricing inputs; it should change PD_P but not Q debt price in the specified model. Do not calibrate historical PDs from spreads without assumptions on risk premia.

**Prerequisites:** BSM option pricing, probability measures, comparative statics, Python. Elementary corporate finance and credit spread interpretation.

**Optional extension:** Compare first-passage default or introduce a small illustrative set of public firm filings, only after checking debt maturity, market capitalization and data consistency. Treat calibration of V and sigma_V from equity as optional and model-dependent.

## Milestones

W1-3: derive contingent-claim valuation; W4-6: implement analytic functions and MC validation; W7-10: grid, matched-PD and maturity analyses; W11-13: limiting cases and robustness; W14-16: write and reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
