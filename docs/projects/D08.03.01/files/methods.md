---
title: "Focused methods — Covered Calls versus Buy-and-Hold: Risk and Performance"
subtitle: "D08.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Payoff and index return
Without dividends, parity gives $S_0-C_0=Ke^{-rT}-P_0$. Equal payoff and funding require common strike, maturity and carry. A rolling index accounts for premium and roll methodology and is not an actual investor's trading record.

## Risk matching
A feasible equity weight is $w_{t-1}=\widehat\sigma^B_{t-1}/\widehat\sigma^M_{t-1}$ subject to declared bounds. Compare $w_{t-1}R^M_t+(1-w_{t-1})R^f_t$ with BXM on common months. Use lagged rather than test-period risk estimates. Report achieved risk, upside/downside capture conditional on comparator sign, counts and paired uncertainty.

## Research checks

This is historical buy-write evaluation, not synthetic hedge optimization. Gate remains blocked until BXM rights and history pass. Price-only SP500 is not an admissible comparator; no pure option-premium interpretation.
