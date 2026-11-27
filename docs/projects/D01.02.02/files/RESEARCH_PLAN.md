# Research plan | D01.02.02

## Study design and independent work

First change one parameter at a time at a common forward and grid, then explore jointly varying correlation and vol-of-vol. Report actual expected variance for every scenario, flag price bounds, and assess slope sensitivity to the strike window.

## Required tasks

1. Reproduce BSM limit with xi->0 and deterministic integrated variance, check strike convexity.

2. Construct level, slope and curvature versus maturity; report finite-difference step sensitivity.

3. Vary v0,theta,kappa,xi,rho one at a time; plot signed sensitivities.

4. Use standardized local Jacobian and singular values to find near-collinear parameter effects; compare short-only versus full surface grids.

5. Add modest quote noise and show whether similar smile features can arise from different parameter vectors.

## Required exhibits

Smile and term structure panels, sensitivity heatmaps, feature Jacobian, singular-value table, matched-scenario plots.

## Robustness

Parameter changes affect multiple smile features jointly. Do not claim unique parameter identification from a few summaries or physical leverage estimates from Q rho. Very small option time values destabilize IV inversion; report excluded cells and use price checks.

## Minimum viable thesis

Validated pricing and IV inversion, five parameter comparisons and one conditioning exercise. Distinct from D01.02.01's calibration objective and D02.02.01's parametric surface fitting.

## Optional extension

Study local identification when maturities and strikes are unevenly sampled or add jump risk as a competing mechanism.

## Prerequisites

Stochastic calculus, option pricing, numerical integration and linear algebra.

## Thesis outline

1. Implied volatility and Heston;

2. Features and numerical validation;

3. Comparative statics;

4. Identification and noise;

5. Interpretation.

## Milestones

W1-3: theory and feature definitions; W4-6: pricer/IV tests; W7-9: parameter grids; W10-12: Jacobian and robustness; W13-16: figures and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
