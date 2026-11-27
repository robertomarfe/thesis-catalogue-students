---
title: "Exchange Rate Jumps and Currency Option Smiles"
subtitle: "Research proposal | D10.04.02"
---

**Derivatives · International finance, FX and commodities · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

FX jump risk changes the relative prices of calls and puts in the wings. Holding the forward and the ATM option price fixed provides a controlled comparison of smile asymmetry and curvature instead of confounding jump effects with the overall volatility level.

## Research question

Holding the forward and ATM option price fixed, how do jump frequency, direction and size affect FX smile slope and wing prices?

## Economic mechanism

Under domestic Q, $\log(S_T/F)=-\sigma^2T/2-\lambda T\zeta+\sigma W_T+\sum_{k=1}^{N_T}J_k$, with $\zeta=E[e^J-1]$.

## Research design

Use the prescribed domestic-Q jump scenarios and delivery grid. Match each ATM option price by a feasible nonnegative diffusion volatility; flag impossible scenarios. Compare smiles at fixed log-forward moneyness and independently simulate compound-Poisson terminal values.

Check martingale, parity, zero intensity, truncation including stock-weighted tail, ATM feasibility and independent Monte Carlo. Report infeasible cases; no observed smile claim.

\newpage

## Required exhibits

Martingale and parity tests; ATM calibration table; smiles by jump scenario; wing error/identification plots.

## Minimum viable thesis

Domestic-Q Merton mixture, matched ATM scenarios, skew/curvature comparisons and independent MC check. Distinct from equity jump pricing and diffusion FX pricing D10.04.01.

## Scope and feasibility

P jump estimates do not identify Q jump risk. Compare same forward and maturity; do not naively invert S under the same pricing measure. No claim to empirically explain market FX risk reversals without quotes.

**Prerequisites:** FX derivatives, jump processes, implied volatility and Python.

**Optional extension:** Compare symmetric versus asymmetric double-exponential jump models or multi-maturity synthetic calibration.

## Milestones

W1-3: derivation; W4-6: mixture/MC; W7-9: calibration grid; W10-12: wing/identification checks; W13-16: writing and replication.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
