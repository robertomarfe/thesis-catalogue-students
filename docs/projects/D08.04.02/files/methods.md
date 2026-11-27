---
title: "Focused methods — Designing Cost-Constrained Tail Risk Hedges"
subtitle: "D08.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Feasibility and payoff
Use one stock plus financed net premium; an unspent budget is not a cost. Protective put overlay is $a(K_p-S_T)^+$; a put spread subtracts $a(K_l-S_T)^+$, $K_l<K_p$; a covered collar subtracts a call with quantity no greater than stock held. The net premium may be negative; record it rather than forcing the budget to bind.

## Loss and evaluation
Price legs under a coherent Q law and evaluate $L=1-W_T/S_0$ under P. ES at 95 percent is the average upper five-percent loss mass, with correct boundary weights. Higher Q volatility is an insurance-cost scenario, not by itself an identified variance premium. Specify the P jump drift consistently with the declared mean.

## Research checks

Separate single-horizon synthetic choice from historical rolling strategies. Verify equal net wealth, budget and extreme-spot payoff limits; report cost, expected return, tail protection, upside and paired uncertainty.
