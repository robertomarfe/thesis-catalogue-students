---
title: "Black versus Bachelier Pricing in Low-Rate Environments"
subtitle: "Research proposal | D07.03.01"
---

**Derivatives · Fixed income and interest rates · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Rate options can be quoted in normal, lognormal or shifted-lognormal volatility. Equal numerical volatility inputs do not represent equal economic uncertainty. Compare the models after matching a common ATM premium, including rate environments in which unshifted Black is not admissible.

## Research question

After matching an ATM premium, how do Black, shifted Black and Bachelier pricing differ across strikes and rate levels?

## Economic mechanism

With annuity $A$ and normal volatility $\sigma_N$, payer PV is $A[(F-K)\Phi(d)+\sigma_N\sqrt u\,\phi(d)]$, $d=(F-K)/(\sigma_N\sqrt u)$.

## Research design

Use the specified forward-rate regimes, expiry/strike grid and normal vol. Match displaced Black ATM prices for each declared shift where feasible; omit inadmissible unshifted Black cases with a reason. Compare prices, fixed-annuity delta/vega and independent quadrature.

Keep infeasible targets and strikes in a domain map. Distinguish rate-volatility pricing convention from D07.03.02 one-factor model calibration and curve risk.

\newpage

## Required exhibits

ATM conversion table; price and common-unit smile plots; domain/failure map; delta and vega comparisons.

## Minimum viable thesis

Three rate regimes including negative, normal versus shifted Black matched ATM, parity and independent price/Greek checks.

## Scope and feasibility

Do not compare normal bp vol directly with percentage Black vol. Shift is a modeling choice, not empirical identification. Same premium and annuity required for fair comparison. Quoted convention does not determine dynamics of the underlying yield curve.

**Prerequisites:** Fixed income, option pricing, normal distribution, numerical roots and Python.

**Optional extension:** Use optional GSW initial curves for annuity construction; caplet/swaption conventions and joint shift calibration.

## Milestones

W1-3: pricing derivations; W4-6: pricers and inversions; W7-9: grids; W10-12: Greeks and curve effects; W13-16: reproducibility and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
