---
title: "One-Factor versus Two-Factor Models for Interest Rate Hedging"
subtitle: "Research proposal | D07.04.02"
---

**Derivatives · Fixed income and interest rates · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Yield-curve changes can span more than one empirically important direction. Additional hedge instruments may remove a second factor, but unstable estimated loadings and large notionals can offset the benefit. Test risk reduction on genuinely subsequent curve shocks.

## Research question

How much additional interest rate risk can a two-factor hedge remove relative to a one-factor hedge, after controlling for estimation error and gross notional?

## Economic mechanism

If $L_k$ contains training-estimated factor loadings and $D$ the hedge sensitivity columns, choose $h$ to target $L_k^\top(d+Dh)=0$.

## Research design

Use the prescribed monthly GSW grid and rolling 120-month PCA of adjacent changes. Hedge the equal-market-value 7/10-year zero portfolio with 2-year alone or 2/5-year zeros. Freeze each estimated hedge before the subsequent curve shock; reprice at fixed maturities and report gross notional.

Do not treat physical PCA loadings as risk-neutral parameters. Unlike D07.01.02, compare statistical factor spanning with zero-bond hedges rather than single-curve swap DV01.

\newpage

## Required exhibits

Factor loading plots, hedge notional and conditioning diagnostics, residual P&L and variance reduction table, parallel/twist shock scenarios.

## Minimum viable thesis

GSW panel, rolling PCA, one- and two-factor zero-bond hedges, held-out shock repricing and notional/condition diagnostics. Distinct from D07.01.02, which focuses on swap DV01.

## Scope and feasibility

Yield curves are fitted and revised; basis and liquidity excluded. No swap, carry, roll, margin or tradable performance claim. Compare identical target and shock samples. A second factor need not improve held-out risk when estimated.

**Prerequisites:** Fixed income, linear algebra, PCA, Python and regression.

**Optional extension:** Use coupon-bond cash flows or a two-factor Gaussian model with separately specified Q parameters; repeat with ECB curves.

## Milestones

W1-3: PCA and duration; W4-6: curve acquisition and repricing; W7-9: hedge optimization; W10-12: held-out and stress tests; W13-16: interpretation and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
