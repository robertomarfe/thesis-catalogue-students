# Research plan | D05.04.02

## Required tasks

1. Derive estimators and analytic references; verify units.

2. Implement independent seed replications and antithetic controls.

3. Compare bias, empirical SD, RMSE, CI coverage and runtime for increasing paths.

4. Inspect bump bias-variance and near-expiry/OTM cases.

5. Explain invalid digital pathwise result and quantify Asian reference uncertainty. For one arithmetic Asian call with 12 fixings, derive the likelihood-ratio score from all conditional log-increment densities and differentiate all fixings for pathwise vega. Use independent reference simulations with uncertainty; do not rank the invalid naive digital pathwise estimator.

## Required exhibits

RMSE versus path count/time, bump sensitivity plot, estimator bias/variance table and reference diagnostics. One Asian delta/vega estimator comparison with reference uncertainty, bump bias and cost-normalized RMSE.

## Robustness

Use identical random draws where appropriate and independent reference; distinguish sampling error from finite-difference bias. No universal ranking. State vega per unit volatility or per 1 vol point explicitly.

## Minimum viable thesis

European call and digital delta and vega, and one arithmetic Asian call (12 fixings, one strike and maturity), using bump-and-revalue, pathwise and likelihood-ratio estimators where valid. Include analytic European benchmarks, an independently generated numerical Asian reference with uncertainty and bump-size diagnostics, repeated seeds and a cost-normalized RMSE comparison. Explicitly report the invalid digital pathwise estimator rather than rank it.

## Optional extension

Conditional smoothing for digital or barrier sensitivities; automatic differentiation for smooth payoffs.

## Prerequisites

BSM, calculus, probability, Monte Carlo, Python.

## Thesis outline

1. Greeks and estimators;

2. Derivations;

3. Numerical design;

4. Efficiency comparisons;

5. Limits.

## Milestones

W1-3: derive estimators; W4-6: analytic checks; W7-9: experiments; W10-12: Asian and robustness; W13-16: writing.

At every meeting submit your own code, inputs/parameter ledger, outputs and unresolved issues. Report null results and failed cases.
