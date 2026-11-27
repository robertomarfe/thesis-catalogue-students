---
title: "Focused methods — Deep Hedging with Transaction Costs"
subtitle: "D04.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Objective and information
Map $(\log(S_i/K),T-t_i,h_{i-1})$ to bounded shares. Use one discounted seller-loss ledger: payoff minus clean premium minus stock gains plus proportional costs. Entropic risk is translation equivariant and $\eta$ has inverse-currency units. Use stable log-sum-exp for empirical evaluation. Future returns are not policy inputs.

## Fair comparison
Use Q for the common premium and P for simulated outcomes; fix decision dates, costs and constraints across neural, delta and band policies. Separate training, validation and test paths before fitting. Retain optimization failures and report training variability rather than selecting a favorable test seed.

## Research checks

The student develops the network, objective, ledger and complete comparison. Report tail loss, turnover, risk objective and stability; in-sample improvement alone is insufficient.
