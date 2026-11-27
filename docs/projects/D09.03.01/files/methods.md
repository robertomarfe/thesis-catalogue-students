---
title: "Focused methods — Corporate Credit Quality Spreads and Macroeconomic Conditions"
subtitle: "D09.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Measurement and alignment
For seasonally adjusted industrial production $I_t$, annual growth in log-percent is $g_t=100\log(I_t/I_{t-12})$. Average daily VIX closes within each month before merging, retaining month-level observation counts. Match the exact monthly calendar; missing months are not zero and are not adjacent observations. Baa-Aaa is an average rating-quality spread, not a maturity-matched traded credit portfolio.

## Conditional associations
A descriptive specification is
$$s_t=a+\phi s_{t-1}+b g_{t-1}+c\,\mathrm{VIX}_{t-1}+u_t.$$
Compare the autoregressive benchmark and a specification with $\Delta s_t$ as target on a common sample. Report standardized effects, persistence and HAC or block uncertainty. Recession chronology and revised industrial production are retrospective; crisis/subperiod selection must be predeclared. Association does not identify causal effects or a physical default probability.

## Research checks

This design remains blocked until the supervisor verifies rights for both Moody series and actual input coverage. Record original filename, vintage and permitted retention separately for each series. No substitute index or simulation can satisfy the unchanged empirical MVT.
