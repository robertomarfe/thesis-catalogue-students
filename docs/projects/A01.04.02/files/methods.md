---
title: "Focused methods — Principal Components versus Observable Asset Pricing Factors"
subtitle: "A01.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Covariance versus traded factors

Compute $V_k$ from the covariance of centered training returns. Apply those weights to raw excess returns $x_t$ at all dates, not to returns demeaned by a test mean (which would remove their premia). Eigenvector signs are arbitrary but factor exposures and signs must transform consistently. Report variance reconstruction using the frozen subspace, separately from expected-return pricing.

## Pricing evaluation

Estimate a candidate normalized SDF $m_t=1-b^\top(f_t-\mu_f)$ using training means and common weights. Freeze $V_k,b,\mu_f$ for later moment evaluation. For two-pass pricing of held-out portfolio definitions, estimate their betas from pre-test returns to the fixed factors; never use future means to form forecasts. A descriptive later regression alpha is a separate diagnostic. Shared underlying stocks limit independence claims.

## Research checks

Freeze factor dimensions, weights, means and model selection before the test. Audit date and asset holdouts separately, report factor return scaling and rank, and retain common pricing moments. Optional OSAP alternative requires its own access verification.
