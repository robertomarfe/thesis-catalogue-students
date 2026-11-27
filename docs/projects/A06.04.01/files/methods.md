---
title: "Focused methods — Equity and Bond Yield Slopes over the Business Cycle"
subtitle: "A06.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

Use matched maturities $s^E_t=e_t(10)-e_t(2)$ and $s^B_t=b_t(10)-b_t(2)$.

With retrospective recession indicator $I_t$, estimate $s^E_t=a+b s^B_t+c I_t+d s^B_t I_t+u_t$. Expansion association is $b$, recession association $b+d$; report the latter with its joint covariance. Distinguish regression on levels from changes; preserve persistence in joint calendar blocks and count recession episodes. Use alternative maturity pairs and lagged industrial production growth as prespecified; retrospective labels are not signals available to investors. Nominal-real mismatch cannot isolate inflation risk.

## Research checks

Verify exact GKK/GSW grid 2/10y with dates and units, distinguish level regression from change regression, compare interaction coefficient with prespecified alternative maturity pairs and lagged IP growth. Resample joint date blocks, report recession episode counts and leave-one-episode sensitivity; no causal identification or real-time prediction.
