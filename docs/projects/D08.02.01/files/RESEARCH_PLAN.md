# Research plan | D08.02.01

## Study design and independent work

Separate the future conditional window from D08.01.02's realized swap variance. Check zero delivery, Jensen and convergence. Do not claim empirical futures calibration from spot observations.

## Required tasks

1. Derive A,B and validate conditional variance expectation; check T=0 and long-T stationary limit.

2. Compute F_VIX with exact CIR transition via quadrature and simulation.

3. Compare with square-root-of-mean approximation, measure gap and curve slope at 1/3/6/12 months.

4. Vary v0,kappa,xi independently; show where contango or backwardation changes and why the convexity term can shift levels.

5. Quantify numerical error for low degrees of freedom and compare deterministic variance or moment-matched approximation.

## Required exhibits

VIX futures curve families, parameter sensitivity and Jensen-gap tables, exact/MC agreement, convergence and stationary-limit diagnostics.

## Robustness

CIR positivity/nonnegativity boundary must be handled exactly. Model assumes continuous returns, deterministic rates and theoretical VIX payoff rather than SOQ calculation; no observed futures returns, term premium or trading performance claimed. VIX spot alone cannot identify Q dynamics.

## Minimum viable thesis

Exact synthetic futures curve under at least three variance states and multiple kappa,xi; independent pricing validation and decomposition of state and convexity effects. Distinct from D08.01.02 integrated realized volatility swap.

## Optional extension

Compare one- and two-factor variance models or calibrate to synthetic VIX futures with held-out maturities.

## Prerequisites

Risk-neutral valuation, square-root diffusions, noncentral chi-square distribution and Python.

## Thesis outline

1. VIX and futures pricing;

2. CIR conditional variance and transitions;

3. Numerical solution;

4. Curve-shape comparative statics;

5. Model limits.

## Milestones

W1-3: derive VIX approximation; W4-6: CIR transition and quadrature; W7-9: curve experiments; W10-12: sensitivity and limits; W13-16: documentation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
