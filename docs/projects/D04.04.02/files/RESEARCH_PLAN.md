# Research plan | D04.04.02

## Study design and independent work

Distinguish quadratic regression hedges from neural entropic-risk optimization. Test future-input perturbation, rank and conditioning, validation-only penalty choice, paired test squared loss and tails.

## Required tasks

1. Verify cash ledger and frictionless GBM convergence.

2. Fit basis regression without look-ahead; select ridge on validation.

3. Freeze and evaluate on independent paths, compare RMSE, ES95 and turnover.

4. Test added lagged volatility features and independent stress DGP with common premium within each comparison.

5. Report sensitivity to training size, basis degree and seed.

## Required exhibits

Held-out hedging error table, policy slices, basis/penalty diagnostics, learning curve and distribution-shift results.

## Robustness

Model-free describes policy inputs, not data generation. No observed market performance; no claim of global optimality or cost-optimal policy. Shared discounted ledger and identical constraints; separate latent oracle from feasible inputs.

## Minimum viable thesis

GBM and one misspecified DGP, linear and enriched basis, independent test and BSM benchmark.

## Optional extension

Train cost-aware policy with backward regression or compare neural policies on identical paths.

## Prerequisites

BSM, regression, Monte Carlo, Python.

## Thesis outline

1. Hedging as projection;

2. Regression policy;

3. Synthetic design;

4. Test results;

5. Robustness.

## Milestones

W1-3: ledger and theory; W4-6: simulations; W7-9: policy fitting; W10-12: independent tests; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
