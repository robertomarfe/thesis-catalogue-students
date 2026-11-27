# Research plan | D05.03.02

## Study design and independent work

Inspect short maturity, rare jumps and deep strikes before asserting convergence. A wider interval may require more terms; do not claim universal exponential convergence.

## Required tasks

1. Derive COS coefficients for a put and verify normalization of phi and martingale moment.

2. Implement vectorized COS and direct quadrature; verify put-call parity.

3. Establish independent reference prices and error tolerances in absolute price and relative error away from tiny values.

4. Sweep N holding interval fixed and interval holding N large; plot error maps, identify cancellation and short-expiry failures.

5. Benchmark one strike and a 100-strike grid including setup cost; report minimum runtime meeting a fixed error tolerance.

## Required exhibits

Convergence/error heatmaps; benchmark reference checks; time-versus-error curves; failure-case table and reproducible code.

## Robustness

Avoid selecting a reference from the same COS implementation. Check tail width separately, do not claim universal exponential convergence. Timing includes coefficient setup and uses identical requested precision. Distinct from FFT interpolation study D05.03.01.

## Minimum viable thesis

BSM and Merton, independent analytic/mixture references, COS and quadrature with convergence and fair runtime comparison.

## Optional extension

Add Heston characteristic-function branch diagnostics and an independent high-precision quadrature reference.

## Prerequisites

Fourier analysis, risk-neutral valuation, numerical integration and Python.

## Thesis outline

1. Characteristic functions;

2. COS derivation;

3. Independent benchmarks;

4. Truncation and runtime;

5. Limits.

## Milestones

W1-3: derivations; W4-6: reference pricers; W7-9: COS and tests; W10-12: error/runtime grid; W13-16: writing and replication.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
