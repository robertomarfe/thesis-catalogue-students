---
title: "Focused methods — Modeling Commodity Spot Prices with Mean-Reverting Processes"
subtitle: "D10.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Exact transition and admissibility
For monthly interval $h=1/12$ years, the OU transition is Gaussian with conditional mean $\mu+(x_t-\mu)e^{-\kappa h}$ and variance $\sigma^2(1-e^{-2\kappa h})/(2\kappa)$. The discrete AR(1) coefficient is $\phi=e^{-\kappa h}$; only $0<\phi<1$ maps to positive finite mean reversion. Report inadmissible fits rather than clipping silently. Distinguish conditional log forecast from mean price forecast (which requires the lognormal variance correction under the model).

## Release lag and forecast comparisons
At end of month $t$, if the latest available monthly average is $t-1$, the target for month $t+H$ requires $H+1$ transitions, for OU and random walk alike. Verify actual release rules. Do not compress missing months or take logs of nonpositive prices; report exceptions and a level-model sensitivity where necessary. Test on common origins and target dates; overlap requires block or HAC inference. Physical estimates are not risk-neutral pricing parameters.

## Research checks

Audit positivity, complete monthly dates, release lag and actual targets. Verify OU transition and random-walk limit on artificial data, report inadmissible fits and paired loss comparisons.
