# Research plan | A11.03.01

## Study design and independent work

Use quarterly parameters and same-quarter consumption/payoffs; preserve the original broad bounds and fixed moments. Report scaling, HAC bandwidth, effective rank and convergence. Validate independently on a designed simulation before empirical estimation; do not select moments after viewing rejection.

## Required tasks

1. Derive moments and analytic Jacobian; validate on simulated data with known SDF and returns generated to satisfy moments, check optimizer recovery.

2. Estimate base/expanded models by multistart identity and two-step HAC GMM, with moment scaling documented and common sample.

3. Compare parameter profiles, moment residuals and sampling intervals; report rank, condition number, weight regularization and J test only when its assumptions credible.

4. Add prespecified lagged instrument and alternative HAC bandwidth; compare conclusions using block bootstrap or simulation to illustrate weak-ID/finite-sample distortion. Separate model misspecification from estimation instability.

## Required exhibits

Moment and Jacobian diagnostics, objective profile/contours, estimates with conditional inference caveats, pricing errors by asset/instrument and weighting matrix comparison; J table where defensible. Reproducible code and real return alignment test.

## Robustness

Bill proxy is ex-post real return, not a known real risk-free rate. No division by beta-normalized scale without retaining identifying gross moment. Verify moment count, positive-semidefinite HAC covariance and Jacobian rank; pseudoinverse/regularization changes usual J reference distribution. Document revised consumption and quarterly timing, crisis sensitivity, and no selection of moments based on rejection.

## Minimum viable thesis

Small overidentified CRRA GMM with verified data, two weight schemes and two fixed moment sets, simulation sanity check, profile/Jacobian and pricing-error diagnostics; valid conclusions possible even if standard asymptotics fail.

## Optional extension

Compare a parsimonious linear-factor SDF under identical moment sets, or weak-identification-robust inference after core completion.

## Prerequisites

CRRA utility and SDFs, nonlinear optimization, GMM/HAC, matrix algebra and Python SciPy/statsmodels.

## Thesis outline

1. Euler restrictions and consumption SDF;

2. GMM and identification;

3. Data and simulation check;

4. Weight/moment sensitivity;

5. Specification and inference limitations.

## Milestones

W1-3: derive moments and data gate; W4-6: validate real returns and synthetic GMM; W7-10: estimate baseline and expanded moments; W11-13: profiles, inference and robustness; W14-16: write and reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
