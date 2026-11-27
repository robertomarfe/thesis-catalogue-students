---
title: "Focused methods — Growth versus Value: Cash Flow Timing and Discount Rate Risk"
subtitle: "A06.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For fixed positive cash flows $c_j$ and continuously compounded rate $y$, $P(y)=\sum_{j=1}^H c_j e^{-jy}$.

With $w_j=c_j e^{-jy}/P$, duration is $-P_y/P=\sum_j j w_j$ and convexity is $P_{yy}/P=\sum_j j^2 w_j$. Under a maturity-dependent shift, first-order log price change is $-\sum_j j w_j\Delta y_j$. Compare central differences at several step sizes and reprice explicitly when cash flows change. Common initial price does not imply common duration. Historical rate beta incorporates revisions to cash flows and is not this derivative.

## Research checks

Normalize two positive cash-flow profiles to identical PV, confirm weights sum to one and analytic duration/convexity via central differences at multiple step sizes. Compare parallel/nonparallel shifts and explicit changed cash-flow scenario; test 50/100y truncation. Historical evidence is optional; no claim about observed growth/value beta without matched data.
