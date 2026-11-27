---
title: "Option Pricing under Model Misspecification: Implications for Prices and Hedging"
subtitle: "Research proposal | D01.01.02"
---

**Derivatives · Vanilla pricing and surfaces · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

A model can match one liquid quote while assigning different risks to other strikes. In a jump-diffusion market, a stock position hedges infinitesimal price changes but cannot generally offset a finite jump. This study asks whether an ATM-calibrated diffusion gives useful prices and hedge positions away from its calibration contract, and isolates the role of discrete rebalancing from residual jump exposure.

## Research question

How does fitting Black-Scholes to an at-the-money jump-diffusion price affect held-out option pricing and delta hedging across strikes and jump intensities?

## Economic mechanism

Let $\Delta$ denote model delta and $J$ a jump multiplier. A finite jump gives the residual $C(SJ)-C(S)-\Delta S(J-1)$, which is not generally zero even with continuous rebalancing between jumps.

## Research design

Use compensated Merton jump-diffusion prices at two expiries and five strikes, varying intensity from zero to 1.5 per year. Calibrate a Black–Scholes volatility to one ATM quote per maturity; test all other strikes. Simulate common physical paths at daily and weekly rebalancing frequencies, including an alternative physical jump intensity.

Freeze the ATM definition and calibration date. Record held-out prices separately from matched-path hedge losses. Build the cash ledger before changing physical jump intensity; do not equate a smaller time step with complete jump-risk replication.

\newpage

## Required exhibits

IV and pricing-error panels, calibration diagnostics, hedge P&L RMSE/tails, jump-conditioned figures and Monte Carlo uncertainty.

## Minimum viable thesis

Verified jump pricer and BSM limit, two intensities, two maturities, held-out strikes, matched-path P&L for both hedges and two grids.

## Scope and feasibility

Model delta is not necessarily the variance-minimizing incomplete-market hedge. No claims of empirical accuracy or exact jump-risk replication. Distinguish initial valuation bias from hedge performance; if using differing initial prices report separately. Keep D01.01.01 terminal sensitivities and D04.01.01 diffusion convergence separate.

**Prerequisites:** Risk-neutral valuation, BSM, Poisson processes, stochastic calculus and Python simulation.

**Optional extension:** Compare the minimum-variance local hedge or a second traded option as a jump-risk hedge under a documented Q/P specification.

## Milestones

W1-3: Merton model and conditional pricing; W4-6: pricer and inversion tests; W7-9: cross-strike calibration; W10-12: P-path hedge experiments; W13-16: sensitivity and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
