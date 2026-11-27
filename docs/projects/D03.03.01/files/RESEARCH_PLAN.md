# Research plan | D03.03.01

## Study design and independent work

Use the specified simulated filter check, compare effective sample sizes and independent seeds, then freeze the model-selection protocol. Separate uncertainty from latent states, parameters and finite particle budgets.

## Required tasks

1. Validate filter on simulated data; compare 1,000/5,000 particles, independent seeds and effective sample size.

2. Estimate both models and plot filtered, not smoothed, variance at forecast origin.

3. Generate one-day density forecasts and five-day variance forecasts using observed data through each origin.

4. Compare mean negative log score, QLIKE and MSE, paired block-bootstrap uncertainty; inspect tail calibration.

5. Repeat with Student-t GARCH and optionally SV, different particle counts and crisis subperiods.

## Required exhibits

Simulation filter diagnostics, fitted parameter table, forecast plots, common-date score table and predictive quantile coverage.

## Robustness

Approximate log-square estimation is not exact SV maximum likelihood. Use filtering and sequential predictive likelihood, never smoothed states for forecasting. Daily squared returns are noisy variance proxies; enforce common units and holdout dates. Particle likelihood noise and weak identification must be reported.

## Minimum viable thesis

Simulated filter check, Gaussian SV and GARCH with honest chronological evaluation of log score and variance. No need for SV to win; distinct from D03.02.02's fractional memory focus.

## Optional extension

Leverage SV with correlated shocks, or Bayesian posterior predictive distributions with parameter uncertainty.

## Prerequisites

Time-series likelihood, Monte Carlo, state-space methods, Python.

## Thesis outline

1. Observation-driven versus latent models;

2. State-space estimation and filtering;

3. Data and evaluation;

4. Forecast results;

5. Model risk.

## Milestones

W1-3: state-space theory; W4-6: filter tests and cleaning; W7-9: parameter estimation; W10-12: predictive scores and robustness; W13-16: report.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
