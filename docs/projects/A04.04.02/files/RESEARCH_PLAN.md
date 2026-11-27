# Research plan | A04.04.02

## Study design and independent work

Use a release ledger or explicitly pseudo-real-time extra lag; set threshold from fixed rule or past data. Compute exact aging bond return and nominal equity total return; report regime counts, marginal variances, covariance and 2*w_s*w_b*cov contribution with date-block inference and fixed-weight risk decomposition.

## Prespecified implementation

Construct stock total returns and 5y synthetic zero one-month holding returns (2/10y robustness) from GSW; exact remaining maturity and dates, convert log bond return with expm1 before variance comparison. Decision month t: choose latest stress observation from prior month or earlier, actual release strictly before origin and max age declared. STLFSI4 weekly ending Friday; series revised, do not assign observation as release. If only revised histories, conservative lag and pseudo-real-time; NFCI robustness. Pair next-month returns with lagged stress state; fixed >0 baseline, threshold quantile estimated training-only. Use rolling 36/60 month correlation and vol/cov; common-date moving blocks with regime assignment preserved/recomputed as appropriate. Compare 60/40 variance to independence counterfactual using within-state variances, disclose event counts; no causal stress interpretation.

## Required tasks

1. Build discount factors and verify zero-bond holding-return formula against parallel-shock duration approximation.

2. Plot rolling 36/60-month covariance/correlation and volatilities.

3. Split by lagged stress above zero and training-sample quantiles; estimate conditional covariance and correlation with paired block bootstrap.

4. Compare 60/40 portfolio risk to an independence counterfactual across regimes.

5. Test robustness by bond maturity, alternative NFCI, lag and pre/post-2008 or inflationary periods; report event counts.

## Required exhibits

Data construction audit; correlation and covariance plots; regime return/risk table; maturity and threshold robustness; diversification comparison.

## Robustness

Synthetic zero returns are not traded bond-index returns. Stress includes financial prices, so association is not causal; use lagged measures, revised-vintage caveat and fixed definitions. Avoid very small stress regimes and overlapping-window naive t-tests.

## Minimum viable thesis

Monthly market and 5y synthetic zero returns, lagged stress, conditional risk and paired block inference. Distinct from macro inflation hedge A04.02.02.

## Optional extension

Inflation and policy regime interactions or bivariate DCC-GARCH, with strictly past-only forecasting.

## Prerequisites

Fixed income, covariance estimation, time-series econometrics and Python.

## Thesis outline

1. Stock-bond risk;

2. Return construction;

3. Stress and conditioning;

4. Correlation and diversification;

5. Robustness.

## Milestones

W1-3: theory/source checks; W4-6: build return panel; W7-9: conditional estimates; W10-12: robustness and portfolio risk; W13-16: write/reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
