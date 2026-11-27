# Research plan | D01.02.03

## Study design and independent work

Check derivative stability and held-out vanillas before comparing barriers. Hold monitoring and strike fixed. Treat barrier state, cash funding and initial capital explicitly; record the interpolation domain and the handling of out-of-domain simulations.

## Required tasks

1. Implement Heston vanilla reference and local variance extraction, map regularization/extrapolation.

2. Validate local model vanillas at withheld strikes/maturities; refine time/spot grid and reject unstable surface.

3. Compare discretely monitored barrier prices with independent MC error bars; common monitoring only.

4. On shared Heston P paths compare local and Heston delta-only self-financing hedges, stopping at knock-out.

5. Stress leverage, vol-of-vol, barrier proximity and time-step; separate surface fit error from genuine dynamics differences.

## Required exhibits

Vanilla price error map; local variance surface; exotic pricing and uncertainty table; delta-hedge distributions and stress diagnostics.

## Robustness

Vanilla agreement within tolerance is a prerequisite, not a finding. Avoid taking noisy second derivatives without positivity diagnostics. Both models' delta hedges incomplete in stochastic-vol market; report failed extrapolations, MC and discretization errors.

## Minimum viable thesis

One validated synthetic surface, withheld vanilla tests, one barrier family and one independent hedge experiment. Distinct from Heston calibration and surface fitting projects.

## Optional extension

Compare forward-start options or delta-vega hedging as a separate control.

## Prerequisites

Ito calculus, Heston, PDE/Monte Carlo, surface differentiation; advanced Python.

## Thesis outline

1. Local/stochastic volatility;

2. Dupire projection;

3. Calibration validation;

4. Path-dependent pricing and hedging;

5. Model risk.

## Milestones

W1-3: theory and pricer; W4-6: surface and derivatives; W7-9: vanilla checks and barriers; W10-12: hedging/stress; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
