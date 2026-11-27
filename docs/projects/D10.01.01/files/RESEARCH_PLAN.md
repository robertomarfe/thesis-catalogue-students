# Research plan | D10.01.01

## Study design and independent work

Audit positivity, complete monthly dates, release lag and actual targets. Verify OU transition and random-walk limit on artificial data, report inadmissible fits and paired loss comparisons.

## Required tasks

1. Plot level/log series and sample changes; estimate AR(1), OU parameters and uncertainty, compare with random walk and unit-root diagnostics. If b not in (0,1), report unconstrained estimates and constrained fit separately; avoid reporting a fictitious finite half-life.

2. Compute expanding forecasts with outcomes available at origin, benchmark forecasts and log-price RMSE/MAE.

3. Compare forecast losses and dependence-aware intervals by horizon; evaluate 2008 and 2020 as prespecified stress periods, not post-hoc exclusions.

4. Compare rolling estimates and nominal versus inflation-adjusted WTI (optional CPI with timing caveat); interpret model instability economically.

## Required exhibits

Price series and parameter stability figures, half-life and uncertainty table, forecast paths and OOS loss comparison, forecast horizon/sample audit. Report log forecast versus expected level distinctly.

## Robustness

Check OU exact transition and AR forecast against simulated known parameters; test alternate sample endpoints, release lag, drift and block length for overlapping losses. If nonpositive monthly observations exist, report and use a level-model sensitivity rather than silently drop/shift; negative futures settlement is not identical to spot measure. No derivative calibration inference from P estimates.

## Minimum viable thesis

Verified monthly spot series; OU versus random walk at 1,3,12 months with chronological evaluation, regime/rolling stability and defensible interpretation of weak or no mean reversion. Report actual forecast origin and data availability.

## Optional extension

Add a two-factor spot model or a futures/convenience-yield analysis only with a separately verified matched futures panel.

## Prerequisites

Stochastic processes, AR models, forecasting and Python statsmodels/SciPy. No futures dataset required.

## Thesis outline

1. Commodity economics and spot dynamics;

2. OU and random-walk models;

3. Data and forecast protocol;

4. Mean reversion and forecasting results;

5. Structural stability and derivative implications.

## Milestones

W1-3: verify EIA series, derive exact transition; W4-6: estimation and simulation unit tests; W7-10: OOS forecasts and loss inference; W11-13: rolling/stress sensitivities; W14-16: interpret and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
