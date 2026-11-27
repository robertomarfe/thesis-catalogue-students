---
title: "Quanto Options and Currency Risk in International Derivatives"
subtitle: "Research proposal | D06.04.02"
---

**Derivatives · Numerical pricing and exotics · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Fixing currency conversion removes direct exchange-rate exposure at settlement but changes the pricing-measure equity drift. The quanto correction depends on risk-neutral equity–FX covariance. The study separates fixed, random and spot conversion, and evaluates both price and equity-delta exposure.

## Research question

How do FX volatility and equity-FX correlation affect quanto prices and deltas relative to ordinary foreign options converted at spot?

## Economic mechanism

For $X$ domestic currency per foreign unit, the domestic pricing-measure equity drift is $r_f-q-\rho\sigma_S\sigma_X$. It follows from the domestic value $XS$ earning the domestic risk-free rate including dividends.

## Research design

Use the specified EUR/USD convention, fixed conversion and correlated Gaussian terminal law. Compare analytic and simulated quanto prices and deltas at two FX volatilities and at least three correlations, including random-conversion and spot-converted foreign controls.

Check the discounted domestic stock martingale and currency units. Hold contractual conversion fixed for delta. Validate random conversion by numeraire invariance; do not use physical correlation as risk-neutral calibration.

\newpage

## Required exhibits

Price and delta curves, quanto adjustment heatmap, domestic/foreign pricing parity and MC error table. Spot-delta comparison in common domestic currency per unit of foreign spot, including numerical validation.

## Minimum viable thesis

Analytic and Monte Carlo quanto call prices and spot deltas for two FX volatilities and three equity–FX correlations at one maturity; validate the analytic spot delta by a central bump and a pathwise or independently simulated estimate, holding the fixed conversion rate and FX spot fixed. Include the random-conversion control and the matched spot-converted foreign option price and delta.

## Scope and feasibility

Zero correlation removes drift correction, not discount or fixed-versus-random conversion differences. Reversing X changes sign of diffusion and measure, not just labels. No observed quanto prices; no P correlations used as Q calibration.

**Prerequisites:** Ito calculus, BSM, change of numeraire, Python.

**Optional extension:** Quanto put or basket under stochastic correlations and rate scenarios, retaining consistent currency ledger.

## Milestones

W1-3: currency and measure; W4-6: formulas and MC; W7-9: parity checks; W10-12: sensitivity; W13-16: writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
