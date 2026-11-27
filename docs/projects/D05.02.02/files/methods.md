---
title: "Focused methods — Numerical Stability in Finite-Difference Option Pricing"
subtitle: "D05.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Time stepping and stability
Use $x=\log(S/K)$, time step $h$ and uniform spatial step $\Delta x$. The centered discounted generator $L$ gives the $\theta$-method, with $\theta=0,1,1/2$ for explicit, backward Euler and Crank--Nicolson. In pure diffusion, explicit stability requires $\sigma^2h/(\Delta x)^2\le1$; with drift and discount test the actual stencil and amplification restrictions. CN is A-stable but its amplification factor tends to $-1$ on stiff negative modes; backward Euler damps them. Rannacher startup uses implicit half steps before CN.

## Payoff and sensitivities
Initialize the call kink and digital jump with specified node or cell-average conventions and asymptotic boundaries. In log coordinates $\Delta=u_x/S$ and $\Gamma=(u_{xx}-u_x)/S^2$. Test errors around strike at positive expiry; report oscillations and negative values instead of clipping. Separate temporal, spatial, boundary and payoff representation errors.

## Research checks

Compare analytical prices and Greeks over spot, not just ATM. A-stability does not imply positivity or accuracy. Exclude deliberately unstable runs from successful time-to-tolerance comparisons.
