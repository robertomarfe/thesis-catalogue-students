---
title: "Are Stocks and Bonds Effective Inflation Hedges?"
subtitle: "Research proposal | A04.02.02"
---

**Asset pricing · Macro-finance and policy risk · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

An asset protects purchasing power only to the extent that holding returns respond favorably to inflation. A yield change is not a bond return, and hedge performance depends on how maturities age.

## Research question

How do equity and nominal Treasury holding returns covary with realized and unexpected inflation, and does their effectiveness as purchasing-power hedges vary across horizons?

## Economic mechanism

For log discount price $p_t(n)=-n y_t(n)$, the log return of an $n$-year zero held for $H$ months is $r^B_{t,t+H}=p_{t+H}(n-H/12)-p_t(n)$.

## Research design

GSW nominal curve, exact monthly and annual aging of 5/10-year synthetic zeros; equity total return, CPI, expanding release-safe AR forecast, fixed subperiods and 60/40 robustness.

Compute both bond prices for n and n-h using the same documented GSW Svensson convention; verify flat-curve log holding return h*y. Compound monthly gross legs and deflate with exact adjacent CPI; fit inflation AR only on available history, use overlapping-horizon HAC or nonoverlap sensitivity and paired date blocks. Label retrospective hedge exposure, not expected return.

\newpage

## Required exhibits

Construction checks, nominal/real return and inflation tables, beta intervals, horizon/regime plots and real portfolio risk comparison.

## Minimum viable thesis

Monthly and annual nominal/real returns of equity and one synthetic zero maturity; realized and modeled surprise inflation, robust intervals and fixed subperiod comparison. Distinct from A04.02.01 cross-sectional pricing.

## Scope and feasibility

GSW zero returns are synthetic government bond holdings, not bond-fund returns or OIS. CPI revisions and release timing constrain true real-time surprises; AR residuals are model-based, not structural shocks. Realized inflation is not observable at the investment date. Regressions are descriptive hedging associations, not causal effects.

**Prerequisites:** Fixed income, return compounding, time-series econometrics, Python.

**Optional extension:** Use SPF inflation expectations or real TIPS curve for a shorter sample; distinguish inflation compensation from expected inflation.

## Milestones

W1-3: Fisher relation and data; W4-6: return construction; W7-9: inflation regressions; W10-12: regimes and portfolio risk; W13-16: write and validate.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
