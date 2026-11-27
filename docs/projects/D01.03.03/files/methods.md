---
title: "Focused methods — Option Pricing and Hedging in the Presence of Extreme Market Movements"
subtitle: "D01.03.03 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Finite jump exposure
Under Merton pricing dynamics, a jump multiplier $J$ changes the value of a call from $C(S)$ to $C(SJ)$, holding time and parameters fixed. The residual against a stock delta is
$$C(SJ)-C(S)-C_S(S)S(J-1).$$
For small jumps it is locally related to gamma; large jumps need not be accurately represented by a second-order expansion. A secondary option $H$ allows local delta-gamma matching through $g=C_{SS}/H_{SS}$ and $h=C_S-gH_S$. A small denominator produces unstable positions. Declare a cap, fallback and threshold before viewing the test sample, and report their use.

## Financing and tail risk
For zero dividends, start each short-call hedge with the same true premium. At rebalancing set cash $B=V-hS-gH$; across the interval it accrues at $r$. At expiry value both options at their contractual payoffs. Define discounted loss $L=e^{-rT}(C_T-V_T)$ and upper-tail expected shortfall at confidence $\alpha$ by
$$ES_\alpha=\min_z\{z+(1-\alpha)^{-1}\mathbb E[(L-z)^+]\}.$$
Use a consistent finite-sample tail convention, especially with ties. Distinguish the pricing measure and physical stress law, hold the risk-neutral model fixed in the physical stress, and estimate paired uncertainty for the difference in ES. Gamma matching does not guarantee lower loss for every jump.

## Research checks

Predeclare gamma caps and fallback before comparing stress scenarios. Use matched paths, initial capital and funding; report ES uncertainty and the frequency of constrained positions, including the no-jump subset.
