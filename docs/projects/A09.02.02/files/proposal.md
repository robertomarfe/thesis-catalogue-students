---
title: "Currency Carry Returns and Global Risk States"
subtitle: "Research proposal | A09.02.02"
---

**Asset pricing · International finance, FX and commodities · Level 2/3**

**Data:** Empirical design conditional on actual access and coverage. **Status:** current review draft; supervisor approval pending.

## Motivation

Currency carry earns a payoff by holding currencies with higher interest-rate-related carry against lower carry currencies. Its exposure to global risk-off states may be important even if its unconditional average payoff is positive. Distinguish a contemporaneous risk-state description from a forecast made before the return period.

## Research question

Are currency carry returns lower and market exposures larger in risk-off states, and can lagged global risk measures forecast carry returns?

## Economic mechanism

Compare $E[c_t\mid I_t=1]$ with $E[c_t\mid I_t=0]$; predict $c_{t+1}$ using only information at $t$.

## Research design

Use the specified published G10 gross carry, monthly market, VIX and NFCI series subject to access and coverage. Freeze risk-off thresholds in training; contrast contemporaneous stress associations with expanding forecasts using lagged indicators. Net is optional and must retain its provider definition.

Audit the G10 gross definition and dates before use. Report state counts, training thresholds, information lags and common forecast origins. Do not substitute other carry factors or claim causal effects.

\newpage

## Required exhibits

Carry wealth and drawdown plot; state means/exposures; predictive OOS R2 and loss intervals; gross/net comparison.

## Minimum viable thesis

One documented G10 gross carry series, common monthly market/VIX data, state-dependent returns and lagged forecasting; net optional if accessible. Distinct from A09.02.01 bilateral forward premium puzzle.

## Scope and feasibility

Published carry is not bilateral UIP or newly implementable strategy. Check long-short return leverage/normalization. VIX contemporaneous conditioning is descriptive; NFCI revised vintage is pseudo-real-time. Rare states have limited power.

**Prerequisites:** FX returns, conditional regressions, portfolio factors, time-series inference.

**Optional extension:** Compare G10 and broader currency universe if same provider definitions; tail regressions.

## Milestones

W1-3: theory and data gate; W4-6: common sample; W7-9: state exposures; W10-12: forecasts and robustness; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
