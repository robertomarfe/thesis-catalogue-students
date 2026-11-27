# Research plan | D07.03.02

## Required tasks

1. Verify par swap rate, annuity and initial curve fit.

2. Implement Jamshidian and independent discounted MC; check zero-vol intrinsic and payer-receiver parity.

3. Compute prices and normal implied vols on expiry-tenor grid.

4. Bump volatility, mean reversion and initial curve with consistent recalibration; report vega and key-rate sensitivity.

5. Match one ATM price across parameter sets and compare others; discuss parameter identification and optional two-factor comparison. The core experiment is strictly one-factor Hull-White. Measure vega and at least one curve sensitivity with contractual strike fixed and curve-refitting convention documented. G2++ correlation analysis is optional and requires separate approval.

## Required exhibits

Curve-fit and parity tests; expiry-tenor normal-vol surface; price/risk grids; MC uncertainty; calibration ambiguity illustration. Vega and curve-sensitivity validation with explicit bump convention and one-factor scope.

## Robustness

Keep cashflow convention, units and numeraire consistent; distinguish initial curve fitting from volatility calibration. Use single-curve stylization, not OIS/IBOR market calibration. Cash-settled swaption payoff differs.

## Minimum viable thesis

One-factor Hull–White fitted to two synthetic curves, analytic-versus-independent Monte Carlo check, expiry–tenor price and volatility sensitivity grid, and at least one vega and one key-rate or parallel-curve sensitivity with a declared bump and recalibration convention. No external swaption quotes required.

## Optional extension

G2++ comparison with matched ATM quote and orthogonal slope shocks.

## Prerequisites

Fixed income, Gaussian diffusions, options, simulation and Python.

## Thesis outline

1. Swaps and swaptions;

2. Gaussian rate model;

3. Pricing validation;

4. Volatility and risk;

5. Calibration limits.

## Milestones

W1-3: annuity and HW; W4-6: curve fit and pricer; W7-9: MC tests; W10-12: surface/risk; W13-16: comparison and write.

At every meeting submit your own code, inputs/parameter ledger, outputs and unresolved issues. Report null results and failed cases.
