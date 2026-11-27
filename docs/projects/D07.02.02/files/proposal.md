---
title: "Interest Rate Options under Gaussian and Square-Root Dynamics"
subtitle: "Research proposal | D07.02.02"
---

**Derivatives · Fixed income and interest rates · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Gaussian and square-root models can agree on today's curve and one liquid at-the-money bond option while implying different tails and sensitivities. A controlled comparison isolates those distributional implications rather than confounding them with different fitted term structures.

## Research question

After matching initial bond prices and at-the-money option volatility approximately, how do Gaussian and square-root dynamics affect out-of-the-money bond options and their Greeks?

## Economic mechanism

For option expiry $u<T$, $C_0=P(0,u)\mathbb E^{\mathbb Q^u}[(P(u,T)-K)^+]$.

## Research design

Use the common flat curve and prescribed Gaussian/CIR parameters. Match the curve via deterministic shifts and solve for one CIR ATM price match, then compare other strikes and maturities. Keep stochastic parameters and contractual strike fixed for curve bumps, updating only the deterministic curve fit.

Freeze the ATM match before comparing other strikes; report domain and uncertainty rather than forcing implied volatilities for zero prices. Distinct from A05.01.01 physical transition estimation.

\newpage

## Required exhibits

Curve fit table; parity and MC error table; option price and implied volatility plots; Greek and tail-scenario comparisons. Bump-convergence table and sensitivity per basis point; document unmatched prices and structural zeros.

## Minimum viable thesis

Two affine models on the same synthetic curve, analytic/Monte Carlo cross-check, one ATM price match and option smile comparison; compare at least one ATM and one non-negligible OTM parallel zero-yield sensitivity with strike and stochastic parameters frozen and deterministic curve fitting updated. Report convergence in bump size, pricing-domain failures and unmatched cases. Distinct from A05.01.01 (physical rate dynamics).

## Scope and feasibility

Match curves and ATM price before attributing differences to diffusion. Shifted CIR need not have positive total rates. Do not infer Q parameters from P estimates. Use CIR boundary/Feller diagnostics; distinguish bond option from caplet.

**Prerequisites:** Stochastic calculus, affine processes, fixed-income pricing, Python.

**Optional extension:** Compare caplets or Jamshidian swaption decomposition under one-factor dynamics.

## Milestones

W1-3: affine derivations; W4-6: reference pricers; W7-9: matching and validation; W10-12: scenarios and Greeks; W13-16: write and reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
