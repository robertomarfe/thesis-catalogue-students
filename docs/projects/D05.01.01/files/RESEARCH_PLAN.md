# Research plan | D05.01.01

## Study design and independent work

Freeze the payoff, seed and timing protocol. The combined estimator addresses the full question even when the MVT requires only two methods. Do not label a high-budget arithmetic reference exact.

## Required tasks

1. Implement plain MC and validate European prices against BSM; derive and test the geometric Asian price against plain MC.

2. Implement antithetics and control variates using pilot-estimated coefficients; compare identical path evaluations, include pilot overhead.

3. Estimate bias, empirical variance, RMSE and 95% interval coverage across seeds; compare runtime and variance-times-runtime efficiency.

4. Report log-log RMSE convergence and efficiency by payoff and moneyness. For Asian benchmark include its numerical uncertainty or evaluate paired differences.

## Required exhibits

Benchmark validation table; convergence plot; precision/cost table (standard error, RMSE, runtime, coverage); variance reduction ratio by strike; reproducible timing log. Explain why low-variance or rare-payoff cases can make relative ratios unstable.

## Robustness

Use independent random streams; exclude compilation warmup consistently but include sampling and coefficient estimation; repeat timing to reduce jitter. Confirm antithetic samples are not treated as independent observations. Test alternative sigma and number of monitoring dates; do not attribute discretization error to exact GBM at contractual dates.

## Minimum viable thesis

Two payoffs, plain MC plus two variance-reduction methods, independent replications, known analytic European benchmark, and a timing-normalized comparison. A ranking reversal across strikes is a useful finding.

## Optional extension

Randomized quasi-Monte Carlo with multiple independent scrambles or conditional Monte Carlo; measure uncertainty over scrambles, not deterministic sequence points.

## Prerequisites

Probability, risk-neutral valuation, basic statistics, Python vectorization. Suitable for a student developing quantitative programming skills.

## Thesis outline

1. Pricing by expectation;

2. Simulation error and variance reduction;

3. Experimental design and benchmarks;

4. Convergence and efficiency;

5. Limitations and applications.

## Milestones

W1-3: derive MC and analytic controls; W4-6: implement and validate pricing; W7-10: build repeated budget-controlled experiment; W11-13: timing/coverage and robustness; W14-16: write and regenerate outputs.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
