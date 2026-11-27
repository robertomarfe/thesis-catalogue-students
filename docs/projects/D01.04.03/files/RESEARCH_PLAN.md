# Research plan | D01.04.03

## Study design and independent work

Record noise draws, holdouts, solver starts and comparable timing rules before fitting. Separate nested limits, recovery under correct specification and prediction under misspecification. Rank models using predeclared metrics, not whichever metric favors one model.

## Required tasks

1. Verify three pricers, model restrictions, parity and accuracy using independent references.

2. Freeze panel splits, error scale, bounds and multistart budget before fitting.

3. Compare weighted training loss, held-out price/IV loss and wall time, distinguish optimizer from pricing calls.

4. Examine parameter recovery on correct-DGP cases and Jacobian conditioning with quote perturbations.

5. Plot Pareto trade-offs across truth/noise levels; report when simpler models suffice.

## Required exhibits

Model/DGP error matrix, price accuracy-versus-runtime plot, parameter stability and failure counts, held-out maturity errors.

## Robustness

Use comparable optimizer budgets and recorded tolerances; no universal model ranking from selected DGPs. Bid/ask perturbations may create arbitrage; document cleaning and use clean truth for independent scoring. Separate extrapolation and interpolation.

## Minimum viable thesis

Three models, two truth DGPs, frozen holdouts, matched accuracy targets, multistart and runtime report.

## Optional extension

Add a prespecified SVI slice baseline or an extra advanced model, distinguishing static surface fit from dynamic pricing.

## Prerequisites

Derivative pricing, numerical integration, constrained optimization, statistics.

## Thesis outline

1. Flexibility and identification;

2. Model families and benchmarks;

3. Synthetic quote design;

4. Calibration/generalization results;

5. Cost and limits.

## Milestones

W1-3: models and objectives; W4-6: independent pricers; W7-9: calibration; W10-12: perturbation and holdout; W13-16: report.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
