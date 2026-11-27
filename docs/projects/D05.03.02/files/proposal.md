---
title: "The COS Method for Pricing Options with Non-Gaussian Returns"
subtitle: "Research proposal | D05.03.02"
---

**Derivatives · Numerical pricing and exotics · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Cosine expansion replaces inversion by a finite series of payoff coefficients and characteristic-function values. Rare jumps can make a visually converged series inaccurate because important probability mass lies outside the approximation interval. The study examines interval width and series length separately.

## Research question

When does COS pricing achieve a given error tolerance faster than direct Fourier quadrature, and which truncation choices fail for non-Gaussian returns?

## Economic mechanism

For $X=\log(S_T/K)$ on $[a,b]$, the COS frequencies are $u_j=j\pi/(b-a)$. Increasing the term count does not remove omitted tail contributions.

## Research design

Compare COS and quadrature for BSM and Merton across the prescribed expiries, strikes and jump intensities. Vary interval width and term count separately, using independent Gaussian and Poisson-mixture reference prices.

Inspect short maturity, rare jumps and deep strikes before asserting convergence. A wider interval may require more terms; do not claim universal exponential convergence.

\newpage

## Required exhibits

Convergence/error heatmaps; benchmark reference checks; time-versus-error curves; failure-case table and reproducible code.

## Minimum viable thesis

BSM and Merton, independent analytic/mixture references, COS and quadrature with convergence and fair runtime comparison.

## Scope and feasibility

Avoid selecting a reference from the same COS implementation. Check tail width separately, do not claim universal exponential convergence. Timing includes coefficient setup and uses identical requested precision. Distinct from FFT interpolation study D05.03.01.

**Prerequisites:** Fourier analysis, risk-neutral valuation, numerical integration and Python.

**Optional extension:** Add Heston characteristic-function branch diagnostics and an independent high-precision quadrature reference.

## Milestones

W1-3: derivations; W4-6: reference pricers; W7-9: COS and tests; W10-12: error/runtime grid; W13-16: writing and replication.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
