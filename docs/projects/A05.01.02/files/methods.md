---
title: "Focused methods — Can One-Factor Interest Rate Models Explain the Dynamics of the Yield Curve?"
subtitle: "A05.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Rank restriction
For $m$ maturities and $n$ dates, form the $n\times m$ matrix $Y$. With maturity-specific intercepts and a scalar factor, centered $Y$ has rank at most one absent measurement noise. Vasicek imposes $b_j=(1-e^{-\kappa_Q\tau_j})/(\kappa_Q\tau_j)$ for positive $\kappa_Q$. Conditional on $b$, estimate date scores by projection. An unconstrained intercept makes this a loading-shape diagnostic, not a complete no-arbitrage calibration.

## Held-out reconstruction
Estimate the training mean and PCA eigenspace only on training dates; freeze them. Same-date reconstruction using the whole vector is not a temporal forecast. With a single observed two-year yield, estimate its mapping to the remaining maturities using training observations only. Use comparable bp errors, maturity-specific residual covariance and rank diagnostics.

## Research checks

Report unrestricted PCA as a rank-matched comparator. Separate same-date reconstruction from held-out maturity prediction; do not claim the fitted loading uniquely identifies physical or risk-neutral dynamics.
