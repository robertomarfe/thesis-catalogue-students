# Research plan | D06.03.02

## Study design and independent work

Validate first-call, no-call, equality and maturity paths by hand. Freeze coupon before physical stress. Report ratio uncertainty and infeasibility; do not confuse a stylized price with an issue quote.

## Required tasks

1. Write a cashflow truth table and test deterministic paths including first call, no call and barrier equality.

2. Estimate fair price/coupon with MC confidence interval and expected life under Q and P separately.

3. Vary barrier, autocall threshold, tenor and volatility; plot redemption-time distributions and coupon versus principal loss.

4. Estimate spot/volatility/rate bumps with common paths, holding original reference level fixed.

5. Compare with a plain bond plus terminal short put benchmark; isolate optional issuer credit effects and run P stress tests.

## Required exhibits

Cashflow specification and tests; fair coupon map; redemption-time and principal-loss distribution; Greek and stress table.

## Robustness

Discontinuous payoff makes naive pathwise Greeks unreliable; test bump sizes and sampling error. Coupon and barrier conventions must be explicit. Price is not an observed issue quote; independent issuer hazard is illustrative and excludes wrong-way risk.

## Minimum viable thesis

One fully specified note, exact observation simulation, fair coupon and sensitivity grid, Q/P distinction and tested cashflow engine.

## Optional extension

Worst-of two-asset note with correlated GBMs; separate correlation sensitivity from single-name volatility.

## Prerequisites

Risk-neutral pricing, Monte Carlo, derivative Greeks and Python.

## Thesis outline

1. Structured note contracts;

2. Pricing and stopping;

3. Simulation design;

4. Coupon and risk decomposition;

5. Model limitations.

## Milestones

W1-3: contract and pricing; W4-6: cashflow engine; W7-9: fair coupon and tests; W10-12: risk/stress; W13-16: documentation and thesis.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
