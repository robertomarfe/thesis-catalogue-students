---
title: "Focused methods — Option Pricing under Model Misspecification: Implications for Prices and Hedging"
subtitle: "D01.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Two measures and a common contract
Under the pricing measure $\mathbb Q$, let jump multiplier $J=e^Y$ with $Y\sim N(m,s_J^2)$, intensity $\lambda_Q$, and $a_Q=\mathbb E^\mathbb Q[J]$. With independent Brownian and Poisson shocks,
$$\frac{dS_t}{S_{t-}}=(r-q-\lambda_Q(a_Q-1))dt+\sigma dW_t^Q+(J-1)dN_t^Q.$$
Conditional on $n$ jumps over $\tau$, log variance is $\sigma^2\tau+ns_J^2$ and mean stock is $F\exp[-\lambda_Q\tau(a_Q-1)]a_Q^n$. Derive the price by weighting conditional lognormal call expectations; the stock-weighted Poisson tail matters as well as the count tail. Freeze the ATM convention (spot or forward) and the volatility fitted at inception for the benchmark hedge. A model delta holds its parameters fixed.

## Wealth and hedge loss
Under $\mathbb P$, specify expected total return and jump intensity separately; the pricing intensity is not an estimate of physical frequency. Here $q=0$ in the baseline. If a replicating portfolio of value $V_j$ holds $h_j$ shares just after rebalancing, cash is $B_j=V_j-h_jS_j$. Its next value is
$$V_{j+1}=B_je^{r\Delta t}+h_jS_{j+1}.$$
Both strategies start at the same true $\mathbb Q$ option premium. Define discounted loss of the short option as $e^{-rT}[(S_T-K)^+-V_T]$. Report loss conditional on a jump and on no jump as well as unconditional loss. Model delta is not necessarily the minimum-variance hedge in an incomplete market. Do not refit implied volatility using held-out strikes or future paths.

## Research checks

Freeze the ATM definition and calibration date. Record held-out prices separately from matched-path hedge losses. Build the cash ledger before changing physical jump intensity; do not equate a smaller time step with complete jump-risk replication.
