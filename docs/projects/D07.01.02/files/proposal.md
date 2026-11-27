---
title: "Interest Rate Swaps and the Management of Duration Risk"
subtitle: "Research proposal | D07.01.02"
---

**Derivatives · Fixed income and interest rates · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

A payer swap can offset the duration of a long fixed-income portfolio, yet a single parallel sensitivity leaves exposure to twists and convexity. Compare a single swap hedge with a key-rate hedge on identical historical curve shocks at fixed cash-flow schedules.

## Research question

How much interest rate risk can a stylized payer swap eliminate from a government bond portfolio, and when do key-rate hedges outperform a single DV01 hedge?

## Economic mechanism

For target signed DV01 $d_B$ and one unit swap sensitivity $d_S$, the neutral hedge quantity is $h=-d_B/d_S$ when $d_S\ne0$.

## Research design

On each eligible GSW date construct the prescribed par bonds and swaps; use the next day's curve as an instantaneous shock. Freeze coupons, cash-flow times and original positions. Compare one swap and the prescribed two-swap key-rate hedge, keeping shocks and notional constraints consistent.

Report initial zero PV for swaps, matched shocks and risk reduction net of exposure sign mistakes. Distinct from D07.04.02: swap DV01/key-rate hedging rather than PCA zero-bond spanning.

\newpage

## Required exhibits

Curve data audit, hedge ratios, P&L distributions, risk reduction by regime and shock type, sensitivity and notional tables, validated pricer.

## Minimum viable thesis

Validated par valuation, signed DV01 hedge, exact shock repricing on a verified daily GSW sample and comparison of one- and two-instrument residual risk.

## Scope and feasibility

Use common dates; no rolling live-position claim, carry or funding P&L. Government zero curve is not OIS or term forward curve. Label hedge as a historical shock replay using synthetic contracts. Repeat with smaller bump sizes, maturity grid and stress dates. No execution costs, collateral or basis included.

**Prerequisites:** Fixed-income pricing, linear algebra, Python and basic portfolio risk analysis.

**Optional extension:** Implement genuine rolling coupon/reset schedule with carry and aging, or compare euro government proxy curves; verify separate curves before claiming swap-market evidence.

## Milestones

W1-3: study curve/swap conventions; W4-6: acquire GSW and validate pricer; W7-10: compute hedge ratios and shock P&L; W11-13: stress and sensitivity; W14-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
