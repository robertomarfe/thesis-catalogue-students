---
title: "Covered Interest Parity and Synthetic FX Forward Rates"
subtitle: "Research proposal | D10.03.01"
---

**Derivatives · International finance, FX and commodities · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Covered interest parity links a currency forward to two funded cash accounts, but published monthly money-market proxies need not be synchronized tradable quotes. Construct parity-implied forward points and analyze their sensitivity, without interpreting the result as observed cross-currency basis.

## Research question

How do the level and differential of short-term USD and EUR interest rates shape synthetic EUR/USD forward prices, and how sensitive is the result to rate conventions and proxy choice?

## Economic mechanism

For $S$ in USD/EUR and simple accrual factors $A_d=1+r_d\tau$, $A_f=1+r_f\tau$, $F=S A_d/A_f$.

## Research design

Use the frozen USD/EUR spot series and USD/EUR-area three-month rate proxies, validating actual overlap and availability. Match month-end spot with latest published prior-month averages or the prescribed conservative lag, use simple three-month accrual, and compare actual-calendar and alternative-proxy scenarios if authorized.

Verify quote orientation, rate units, positive accrual, zero initial PV and reciprocal identity. Record availability and exact overlap. No observed basis or executable trade claim.

\newpage

## Required exhibits

Spot and synthetic forward curves/time series, forward points versus rate differential, decomposition and shock table in USD per EUR and USD notionals; precise metadata and timestamp convention. Explicitly state all forward prices are hypothetical rather than observed.

## Minimum viable thesis

Verified spot and rate sources, correct parity and valuation identities, one tenor with historical synthetic points and stress/sensitivity analysis. Fallback to transparent synthetic scenarios if no overlapping rate series; empirical title/claim must then be reviewed.

## Scope and feasibility

Check no negative accrual factors, reciprocal quote conversion and zero initial PV. Test actual calendar accrual versus 0.25 and stale versus contemporaneous monthly averages; non-synchronous observations and proxy funding differences are limitations, not arbitrage. No claim of executable CIP trades or post-crisis deviations.

**Prerequisites:** Fixed income discounting, FX conventions, elementary calculus and Python data manipulation.

**Optional extension:** Use verified daily OIS/term curves or actual traded forward quotes if institutional access is available; then separately measure basis with consistent collateral, timestamps and bid-ask.

## Milestones

W1-3: derive parity and confirm sources; W4-6: construct aligned proxies and validate identities; W7-10: historical decomposition and stress analysis; W11-13: timing/proxy robustness; W14-16: document and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
