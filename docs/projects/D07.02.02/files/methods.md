---
title: "Focused methods — Interest Rate Options under Gaussian and Square-Root Dynamics"
subtitle: "D07.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Shift and support
For unshifted positive factor $x$ with discount curve $P_x$, set $P_r(0,T)=P_x(0,T)\exp(-\int_0^T\varphi(s)ds)$. The shift is determined by the ratio of the target and base discount curves. The shifted short rate can be negative; the CIR state remains nonnegative. At expiry $u$, shifted bond price is $P_x(u,T)\exp(-\int_u^T\varphi(s)ds)$. Because the CIR bond price is decreasing in the factor, it has a finite upper endpoint. A strike above that endpoint produces a structural zero, not a numerical failure.

## Matched comparisons
Use the same initial forward and strike; one ATM match does not imply equality of other prices. Validate affine pricing against exact-transition CIR simulation with refined integrated discounting, and an independent Gaussian benchmark. For parallel curve bumps re-fit the deterministic shift but keep stochastic dynamics and strike fixed. Report unmatched cases, OTM structural zeros, and a non-negligible OTM sensitivity with bump convergence.

## Research checks

Freeze the ATM match before comparing other strikes; report domain and uncertainty rather than forcing implied volatilities for zero prices. Distinct from A05.01.01 physical transition estimation.
