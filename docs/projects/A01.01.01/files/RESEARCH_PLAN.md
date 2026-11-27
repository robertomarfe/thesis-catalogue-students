# Research plan | A01.01.01

## Study design and independent work

Use one RF subtraction, common complete dates and separate portfolio panels. Report T, N, K, eigenvalues and failed draws. Re-estimate both regression passes in joint date blocks; do not interpret a rejected joint hypothesis as proof of inefficiency.

## Required tasks

1. Summarize excess return, volatility and beta across 5x5 portfolios; plot mean return and market beta heatmaps.

2. Estimate time-series alpha/beta, HAC intervals, RMSE of alphas and GRS joint test; report covariance condition.

3. Estimate cross-sectional beta price and intercept using two-pass regressions; use joint date-block bootstrap that re-estimates betas and premia.

4. Compare predicted and observed means against the CAPM restriction, reporting economic magnitudes and uncertainty.

5. Repeat across subperiods and industries; use FF3 as a limited diagnostic for omitted exposures.

## Required exhibits

Beta/alpha heatmaps, GRS and robust joint test table, security market line scatter, pricing error summary, beta uncertainty and sample split results.

## Robustness

Use a common month index and risk-free series; test equal-weighted size/value portfolios separately, not mixed with value-weighted series. Do not interpret GRS rejection as a unique rejection of rationality; market proxy and joint hypothesis matter. Bootstrap entire time slices jointly; report near-singular matrices.

## Minimum viable thesis

One full 25-portfolio panel, derivation, alpha tests, security market line and cross-sectional inference with a separate industry or temporal robustness panel.

## Optional extension

Use rolling or conditional betas, but retain the unconditional CAPM as the primary object.

## Prerequisites

OLS, multivariate statistics, portfolio theory, Python statsmodels/NumPy.

## Thesis outline

1. Mean-variance theory and CAPM;

2. Testing restrictions and inference;

3. Test assets and data;

4. Time-series and cross-sectional evidence;

5. Interpretation.

## Milestones

W1-3: CAPM and test derivations; W4-5: construct portfolio panel; W6-8: estimate alpha/beta and GRS; W9-12: two-pass and bootstrap; W13-16: robustness and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
