# Research plan | A03.03.01

## Required tasks

1. Derive iid formulas from recursion, verify Euler equations and CRRA benchmark.

2. Map rf, wealth price-consumption ratio and excess returns across gamma/psi with fixed beta, noting inadmissible points.

3. Solve two-state wealth ratios by fixed point and independent root solver; verify residuals.

4. Compute state-specific SDF moments, bill rates and claim prices (spectral radius below one for finite dividend prices); compare iid and persistent economies with matched unconditional moments as sensitivity.

5. Interpret independent gamma/psi effects, not calibration success.

## Required exhibits

Derivation, Euler residual table, preference comparative statics, state-dependent prices and risk premia, admissibility map.

## Robustness

Do not use wealth return as an arbitrary stock proxy. Separate log and arithmetic expected excess returns. Iid risk prices have restricted mechanisms; continuation-value risk requires state variation. No claim of explaining observed equity premium without a quantitative empirical test.

## Minimum viable thesis

Iid closed form and two-state solution with CRRA check, preference grids and equilibrium verification; leveraged claim optional. Distinct from A03.03.02's long-run risk calibration.

## Optional extension

Match observed consumption moments from public FRED data or introduce a persistent Gaussian expected-growth state.

## Prerequisites

Intertemporal utility, Euler equations, Markov chains, lognormal moments and numerical root finding.

## Thesis outline

1. Recursive versus CRRA preferences;

2. Iid equilibrium;

3. Markov growth solution;

4. Preference experiments;

5. Economic interpretation.

## Milestones

W1-3: recursion and SDF; W4-6: iid formulas/tests; W7-9: Markov solver; W10-12: price/risk sensitivity; W13-16: writing.

At every meeting submit your own code, inputs/parameter ledger, outputs and unresolved issues. Report null results and failed cases.
