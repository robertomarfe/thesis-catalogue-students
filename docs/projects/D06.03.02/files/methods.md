---
title: "Focused methods — Autocallable Notes: Pricing and Embedded Risk"
subtitle: "D06.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Contract and cashflow ledger
Set notional to one and $R_j=S_{t_j}/S_{\mathrm{ref}}$ with fixed issue reference. Redeem at the first eligible date with $R_j\ge1$, paying $1+jc$. If never called, at maturity pay $1+mc$ when $R_m\ge B$, otherwise $R_m$ with no coupon. Include threshold equality and a single mutually exclusive redemption cashflow. Define $A,B_c$ as discounted principal and coupon loading. Under $\mathbb Q$ value is $\mathbb E A+c\mathbb E B_c$; a positive loading is necessary to solve for a coupon. If base PV exceeds par, a negative root is not a feasible nonnegative issue coupon.

## Risk and uncertainty
Use exact observation-date sampling and paired bumps at fixed reference and contract terms. Discontinuities invalidate naive pathwise Greeks. Estimate coupon uncertainty as a ratio using paired or replicate observations. Distinguish Q contractual life from P loss and default termination. Independent zero-recovery default is a stylized optional scenario.

## Research checks

Validate first-call, no-call, equality and maturity paths by hand. Freeze coupon before physical stress. Report ratio uncertainty and infeasibility; do not confuse a stylized price with an issue quote.
