---
title: "Focused methods — Variance Risk Premia and Economic Uncertainty"
subtitle: "A07.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Separate the two variance legs
Let $RV_{t,30}$ be the sum of squared log returns during the next 30 calendar days. The annualized physical forecast is $(365/30)E_t^{\mathbb P}[RV_{t,30}]$; the risk-neutral leg is approximated by squared decimal VIX. Forecast using only matured labels and predeclared historical/HAR-style regressors. Use the same units for both legs and show sensitivity to physical forecast error. VIX and the broad FF market proxy have different underlying definitions.

## Association and uncertainty
Estimate a relation of the form $VRP_t=a+b\log EPU_{t-\ell}+cP_t+dNFCI_{t-\ell'}+e_t$. Use lags reflecting availability, not a convenient observation-date join; revised data cannot establish actual real-time performance. Re-estimate the generated physical forecast inside joint time blocks where feasible. The regression is descriptive/conditional, not an instrumented causal design.

## Research checks

Verify rights for EPU and other series. Keep a release-date ledger, include a predeclared crisis sensitivity, and report forecast uncertainty alongside association. A positive or negative association is not itself a causal finding or a return premium.
