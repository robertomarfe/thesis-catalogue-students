---
title: "Pricing Commodity Options under Mean Reversion"
subtitle: "Research proposal | D10.02.02"
---

**Derivatives · International finance, FX and commodities · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Mean reversion dampens the effect of current shocks on distant delivery prices. Commodity options therefore depend on both option expiry and underlying delivery, even when the initial forward curve is held fixed. This experiment isolates that mechanism from curve fitting.

## Research question

How does mean reversion affect the maturity pattern of option prices on commodity forwards, holding the initial forward curve fixed?

## Economic mechanism

With $dF(t,T)/F(t,T)=\sigma e^{-\kappa(T-t)}dW_t^{\mathbb Q}$, the expiry variance is $\int_0^u\sigma^2e^{-2\kappa(T-t)}dt$.

## Research design

Use the specified flat initial forward, volatility, maturity and delivery grid. Compare matched spot diffusion volatility and matched one-year forward variance. Price European options on F(u,T) analytically and by exact Gaussian simulation, preserving expiry versus delivery and deterministic rates.

Check the constant-volatility limit, separate expiry from delivery and hold forward/discount fixed. Use independent seeds, report sampling error and keep both matching designs distinct.

\newpage

## Required exhibits

Formula checks, option price/error table, expiry-delivery heatmaps, volatility term structures, matched-variance comparison.

## Minimum viable thesis

One-factor derivation, two matching designs, analytic/Monte Carlo agreement and economic interpretation of delivery lag; two-factor extension optional. Distinct from D10.01.02, which studies the forward curve itself.

## Scope and feasibility

Use deterministic rates and European payoff on F(u,T), not S_u unless u=T. Ensure Q drift and initial curve are consistent; forward and futures equality needs deterministic rates. Gaussian model is an illustrative positive-price model, not calibrated oil data.

**Prerequisites:** Gaussian processes, risk-neutral pricing, Black formula, Monte Carlo.

**Optional extension:** With lawful historical options and futures quotes, estimate volatility term structure and test one-factor restrictions.

## Milestones

W1-3: derive dynamics and pricing; W4-6: implement analytic benchmark and simulation; W7-9: maturity grids and matched comparisons; W10-12: robustness and optional second factor; W13-16: write and reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
