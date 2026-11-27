---
title: "Focused methods — Structural Credit Models with Early Default"
subtitle: "D09.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Continuous crossing
For $x_t=\log(V_t/H)$ under $\mathbb Q$, $dx=(r-\sigma_V^2/2)dt+\sigma_V dW$. Conditional on positive endpoints $x,y$ over length $h$, the probability of a hit is $\exp[-2xy/(\sigma_V^2h)]$; if either endpoint is nonpositive, a hit is certain. The conditional bridge removes the constant drift. Compare this with the unconditional first-passage law obtained by reflection. For $x_0>0$ and drift $m$, survival to $T$ equals
$$\Phi\left(\frac{x_0+mT}{\sigma_V\sqrt T}\right)-e^{-2mx_0/\sigma_V^2}\Phi\left(\frac{-x_0+mT}{\sigma_V\sqrt T}\right).$$

## Recovery contract
For maturity-contingent recovery, the terminal payment is $RF$ on an early hit and $\min(V_T,F)$ otherwise. Price the entire terminal payment at $e^{-rT}$. A recovery paid at the hitting date is a different instrument. Use $RF\le H<F$ as prescribed; do not infer a general ordering across recovery rules.

## Research checks

Show the analytic hit check, bridge versus endpoint-only monitoring and common-path paired intervals. Compare the maturity-only benchmark under identical terminal inputs. Preserve unsuccessful or high-error grid cases and quantify both default timing and loss effects.
