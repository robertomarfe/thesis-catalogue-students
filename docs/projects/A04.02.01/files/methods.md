---
title: "Focused methods — Inflation Risk and the Cross-Section of Equity Returns"
subtitle: "A04.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

With quarterly average CPI $I_q$, let $\pi_q=I_q/I_{q-1}-1$ and $\widehat\pi_q=(1+f_{q-1}/100)^{1/4}-1$. The surprise is $u_q=\pi_q-\widehat\pi_q$.

Here $f_{q-1}$ is the previous-vintage annualized quarterly-average CPI forecast. Verify target and vintage, not just column names. For nominal gross portfolio and bill returns the real simple excess return is $(R_i-R_b)/(1+\pi_q)$, not nominal excess minus inflation. Exposure regressions include a consistently defined market excess return and the same surprise. Regress average excess returns on estimated inflation and market betas, reporting rank and leverage. Re-estimate both stages jointly in calendar-quarter blocks to preserve cross-asset dependence and generated-beta uncertainty. The relation is descriptive, not a structural risk price.

## Research checks

Hand-check one quarterly-average CPI realization and one forecast error from the prior vintage; compound market, portfolio and bill legs separately. Estimate nominal and real exposures on matched quarters and jointly bootstrap quarters, re-estimating both stages. Report common sample, rank, regime split and revised-CPI caveat.
