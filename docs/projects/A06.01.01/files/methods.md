---
title: "Focused methods — Dividend Growth Expectations and the Valuation of the Stock Market"
subtitle: "A06.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

With annual simple growth $g$ and constant required return $k>g$, the Gordon ratio is $P_t/D_t=(1+g)/(k-g)$.

At fixed $g$, the rate derivative is $-(1+g)/(k-g)^2$; at fixed $k$, the growth derivative is $(1+k)/(k-g)^2$. A given ratio $v$ identifies the locus $k=g+(1+g)/v$, not two parameters. In a two-stage model discount the explicit annual dividends plus the terminal price computed at the final date using next-year dividend. Report terminal share and ensure long-run convergence. December Shiller observations are monthly-average price and trailing annual dividend proxies, not exact year-end payout accounting.

## Research checks

Manually verify December dates and units; report missing years and log-to-simple growth conversion, iso-P/D contours and required-return/growth pairs. Compare one- and two-stage prices with identical growth limit and terminal share; show sensitivity to horizon and a small joint parameter perturbation. Do not use historical growth as investor forecast without a model.
