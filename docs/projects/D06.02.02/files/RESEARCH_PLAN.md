# Research plan | D06.02.02

## Study design and independent work

Do not use realized future cashflows in test decisions. Compare three basis settings and three training sizes after one validated case. Distinguish regression conditioning from stopping-policy performance.

## Required tasks

1. Derive Snell envelope and implement exercise-aligned tree; verify European floor and maturity-only equality.

2. Train LSM backward, record regression sample counts and stopping fractions by date; avoid exercising out of money.

3. Freeze policy and evaluate on independent paths; report MC error conditional on policy plus between-training variability.

4. Compare basis degree and training size using a fixed validation set; evaluate chosen policy once on held-out paths.

5. Analyze exercise boundary versus tree, early exercise frequency and gap across maturity/volatility/moneyness.

## Required exhibits

Tree convergence, price and policy gap table, independent evaluation intervals, exercise-boundary figures, regression conditioning and computation time.

## Robustness

A better in-sample fit need not improve stopping policy. Use only information at exercise time, no future cash-flow leakage in evaluation; ensure correct discount times and distinguish policy gap from reference/MC noise. No exact optimality claim for LSM.

## Minimum viable thesis

One-dimensional Bermudan put, three basis settings, three training sizes, independent test paths, tree reference and uncertainty. Distinct from early-exercise economics (D06.02.01).

## Optional extension

Bermudan max/average option on two correlated assets; compare with a dual upper bound only after validating the martingale construction.

## Prerequisites

Conditional expectation, Monte Carlo, least squares and Python.

## Thesis outline

1. Optimal stopping and Snell envelope;

2. LSM regression algorithm;

3. Tree reference and train/test design;

4. Policy sensitivity;

5. Limitations.

## Milestones

W1-3: stopping and tree; W4-6: implement LSM; W7-9: policy validation and independent value; W10-12: basis, sample and exercise sensitivity; W13-16: code and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
