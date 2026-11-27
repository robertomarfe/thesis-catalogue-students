---
title: "Focused methods — Protective Puts and the Cost of Crash Insurance"
subtitle: "D08.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Premium financing
Holding one stock and borrowing the put premium gives $W_T=S_T+(K-S_T)^+-P_0e^{rT}$ from net initial wealth $S_0$. This is not the repeated PPUT return. Index history depends on roll timing, strike, premium and methodology; it does not reveal individual option premiums.

## Insurance value
Compare realized returns and tail loss on common months versus a lagged risk-matched stock-cash allocation. Drawdown depends on the wealth path; expected shortfall depends on return horizon. In the synthetic supplement price under Q and simulate under P, not as a replacement for missing index data.

## Research checks

Unlike D08.04.02, this is historical rolling insurance evaluation. Gate remains blocked. Report achieved risk and uncertainty; simulation-only redesign needs explicit approval.
