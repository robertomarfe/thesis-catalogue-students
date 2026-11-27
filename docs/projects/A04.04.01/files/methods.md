---
title: "Focused methods — Economic Policy Uncertainty and Equity Market Risk"
subtitle: "A04.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For daily log market returns in month $t+1$, use $V_{t+1}=\sum_{d\in t+1}r_d^2$. A VIX reading $v_t$ in index points yields proxy $(v_t/100)^2/12$.

The VIX proxy converts implied annualized variance to approximate monthly units, not physical conditional variance. Fit positive forecasts with past variance and VIX, then add released news EPU. For log regression estimate smearing from matured training outcomes only. For positive forecast $f$ and target $V$ compare $V/f-\log(V/f)-1$ and squared errors on identical dates; freeze any floor before testing. Use only EPU released by origin, including conservative extra lag if release history is unavailable. Distinguish news EPU from composite EPU and label revised-history exercises pseudo-out-of-sample. Daily squared log returns are not intraday realized variance.

## Research checks

Freeze lag and return-calendar coverage; use only published EPU and VIX at origin, report conservative extra-lag sensitivity. Match forecast horizon, positive variance units and common origins; train smearing only on mature outcomes; compare paired QLIKE/MSE and crisis sensitivity, no causal claim.
