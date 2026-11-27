---
title: "Focused methods — The Disposition Effect and Return Predictability: A Simulation Study"
subtitle: "A12.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

Investor order $q_i(P)=\max(a_i(F-P)/P_- -s_i h_i,-h_i)$, with previous price $P_-$ and holdings $h_i$.

Provider demand $m(F-P)/P_-$, $m>0$, makes total demand continuous strictly decreasing for $a_i\geq0$. Check clearing and invalid prices. Purchases update reference by share-weighted cost; sales leave surviving reference unchanged. Centered propensity matches mean, not turnover; calibrate turnover on development paths only. Investor cash unconstrained, provider may short; compare paired news and strictly lagged overhang.

## Research checks

Check monotone market clearing, nonnegative holdings and exact inventory accounting; reproduce purchase-weighted reference update and no-reference/symmetric/asymmetric controls with identical shocks. Add explicit matched-turnover calibration on development paths only, report unmatched paths and paired simulation intervals; use strictly lagged predictive variables. No claim on actual investor data.
