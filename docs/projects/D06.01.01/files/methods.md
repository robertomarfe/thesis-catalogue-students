---
title: "Focused methods — Asian Option Pricing and the Value of Averaging"
subtitle: "D06.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Geometric and arithmetic averages
For exact GBM, $\log S_{t_j}=\log S_0+(r-q-\sigma^2/2)t_j+\sigma W_{t_j}$. Hence $\log G$ has mean $\mu_G=\log S_0+(r-q-\sigma^2/2)\bar t$ and variance $s_G^2=\sigma^2m^{-2}\sum_{i,j}\min(t_i,t_j)$. Its mean level is $e^{\mu_G+s_G^2/2}$. Derive a lognormal call expectation and discount to payment $T$. The arithmetic average is not generally lognormal; use the geometric call as a control with an independent pilot coefficient.

## Schedule and exposure
One fixing at $T$ reduces to a European claim, and $A\ge G$ implies ordering for matched Asian calls. Nonzero carry changes expected average levels when dates change. Estimate delta and vega at fixed contractual dates and strike using common normals and bump convergence. All fixings are future at initiation; realized fixings would change the state and sensitivity convention.

## Research checks

Change frequency and window separately. Use union-grid draws where practical because grids are not nested. Preserve payment time; do not call a finite fixing grid a continuous average.
