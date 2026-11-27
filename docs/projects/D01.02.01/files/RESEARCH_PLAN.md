# Research plan | D01.02.01

## Study design and independent work

Begin with a checked pricer and a two-parameter fit, then release all five parameters. Freeze an entire maturity and alternating strikes before generating noise. Report objective profiles, failed starts, parameter recovery and held-out prices as separate exhibits.

## Required tasks

1. Implement BSM prices/Greeks and Heston characteristic-function prices; check parity, limits as xi tends to zero with v0=theta, and numerical integration tolerance.

2. Calibrate a single BSM volatility and Heston by weighted least squares on training quotes (vega-scaled price errors or IV errors, fixed rule). Use positive parameter transforms, bounded rho and multiple starting points; record convergence.

3. Compare train and held-out price RMSE, IV RMSE (on invertible quotes), and maximum error. Repeat over noise seeds and over a separate flat-volatility generating model.

4. Vary rho, xi and kappa one at a time; inspect objective profiles and near-optimal parameter sets rather than equating good fit with parameter identification.

## Required exhibits

Table of true and fitted parameters with dispersion and training/test errors; smile-by-maturity panels; objective-profile figure for kappa/theta or xi/rho; numerical validation log. Interpret fit improvements relative to the known noise scale, not only percentage changes.

## Robustness

Check quadrature truncation, alternate initializations, quote weighting, Feller-constrained versus unconstrained (with valid numerical pricing), strike-only versus maturity holdout, and stress a low-skew scenario. Do not describe synthetic holdout fit as market evidence. Never reuse the held-out quotes to choose weights or parameter bounds.

## Minimum viable thesis

A correct BSM and Heston pricer, one full noise-free and one noisy calibration experiment, a prespecified holdout, and a defensible explanation of parameter recovery versus predictive pricing. Pass numerical tests before interpreting calibration. A null improvement is informative under the flat-volatility generating model.

## Optional extension

Optionally add a second synthetic generator (Merton jumps) to examine misspecification or a single documented free quote snapshot if available; keep actual-market validation clearly separate.

## Prerequisites

Risk-neutral pricing, Ito calculus, numerical integration, nonlinear optimization, Python/NumPy/SciPy. The characteristic-function derivation is the advanced element; use a published formula if needed and explain its logic.

## Thesis outline

1. Motivation and option smile;

2. No-arbitrage, BSM and Heston derivation;

3. Numerical pricing and calibration design;

4. Fit, identification and held-out results;

5. Robustness, limitations and conclusion.

## Milestones

W1-3: derive pricing equations and reproduce BSM tests; W4-6: implement/validate characteristic function and freeze surface design; W7-10: calibrate with multistart and noise repetitions, lock test set; W11-13: profile parameters and stress scenarios; W14-16: interpret, write, reproduce all exhibits from a clean run.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
