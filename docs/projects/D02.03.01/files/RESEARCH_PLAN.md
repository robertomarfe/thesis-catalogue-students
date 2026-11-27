# Research plan | D02.03.01

## Study design and independent work

Use irregular strike spacing, two independently constructed clean laws and fixed noise draws. Report adjustment cost and holdout recovery separately; distinguish discrete state-price mass from a differentiable density.

## Required tasks

1. Derive arbitrage inequalities and construct a deliberately violating three-strike butterfly example.

2. Fit cubic interpolation in IV space (after price inversion), unconstrained price interpolation and constrained price projection plus piecewise-linear interpolation. Use nonuniform finite differences; record infeasible inversions and optimizer status.

3. Evaluate dense held-out clean call prices, slopes, convexity violations and magnitude of negative butterfly costs.

4. Quantify adjustment to observed noisy quotes and error trade-off for different sparsity and noise levels; inspect reconstructed interval state-price mass rather than differentiating kinks as a smooth density.

## Required exhibits

Smile and call-price plots, butterfly spread/convexity maps, held-out error table, feasibility and quote-adjustment statistics, reproducible projection and diagnostic code. Include at least one example where visually smooth IV generates a violation.

## Robustness

Test exact BSM prices and nonuniform spacing; compare deterministic tolerance with floating-point error and verify constraints on each knot interval. Do not claim arbitrage-free extrapolation outside domain or calendar freedom for independent slices. Test price- versus vega-weighted projection with prespecified weights; report whether clean truth is inside quote intervals.

## Minimum viable thesis

Correct finite-grid arbitrage restrictions, three interpolation alternatives, two clean DGPs, controlled noise experiment, held-out errors and economic interpretation of convexity. No requirement for a smooth global density.

## Optional extension

Extend to convex spline or joint calendar-constrained normalized call surfaces with maturity-consistent forwards, and test on a second synthetic DGP or verified public quotes.

## Prerequisites

Black-Scholes inversion, convexity, elementary linear/quadratic programming, SciPy or CVXPY.

## Thesis outline

1. Static arbitrage and state prices;

2. Interpolation and constrained optimization;

3. Data-generating models and diagnostics;

4. Pricing accuracy versus arbitrage;

5. Limitations and conclusion.

## Milestones

W1-3: derive inequalities and benchmark prices; W4-6: implement projection and interpolation tests; W7-10: run noise/sparsity grid; W11-13: stress domain and weights; W14-16: finalize reproducible figures and thesis.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
