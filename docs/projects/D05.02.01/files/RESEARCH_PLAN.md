# Research plan | D05.02.01

## Study design and independent work

Save the time-dependent boundary or rerun shorter expiries explicitly. Report domain and odd/even effects, complementarity and interpolation uncertainty. Fix price tolerance before timing.

## Required tasks

1. Derive optimal stopping recursion and PDE complementarity; implement European test and check probabilities.

2. Implement American CRR and implicit projected SOR, recording residuals and iteration limits.

3. Verify American price >= European price and intrinsic value; test r approaching zero for q=0.

4. Compare errors versus grid size and runtime, including odd/even tree effects and Smax sensitivity.

5. Plot exercise boundary as highest exercised stock grid node before expiry; interpolate carefully and quantify grid dependence.

## Required exhibits

Verified solvers, European benchmark and complementarity tests, price/convergence/timing tables, exercise-boundary curves and reference uncertainty.

## Robustness

Do not treat simple projection after an unconstrained implicit solve as an exact LCP solution. Match time-to-expiry and boundary definitions; report interpolation error and incomplete convergence. No market price validation implied by numerical agreement.

## Minimum viable thesis

Two working American solvers, European analytical checks, independent refined references, convergence and boundary analysis for at least six contracts.

## Optional extension

Add dividends or Crank-Nicolson with Rannacher smoothing, explicitly treating oscillations near the payoff kink.

## Prerequisites

Derivatives pricing, numerical linear algebra, PDE basics and Python.

## Thesis outline

1. American option optimal stopping;

2. Trees and obstacle PDE;

3. Implementation and reference design;

4. Accuracy, runtime and boundary results;

5. Numerical implications.

## Milestones

W1-3: optimal stopping and LCP; W4-6: European/CRR solver; W7-9: implicit obstacle solver; W10-12: convergence and boundaries; W13-16: robustness and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
