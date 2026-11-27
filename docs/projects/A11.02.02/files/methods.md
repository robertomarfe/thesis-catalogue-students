---
title: "Focused methods — Hansen-Jagannathan Distance and the Comparison of Asset Pricing Models"
subtitle: "A11.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Projection onto the pricing restrictions

For column $X$ of gross returns with unit prices and candidate $m$, seek a correction $h$ minimizing $E[h^2]$ subject to $E[hX]=-g$. Decompose $h$ into its projection onto the payoff span and an orthogonal component. For full-rank $G=E[XX^\top]$, the minimum correction is $h=-X^\top G^{-1}g$, so $d^2=E[h^2]=g^\top G^{-1}g$. This is an uncentered second moment, not a covariance. A singular matrix calls for an independent basis or an explicit range check; a ridge defines a different metric. The adjusted kernel need not be positive.

Fit $m=a-b^\top f$ using training pricing restrictions. Evaluate frozen coefficients on common held-out payoffs with the same $G$ for all candidates on that panel. Negative realizations and raw errors remain important diagnostics.

## Research checks

Construct gross returns including the actual monthly bill, not excess returns with unit prices. Distinguish train and holdout metrics and apply common conditioning rules; paired time-block resampling should refit the training step and evaluate common holdout draws.
