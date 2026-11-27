---
title: "From Discount Curves to Interest Rate Swap Prices"
subtitle: "Research proposal | D07.01.01"
---

**Derivatives · Fixed income and interest rates · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Discount curve interpolation changes forward rates and can therefore change hypothetical swap values even when two methods reproduce all quoted zero-yield nodes. Measure the economic magnitude in basis points and currency units for fixed contracts, keeping the single-curve abstraction explicit.

## Research question

How do curve shape and interpolation choices affect hypothetical single-curve par swap rates and PV01/key-rate risk across maturities? When are differences economically material for a fixed notional?

## Economic mechanism

For $A=\sum_i\alpha_iP(0,t_i)$, the spot-starting single-curve par rate is $K=(1-P(0,T))/A$.

## Research design

Use verified GSW nominal zero curves and a predeclared selection of six curve regimes. Compare linear zero yields and linear log discounts at identical annual/semiannual schedules and notional; report par rates, forwards and signed parallel/local sensitivity with fixed coupon.

Verify node reproduction, discount positivity, zero PV at par and bump convergence. Separate interpolation and short-end extrapolation; synthetic fallback requires an explicit approved redesign.

\newpage

## Required exhibits

Curve and forward plots for selected dates; swap rate/DV01 table and time series of interpolation differences; key-rate exposure chart; unit/zero-PV tests. Report exact discounting conventions, and treat all prices as hypothetical examples rather than market quotes.

## Minimum viable thesis

A downloaded verified zero curve, two interpolation schemes, correct par identity, at least three swap maturities and curve regimes, plus DV01 sensitivity and economic interpretation. Fallback: transparent synthetic curves if the dataset cannot be obtained, with amended empirical claim.

## Scope and feasibility

Check nonpositive discount factors and implausibly oscillating forwards; do not impose positive forwards merely as no-arbitrage under negative-rate regimes. Compare short-end extrapolation, payment frequencies and bump shape; ensure key-rate and parallel bumps are consistently defined. Government curves are not OIS, and floating projection is an explicit single-curve simplification.

**Prerequisites:** Fixed income, discount factors, calculus and interpolation, Python pandas/SciPy. No actual swap dealer quotes needed.

**Optional extension:** Add a separate stylized projection curve and explain basis risk, or compare ECB AAA government zero curves without inferring actual USD/EUR swap market spreads.

## Milestones

W1-3: derive par rate and risk measures, acquire data; W4-6: parse zero yields and validate synthetic flat curves; W7-10: build panel of swap values and key-rate sensitivities; W11-13: stress tests and short-end conventions; W14-16: interpret and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
