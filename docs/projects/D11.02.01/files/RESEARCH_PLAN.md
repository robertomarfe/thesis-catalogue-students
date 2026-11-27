# Research plan | D11.02.01

## Study design and independent work

Do not silently clip negative density estimates and call them calibrated distributions. Track feasibility, normalization, tail sensitivity and uncertainty across the prescribed grids. Distinguish distribution recovery from smile interpolation.

## Required tasks

1. Verify convexity and parity for noiseless calls; quantify violations induced by noise.

2. Fit each recovery method with fixed tuning using synthetic training scenarios, never true test density for tuning.

3. Compare call reconstruction, held-out strike errors, integrated CDF error and tail probability below x=0.8.

4. Report mass, mean, negative density mass, grid and regularization sensitivity.

5. Construct LP lower/upper bounds for the tail probability given call-price intervals on the assumed grid; document support dependence.

## Required exhibits

Density/CDF panels, call fit and tail error tables, diagnostics for constraints, partial-identification intervals.

## Robustness

Convex piecewise-linear calls imply a discrete distribution, not a smooth density. Do not interpret Q tail probabilities as physical probabilities. Finite strikes do not identify extreme tails; support constraints and smoothing are assumptions, not market information. Quote noise may cause infeasibility.

## Minimum viable thesis

Two known distributions, three strike grids and noise scenarios, naive versus constrained reconstruction, mass/mean and tail diagnostics. Distinct from D02.03.01, which evaluates interpolation rather than distribution recovery.

## Optional extension

Use lawful single-date option quotes, compare bid-ask-consistent probability bounds and point estimates.

## Prerequisites

Option pricing, numerical differentiation, constrained least squares, linear programming.

## Thesis outline

1. State prices and option derivatives;

2. Inverse problem and constraints;

3. Synthetic data;

4. Recovery and tail identification;

5. Implications.

## Milestones

W1-3: derive identities; W4-6: simulate calls and implement differences; W7-9: constrained fit and tuning; W10-12: tail bounds and sensitivity; W13-16: write and package.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
