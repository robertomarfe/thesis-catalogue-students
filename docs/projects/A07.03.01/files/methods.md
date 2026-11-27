---
title: "Focused methods — Skewness Risk and the Cross-Section of Equity Returns"
subtitle: "A07.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Quadratic SDF and exposures
For excess returns, $E[m r_i^e]=0$. A quadratic approximation $m=a-bx-cx^2$ connects expected returns to covariances with $x$ and $x^2$ after normalizing by $E[m]$. Orthogonalize $x^2$ on a constant and $x$ within each past window before estimating $r_i^e=\alpha_i+\beta_i x+\gamma_i z+e_i$. This is not identical to standardized coskewness $E[(r_i^e-E r_i^e)x^2]/(\sigma_i\operatorname{Var}(x))$; report both with documented scaling.

## Pricing design
Estimate Fama-MacBeth monthly cross-sectional slopes on predetermined exposures, comparing the same assets and evaluation dates. Standardize using only the relevant past cross section if prescribed. Report beta/coskewness correlations and joint-date bootstrap uncertainty, re-estimating past moments and exposures. A significant slope is not proof of a structural quadratic SDF.

## Research checks

Do not remove extreme days based on their effect on significance. Verify that the daily and monthly portfolio labels match, that the market is excess return, and that generated-regressor uncertainty is recognized.
