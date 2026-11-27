---
title: "Focused methods — Equity Yield Curves across Investment Styles"
subtitle: "A06.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For an exactly matched high/low style pair define $\Delta e_t(n)=e_{H,t}(n)-e_{L,t}(n)$.

The difference of 10–1 year slopes is $\Delta e_t(10)-\Delta e_t(1)$. Estimate uncertainty from joint blocks of dates, preserving all assets and maturities together. Positive-dividend portfolio claims are essential for log normalization; a long-short factor payoff is not such a claim. A slope difference cannot identify duration or discount-rate news separately from cash-flow expectations. Report labels, weights, units and vintage; no inferred French crosswalk.

## Research checks

Require positive-dividend portfolio IDs and validated exact high/low style crosswalk with common 1/5/10y dates; report both individual curves and paired differences/slope, joint calendar-block intervals and sensitivity across regimes. Keep matched weighting, units and vintage. If exact pair not verified, stop rather than substitute FF labels.
