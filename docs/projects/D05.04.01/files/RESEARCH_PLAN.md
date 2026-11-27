# Research plan | D05.04.01

## Study design and independent work

Use nested Brownian increments for Euler comparisons and independent replications. Separate path-count error from time-step error. Keep fixing dates constant and report high-vol-of-vol failures.

## Required tasks

1. Validate CIR conditional first two moments and zero vol-of-vol limit.

2. Implement full/partial truncation and QE-M using original algorithm; document correlation handling.

3. Establish independent European reference and verify martingale moment.

4. Report bias, confidence intervals, negative-state frequency and time-to-tolerance as grid changes.

5. Price discretely monitored Asian option using same observation dates and finest-grid cross-scheme comparison; label reference uncertainty.

## Required exhibits

Scheme pseudocode and tests; bias/SE/runtime plots; boundary diagnostic; exotic sensitivity and convergence table.

## Robustness

Keep monitoring fixed when refining simulation; compare confidence intervals rather than absolute sample discrepancies. Do not silently clip states or call finest MC exact. Time hardware and setup consistently.

## Minimum viable thesis

Two Euler schemes plus QE-M, two variance regimes, European references and convergence/cost comparison.

## Optional extension

Exact CIR transition with approximate integrated variance; compare with Broadie-Kaya exact joint benchmark if feasible.

## Prerequisites

SDEs, Monte Carlo, characteristic functions, Python.

## Thesis outline

1. Heston and boundary behavior;

2. Discretization schemes;

3. Validation;

4. Accuracy/cost experiments;

5. Exotic implications.

## Milestones

W1-3: model and schemes; W4-6: reference and Euler; W7-9: QE-M; W10-12: convergence grid; W13-16: exotic and report.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
