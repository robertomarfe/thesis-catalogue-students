---
title: "Focused methods — Macroeconomic Expectations and the Predictability of Bond Returns"
subtitle: "A05.03.03 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Survey vintage and timing
A next-four-quarter growth proxy from mean levels should use a documented same-vintage base and horizon: $g=\log(\widehat X_{t+4|t}/\widehat X_{t|t})$ if those exact forecast horizons exist. This is a growth rate of mean forecasts, not necessarily the mean of individual growth rates. Do not use a later-revised base. Join by actual release before portfolio formation; same-day releases require an established timing order.

## Excess return and forecast test
Use $rx^{(n)}_{t+4}=ny_t(n)-(n-1)y_{t+4}(n-1)-y_t(1)$ for quarterly origins and annual holding horizon. Only matured targets enter training; use the same realized targets for the yield-only and augmented regressions. Account for quarterly annual overlap (baseline HAC at least three lags), training-stage factor estimation and revisions of curve data. Survey association is not a structural shock.

## Research checks

Require release and horizon metadata before estimation. If necessary use the original minimum of one released horizon and two maturities; do not substitute dispersion for expected growth. Label the result pseudo-OOS unless vintages are truly reconstructible.
