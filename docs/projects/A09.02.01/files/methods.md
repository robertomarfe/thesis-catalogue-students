---
title: "Focused methods — The Forward Premium Puzzle and Currency Carry"
subtitle: "A09.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Quote orientation and UIP
Use $S_t$ and $F_t$ in USD per GBP with matched fixing and tenor. The forward premium is $f_t-s_t$ in log units; expected log spot appreciation equals this premium under the usual log-linear UIP benchmark. The regression null is $(\alpha,\beta)=(0,1)$ under that benchmark; Jensen terms and currency risk premia qualify its interpretation. The long-GBP forward's USD payoff per GBP is $S_{t+1}-F_t$; the log difference $s_{t+1}-f_t$ is not a funded simple return. Reversing both quotes reverses these log differences.

## Timing and distinct evidence
Verify the original BoE series and actual termination date locally; the inherited design requests a forward sample ending in 2021 and the following spot endpoint. Month-end observations approximate settlement and are not executable trades. Exclude missing calendar pairs instead of compressing time. Published G10 gross carry is a separate cross-sectional payoff; document portfolio sign and normalization, and use net only as documented sensitivity. Use common monthly dates, dependence-aware uncertainty and a distinct, explicitly approved fallback if the actual quotes cannot be obtained.

## Research checks

Before estimation verify outright versus points, quote orientation, fixing and outcome dates; audit rights and actual coverage. Do not splice observed and synthetic forwards or infer G10 carry from a bilateral regression.
