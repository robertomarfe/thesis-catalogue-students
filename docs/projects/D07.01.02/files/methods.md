---
title: "Focused methods — Interest Rate Swaps and the Management of Duration Risk"
subtitle: "D07.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Position signs and repricing
Bond value is $V_B=\sum_i CF_iP(t_i)$. For payer swap, $V_S=N[(1-P(T))-K\sum_i\alpha_i P(t_i)]$ in the reset-date single-curve abstraction. Define signed PV change per +1 bp by centered difference for each shock. With sensitivity matrix $D$ (columns are per-unit hedge instruments), solve $d_B+Dh=0$ for selected target exposures, using constraints and documenting singular or ill-conditioned cases.

## Economic comparison
Reprice with original cash flows after the next observed curve shock; this is not a holding-period return, since no time elapses in the repricing convention. Compare residual P&L dispersion, nonlinear error, tail exposure and gross notionals. Test bump sizes and shock basis; avoid par-resetting coupons after the bump.

## Research checks

Report initial zero PV for swaps, matched shocks and risk reduction net of exposure sign mistakes. Distinct from D07.04.02: swap DV01/key-rate hedging rather than PCA zero-bond spanning.
