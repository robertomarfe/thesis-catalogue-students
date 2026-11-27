---
title: "Focused methods — The Term Structure of Implied Volatility in Equity Markets"
subtitle: "D02.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Horizon-consistent variance
For index levels $I_{30},I_{90}$ expressed in volatility percentage points, let $v_j=(I_j/100)^2$ and $T_j=j/365$ under the approximate calendar convention. Total variance is $w_j=T_jv_j$. The implied forward-variance proxy is
$$v_{30,90}=\frac{T_{90}v_{90}-T_{30}v_{30}}{T_{90}-T_{30}}.$$
Verify the provider horizons and definitions; raw index differences are not forward variance. Flag negative proxies rather than automatically repairing them. Finite option strikes and index construction qualify the risk-neutral interpretation.

## Physical targets and information sets
For daily log returns $u_d$ and origin $t$, annualize the sum over audited trading sessions inside the next $h$ calendar days:
$$Y_{t,h}=\frac{365}{h}\sum_{t<d\le t+h}u_d^2.$$
A missing required session makes the target missing. The outcome becomes available no earlier than $t+h$. Build historical-variance, level-only and level-plus-slope models with positive variance predictions, using only matured training targets. Use the same held-out origins and horizon for QLIKE $\log f+Y/f$ and squared-error comparisons; overlapping targets require dependence-aware inference. French market returns are a broad-market proxy, not a matched SPX return. Forecast accuracy does not imply equality between $\mathbb P$ and $\mathbb Q$ variance expectations.

## Research checks

Check common month-end dates and complete 30/90-calendar-day target intervals before fitting. Preserve the information set at every forecast origin; separate the implied level and forward proxy, and score common outcomes.
