---
title: "Macroeconomic Expectations and the Predictability of Bond Returns"
subtitle: "Research proposal | A05.03.03"
---

**Asset pricing · Fixed income and interest rates · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Forward rates embed both expectations and risk compensation. Survey forecasts may contribute independently measured information about future growth and inflation. The study evaluates incremental pseudo-out-of-sample predictability conditional on a yield-only benchmark and documented survey releases.

## Research question

Do real GDP growth and inflation expectations from the Survey of Professional Forecasters improve pseudo-out-of-sample forecasts of future Treasury excess returns beyond forward-rate factors?

## Economic mechanism

Use a released macro expectation vector $z_t$ in $\widehat{rx}_{t+4|t}^{(n)}=a_n+b_n^\top f_t+c_n^\top z_t$ at quarterly frequency.

## Research design

Match GSW zero yields to the same-survey GDP and CPI forecasts and actual SPF release dates. Form one-year aged excess returns at the prescribed maturities; estimate yield-only and augmented forecasts on the same eligible origins, with expanding estimation and matured annual labels.

Require release and horizon metadata before estimation. If necessary use the original minimum of one released horizon and two maturities; do not substitute dispersion for expected growth. Label the result pseudo-OOS unless vintages are truly reconstructible.

\newpage

## Required exhibits

Forecast calendar and sample table, coefficient paths, OOS forecast performance by maturity, incremental predictive-loss intervals.

## Minimum viable thesis

One released SPF horizon, two maturities, historical mean/yield-only/augmented forecasts, overlap-aware held-out scoring.

## Scope and feasibility

SPF levels may mix units or definitions across vintages; use same-vintage ratios and document horizon. Retrospective fitted yields and revisions make exercise pseudo-real-time unless verified. No claim of causal forecasting mechanism or trading profitability.

**Prerequisites:** Fixed income, predictive regressions, forecast evaluation, macro data.

**Optional extension:** Add dispersion measured separately from expected growth, after validating SPF D2 horizon and release conventions.

## Milestones

W1-3: literature and SPF calendar; W4-6: features and labels; W7-9: rolling estimation; W10-12: held-out and uncertainty; W13-16: writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
