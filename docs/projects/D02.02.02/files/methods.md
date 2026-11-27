---
title: "Focused methods — Calibrating Equity Option Surfaces with Real Market Quotes"
subtitle: "D02.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Contract-level quote normalization
For one European cash-settled contract family, use matched settlement dates, discount $D$ and forward $F$; $C-P=D(F-K)$ only for synchronized, otherwise comparable contracts. With $k=\log(K/F)$ and total implied variance $w=T I^2$, use out-of-the-money quotes and convert puts to call equivalents by parity. Record bid, ask, timestamp, multiplier, exact expiry, exercise convention and the origin of the forward. Bound violations are diagnostics, not values to clip indiscriminately.

## Static versus structural calibration
Fit raw SVI $w=a+b[\rho(k-m)+\sqrt{(k-m)^2+s^2}]$ slice by slice, and Heston jointly across maturities under $\mathbb Q$. A baseline flat Black volatility gives a simpler reference. For common price errors $e_i=C_i^{fit}-C_i^{mid}$ compare raw currency loss and $\sum_i(e_i/\max(s_i,s_{min}))^2$, where $s_i$ denotes the spread and the floor is chosen before the test. Report fraction inside bid/ask, held-out price and IV errors, and finite-grid arbitrage. Slice interpolation is not a stochastic price model; an entire-maturity holdout requires explicit interpolation for SVI. No rights, quote coverage or empirical results are supplied. A commercial sample file does not establish feasibility.

## Research checks

Do not assign the original empirical design until rights, underlying/forward synchronization and accepted dates/strikes are verified. Freeze cleaning variants, objective and held-out contracts; compare identical observations and retain rejected quote counts.
