# Research plan | D05.03.01

## Study design and independent work

Separate characteristic-function, cutoff, aliasing and interpolation error. Freeze tolerance and hardware protocol. Use absolute currency errors near zero; calibration is outside scope.

## Required tasks

1. Derive inversion, validate characteristic function normalization and martingale moments.

2. Test BSM analytic errors; implement two numerically independent Heston representations.

3. Sweep alpha, truncation and grid size, separately assess off-grid interpolation.

4. Report maximum and median absolute price error and timings at fixed tolerance (e.g. 0.001 per 100 spot).

5. Test short maturities, far strikes and high vol-of-vol; flag moment explosions and branch issues rather than suppressing failures.

## Required exhibits

Convergence plots, error/time Pareto frontiers, parameter grid and failure table, reproducible timing script.

## Robustness

Do not compare a coarse FFT with a high-accuracy reference without reporting tolerance. Reference inversion may share characteristic-function error; use independent limiting cases. Price error primary; relative errors near zero and IV error secondary. Keep model calibration out of scope.

## Minimum viable thesis

BSM exact validation, one Heston reference, FFT and direct quadrature comparisons across strike counts at matched tolerance. Distinct from D05.01 and D05.02 numerical methods.

## Optional extension

Add COS method and compare tail truncation or characteristic functions of jump models.

## Prerequisites

Complex numbers, Fourier transforms, stochastic volatility, numerical analysis.

## Thesis outline

1. Characteristic functions and inversion;

2. Algorithms;

3. Validation;

4. Accuracy-efficiency trade-offs;

5. Practical guidance.

## Milestones

W1-3: derive inversion; W4-6: implement and validate CF; W7-9: FFT and quadrature grids; W10-12: stress and timing; W13-16: document.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
