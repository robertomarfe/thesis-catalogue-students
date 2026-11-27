# Research plan | D07.02.01

## Study design and independent work

Report curve recovery, price and numerical error separately; evaluate all prescribed curves and a range of option parameters. Do not present an exact fit as evidence that option values are identified.

## Required tasks

1. Derive shift and bond formula; verify curve recovery to numerical tolerance on a maturity grid and sigma->0 limit.

2. Implement bond option closed form and put-call parity; independently value using exact joint Gaussian simulation of x and integral x with 100,000 paths, seed

2027. 3. Compare same-curve models varying a,sigma and quantify option-price range.

4. Compare constant-drift approximation's curve residuals and derivative prices; separate curve-fit error from dynamics.

5. Test optional GSW interpolation and sensitivity of forward differentiation; report zero rate and forward residuals.

## Required exhibits

Input/recovered curves, fit-error table, option sensitivity heatmaps, MC validation, interpolation diagnostic.

## Robustness

Government fitted curves are not collateralized swap/OIS curves. No swaption volatility data needed for core; parameters are scenarios, not calibrated to market option prices. Avoid differentiating noisy discrete rates without interpolation; do not confuse fit of initial discount factors with model validation.

## Minimum viable thesis

Three synthetic curves, exact shift/discount recovery, analytical bond option and independent validation at multiple a,sigma. Optional GSW makes empirical illustration richer but is not required.

## Optional extension

Calibrate a,sigma on generated caplet or swaption quotes and assess identification using a Jacobian/synthetic holdout.

## Prerequisites

Fixed income, Gaussian processes, stochastic discounting and Python.

## Thesis outline

1. Gaussian affine term structure;

2. Time-dependent shift;

3. Curve recovery and validation;

4. Derivative valuation sensitivity;

5. Identification limits.

## Milestones

W1-3: derive shift and pricing; W4-6: implement curves and Gaussian integrals; W7-9: bond-option benchmark; W10-12: sensitivity and optional GSW; W13-16: write and reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
