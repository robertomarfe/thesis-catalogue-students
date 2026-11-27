---
title: "Focused methods — From Discount Curves to Interest Rate Swap Prices"
subtitle: "D07.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Curve and swap conventions
For continuous zero yield $y(t)$, $P(0,t)=e^{-ty(t)}$. At nodes both interpolations reproduce the input; between nodes, linear log discounts imply piecewise constant instantaneous forwards. Flat first yield below one year is an explicit extrapolation, not an OIS observation. At reset and without spreads, the floating leg telescopes to $1-P(0,T)$. Receiver PV is $N[K A-(1-P(0,T))]$; payer has opposite sign.

## Sensitivities
Define signed DV01 as the centered PV change for a positive one-bp yield shock: $[V(y+\delta)-V(y-\delta)]/2$ with $\delta=10^{-4}$. Freeze the original fixed coupon, notional and payment schedule. Use explicit localized shock shapes for key-rate risk. Negative forwards alone are not arbitrage in a negative-rate environment. Treasury curves support hypothetical examples, not actual collateralized swap quotes.

## Research checks

Verify node reproduction, discount positivity, zero PV at par and bump convergence. Separate interpolation and short-end extrapolation; synthetic fallback requires an explicit approved redesign.
