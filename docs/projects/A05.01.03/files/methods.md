---
title: "Focused methods — Interest Rate Volatility and the Performance of Affine Term Structure Models"
subtitle: "A05.01.03 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Conditional variance
Vasicek yields $V_h=\sigma^2(1-e^{-2\kappa h})/(2\kappa)$. CIR adds a term linear in the current rate, as in the proposal. Estimate conditional means consistently and define a variance outcome from squared forecast innovations, not squared levels. Score positive variance forecasts using a common loss such as $\log V+e^2/V$. Respect irregular calendar gaps.

## From rate to yield risk
If $y_j=a_j+b_j r$, conditional innovation covariance is $bb^\top V_h$ for $b=(b_1,\ldots,b_m)^\top$. This is a one-factor restriction. Physical rate estimates do not identify the risk-neutral loadings; either use separately documented illustrative loadings or a training-only empirical projection. Interpret unexplained covariance rather than forcing all observed yield shocks into the short-rate factor.

## Research checks

Use identical dates for comparisons, rate-bin diagnostics and a predeclared mean/variance scoring convention. Distinguish this variance-target experiment from A05.01.01 density forecasting.
