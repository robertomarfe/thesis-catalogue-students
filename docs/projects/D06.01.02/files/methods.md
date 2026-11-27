---
title: "Focused methods — Barrier Options and Discrete Monitoring Risk"
subtitle: "D06.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Two contracts and one path law
For lower barrier $B<S_0$, strike $K$ and maturity $T$, the continuously monitored payoff is $(S_T-K)^+\mathbf1\{\inf_{0\le t\le T}S_t>B\}$. Discrete monitoring instead checks agreed dates including expiry. Conditional on log endpoints, crossing probability does not depend on drift. For $x,y>b=\log B$, interval survival is
$$p(x,y;h)=1-\exp[-2(x-b)(y-b)/(\sigma^2h)].$$
It is zero if either endpoint is at or below $b$. Multiply conditional interval survivals or sample crossings, using stable evaluation near the boundary. Use a reflected transition density for an independent continuous reference within its domain.

## Numerical versus economic difference
On common endpoints the discrete payoff weakly exceeds the conditional continuous payoff. This is a monitoring premium between distinct contracts, or discretization bias only when the target is continuous monitoring. Check in/out parity with identical monitoring and the low-barrier vanilla limit.

## Research checks

Use paired SE on identical endpoints within each grid; 12/52/252 are not nested. Do not bridge-adjust a genuine discrete contract. Include the immediate-knockout case and retain underflow diagnostics.
