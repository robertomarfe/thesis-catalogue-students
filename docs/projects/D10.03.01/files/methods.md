---
title: "Focused methods — Covered Interest Parity and Synthetic FX Forward Rates"
subtitle: "D10.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Cash-and-carry accounting
Let $S_t$ be USD per EUR, $r_d$ the USD annual rate, $r_f$ the EUR annual rate and $\tau$ the year fraction. Borrow USD to buy EUR now, invest EUR and repay USD at delivery; no-arbitrage with identical borrow/lend rates gives $F_t=S_t(1+r_d\tau)/(1+r_f\tau)$. Both accrual factors must be positive. Under continuous compounding the formula is $S_te^{(r_d-r_f)\tau}$ instead. For a long one-EUR forward with strike $K$, current value under the same simple-accrual model is $S_t/A_f-K/A_d$ in USD, zero at $K=F_t$. Invert the quote and swap currency roles consistently.

## Proxy interpretation
Report points $(F_t-S_t)/10^{-4}$ in pips, not percent returns. Audit prior-month rate publication, series definitions and missing dates; same-month averages are a descriptive sensitivity. These proxies do not measure actual executable funding or observed forward prices. A hypothetical basis shift is a scenario, not an estimate of CIP deviations. If overlap fails, obtain explicit approval before converting the empirical project to synthetic scenarios.

## Research checks

Verify quote orientation, rate units, positive accrual, zero initial PV and reciprocal identity. Record availability and exact overlap. No observed basis or executable trade claim.
