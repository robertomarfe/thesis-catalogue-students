---
title: "Focused methods — Currency Carry Returns and Global Risk States"
subtitle: "A09.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Payoff and information sets
Let $c_t$ be the documented monthly gross carry excess payoff in decimal units. Do not treat an unfunded long-short payoff as a total return on one unit of invested wealth without an explicit capital and funding convention. Define $I_t$ from a prespecified market-tail or high-volatility criterion and report $E[c_t\mid I_t]$, downside quantiles, sample counts and dependence-aware intervals. A state defined using month-$t$ market outcomes is not known before month $t$.

## Predictive comparison
At origin $t$, estimate $c_{t+1}=a+bz_t+e_{t+1}$ using only fully matured training pairs, with $z_t$ an available VIX or financial-conditions observation. Use an expanding historical mean on identical test dates; compare loss and out-of-sample $R^2=1-\sum e_{\mathrm{model}}^2/\sum e_{\mathrm{mean}}^2$. Freeze variable scaling and selection before testing. Revised NFCI is not automatically real-time; identify vintage limitations. Net returns, if accessible, reflect modeled costs and not the student's execution.

## Research checks

Audit the G10 gross definition and dates before use. Report state counts, training thresholds, information lags and common forecast origins. Do not substitute other carry factors or claim causal effects.
