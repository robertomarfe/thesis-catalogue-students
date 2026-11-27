---
title: "Focused methods — Digital Assets and Traditional Asset Pricing Factors"
subtitle: "A09.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Calendar and quote convention
Use USD prices and the documented observation timestamp; the historical source recipe mentions 5 PM PST, which must be verified against actual provider documentation. Do not infer a trading-day calendar from daily crypto observations. For the first monthly return retain the prior month-end level. Use simple returns and subtract the same monthly USD RF used in factors. Missing exact endpoints are a gate, not an invitation to interpolate. The last-US-trading-day alternative requires an independent exchange calendar and acknowledges asynchronous closes.

## Factor exposure
For monthly factors $f_t$, estimate the intercept and market, size and value exposures on matched dates; define a trailing window and minimum count before reporting rolling betas. Use dependence-aware uncertainty and distinguish descriptive rolling estimates from any lagged predictive specification. Check a lagged VIX specification separately. Neither a changing beta nor an intercept identifies crypto-wide risk pricing. Large valid returns remain in the baseline; investigate errors, not inconvenient observations.

## Research checks

Blocked until permission, actual coverage and timestamp are validated. Retain the baseline 72-month and split 36-month thresholds from the input protocol; require exact prior endpoints and documented timing robustness. No unapproved substitute or raw redistribution.
