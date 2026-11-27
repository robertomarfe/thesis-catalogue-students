# Research plan | D07.04.01

## Study design and independent work

Keep the counterexample labeled inadmissible under money-market Q, not an alternative calibrated pricing model. Separate integration bias, sampling uncertainty and runtime.

## Required tasks

1. Derive bond dynamics by Ito and verify the drift cancellation.

2. Implement exact Gaussian forward increments or fine-grid benchmark and compare Euler.

3. Test E[P(t,T)/B(t)]=P(0,T) with paired MC uncertainty for each maturity and grid.

4. Quantify omitted-drift distortion and compare time versus maturity integration errors.

5. Reconstruct level, slope and curvature responses for one and two factors under matched initial curves.

## Required exhibits

Forward and bond evolution plots, discounted-price errors in bp of initial notional with MC intervals, convergence and runtime table, factor loading curves.

## Robustness

Do not infer physical forecasts from Q drift. Distinguish MC sampling, quadrature and time-step error; time-to-maturity coordinates require a transport term. Do not claim exact no-arbitrage for arbitrary numerical interpolants.

## Minimum viable thesis

One-factor deterministic volatility HJM, analytic drift, three maturity/grid checks and zero-drift counterexample; agreement with benchmark within numerical and MC tolerance.

## Optional extension

Add a second factor and compare Gaussian bond-option prices with a jointly simulated discounted payoff.

## Prerequisites

Stochastic calculus, bond math, Gaussian processes, numerical quadrature, Python.

## Thesis outline

1. Forward rates and bond pricing;

2. HJM restriction;

3. Gaussian benchmark and discretization;

4. Martingale diagnostics;

5. Factor structure and limitations.

## Milestones

W1-3: derive restriction and quote conventions; W4-6: exact reference and grid tests; W7-9: paired MC; W10-12: factor/grid robustness; W13-16: write and reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
