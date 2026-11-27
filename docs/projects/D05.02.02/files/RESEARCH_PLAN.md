# Research plan | D05.02.02

## Study design and independent work

Compare analytical prices and Greeks over spot, not just ATM. A-stability does not imply positivity or accuracy. Exclude deliberately unstable runs from successful time-to-tolerance comparisons.

## Required tasks

1. Derive stencil, stability/positivity conditions and boundary treatment.

2. Implement each scheme; unit-test zero payoff, constant payoff discount and BSM prices.

3. Sweep dt/dx^2 to demonstrate instability deliberately, not use unstable prices as candidates.

4. Compare price, delta, gamma max/RMS errors near strike and across interior grid; plot oscillations for short maturities and Rannacher smoothing.

5. Separate time, space and truncation errors with one-at-a-time refinement and runtime/error frontiers.

## Required exhibits

Stencil/stability table, convergence rates, spot profiles of price/Greeks, oscillation figures, error-runtime tradeoffs and boundary tests.

## Robustness

For digital options derivatives near strike become steep as T approaches zero; assess at positive T and analytic Greeks. Boundary approximation and discontinuity/grid alignment can dominate convergence. A-stability is not positivity; report negative or oscillating prices rather than silently clip.

## Minimum viable thesis

Three schemes plus Rannacher variant, European call and digital, analytical references, stable/unstable grids, separate refinement and Greek diagnostics. Distinct from D05.02.01's American optimal-stopping solver comparison.

## Optional extension

Use a nonuniform or adaptive grid and compare efficiency for short-dated digital or barrier options.

## Prerequisites

Numerical linear algebra, PDEs, BSM and Python/SciPy.

## Thesis outline

1. BSM PDE and stencil;

2. Stability and damping;

3. Algorithm and benchmark;

4. Convergence and oscillations;

5. Practical recommendations.

## Milestones

W1-3: discretize PDE; W4-6: implement and verify boundaries; W7-9: stability and refinement sweeps; W10-12: Greeks, smoothing and runtime; W13-16: document and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
