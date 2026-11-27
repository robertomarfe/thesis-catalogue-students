# Research plan | D01.03.02

## Study design and independent work

Generate a separate Heston and Merton truth panel. Use the same objective, bounds policy, numerical precision and untouched test grid across fitted models; report model-dependent failures and do not select short maturities after inspecting errors.

## Required tasks

1. Verify pricing and IV inversion against BSM limits.

2. Fit both models to both truth panels with common weights.

3. Compare training and held-out price/IV errors and short-end skew.

4. Profile parameters and record near-equivalent fits; report Jacobian singular values.

5. Repeat noise and strike-grid scenarios; compare short-maturity OTM premiums and explain limits of inference.

## Required exhibits

Smile panels, calibration and held-out tables, parameter profile, residual heatmap and pricing error audit.

## Robustness

Synthetic model discrimination is not empirical identification. Match quotes, weights, search budget and tolerances; avoid nearly zero vega. No actual option database or structural claim. Unlike D01.03.01, this is cross-model calibration and holdout.

## Minimum viable thesis

Two synthetic panels, two calibrated models, held-out strikes/maturities and multistart diagnostic.

## Optional extension

Compare Bates model with a parameter-count penalty or barrier prices under observationally similar vanillas.

## Prerequisites

Stochastic calculus, characteristic functions, optimization, Python.

## Thesis outline

1. Skew mechanisms;

2. Models and pricing;

3. Calibration design;

4. Discrimination;

5. Limits.

## Milestones

W1-3: models; W4-6: independent pricing; W7-9: calibration; W10-12: holdouts and profiles; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
