# Research plan | A05.01.03

## Study design and independent work

Use identical dates for comparisons, rate-bin diagnostics and a predeclared mean/variance scoring convention. Distinguish this variance-target experiment from A05.01.01 density forecasting.

## Required tasks

1. Audit rate conversion, zero/negative episodes, sample and time steps.

2. Estimate P dynamics, examine conditional variance by rate bins and standardized residuals; verify CIR conditional moments by simulation.

3. Freeze expanding estimation procedure, forecast squared rate innovations and score QLIKE/MSE; report errors by rate regime.

4. Fit yield-on-short-rate empirical loadings on training dates; test implied relative conditional variances and residual covariance on held-out dates.

5. Compare against direct rolling yield variance forecasts and sensitivity to sampling frequency; quantify measurement error from bill proxy.

## Required exhibits

Transition estimates, conditional variance curves, forecast losses and rate-bin diagnostics, yield residual variance/rank table and exclusion report.

## Robustness

CIR near zero can be problematic with noisy bill quotes; no silent clipping or shifting. Actual rate innovations are not observed; squared forecast residuals are noisy proxies and mean-model misspecification matters. Empirical yield loadings are not Q pricing parameters. Distinct from A05.01.01 transition fit and A05.01.02 rank-one mean reconstruction.

## Minimum viable thesis

Common-positive sample exact-transition Vasicek/CIR, conditional variance forecasts against rolling benchmark, rate-bin and two-maturity yield-volatility diagnostics.

## Optional extension

Estimate a two-factor model or a shifted square-root process with shift selected on training only; compare likelihood and conditional variance.

## Prerequisites

Stochastic processes, likelihood, fixed income and time-series forecasting.

## Thesis outline

1. Affine short-rate models;

2. Conditional moments and data;

3. Estimation;

4. Volatility forecasts and yield restrictions;

5. Limitations.

## Milestones

W1-3: derive conditional moments; W4-6: align rates and curves; W7-9: fit and validate transitions; W10-12: forecast and cross-maturity diagnostics; W13-16: write and audit.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
