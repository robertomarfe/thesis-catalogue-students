# Research plan | D05.01.02

## Study design and independent work

Check Gaussian covariance before pricing. If reference uncertainty prevents ranking, increase the reference budget or label the result unresolved. The exercise measures integration error, not continuous-monitoring discretization.

## Required tasks

1. Derive Q expectation and verify lognormal geometric Asian closed form; check bridge covariance and marginal means.

2. Implement three estimators, use powers of two without skipping Sobol points and record scramble seeds.

3. Compare RMSE, bias estimates and empirical dispersion against reference, with uncertainty on reference.

4. Plot log-error versus N and versus wall-clock time; report setup versus evaluation costs and memory.

5. Examine monitoring dimension and moneyness, and repeat for a geometric Asian payoff with exact truth to isolate estimator error.

## Required exhibits

Validated generators, reference precision table, estimator RMSE and timing curves, convergence slopes with caveats and reproducible seed list.

## Robustness

Use independent randomizations, same hardware and repeated timing; avoid ordinary IID confidence intervals for low-discrepancy samples. Clip inverse-CDF endpoints only by a documented machine-precision rule. Report deep OTM cases with rare positive payoffs separately. The exercise compares integration error, not market accuracy or discretization of continuous monitoring.

## Minimum viable thesis

All three estimators, exact geometric benchmark and independently validated arithmetic reference, two monitoring dimensions and three sample budgets with replicated error/timing analysis.

## Optional extension

Combine RQMC with control variates or PCA path construction; baseline must isolate sampling and coordinate-ordering effects.

## Prerequisites

Monte Carlo, multivariate normals, Python SciPy qmc and numerical benchmarking. No market data required.

## Thesis outline

1. Path-dependent valuation;

2. Monte Carlo and randomized QMC;

3. Brownian path generation and benchmarks;

4. Convergence and runtime;

5. Effective dimension and limits.

## Milestones

W1-3: study Sobol and bridge; W4-6: implement and test path generators; W7-10: run benchmarks; W11-13: dimension and payoff sensitivity; W14-16: document and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
