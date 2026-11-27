# Research plan | D11.02.02

## Study design and independent work

Report absolute moment errors and cancellation across strip, tail and noise choices. Compare central moments only on admissible inputs. Record the exact support and quote tolerance for conditional bounds.

## Required tasks

1. Derive spanning formula and analytic mixture raw/central log moments.

2. Recover moments from dense full-range strips; verify convergence to benchmark.

3. Vary strike support, mesh and bid/ask noise; quantify bias and sampling variation separately.

4. Construct two feasible nonnegative discrete Q distributions matching same finite quotes within tolerance but differing in fourth moment (LP on fixed support).

5. Expand support and show tail assumption sensitivity; report undefined moments/negative estimated variance without forcing validity.

## Required exhibits

Moment error surfaces; tail contribution plots; feasible moment intervals and matched-price examples; numerical tolerances.

## Robustness

No finite-strike claim of model-free exact moments. LP bounds apply to declared support; log moment tails near zero may be unbounded without restrictions. Q moments not realized P risk; density recovery is not the objective (D11.02.01).

## Minimum viable thesis

Analytic two-market truth, option-strip moment recovery, truncation/noise study and at least one support-conditional moment bound.

## Optional extension

Compare option-implied crash probabilities or robust bounds with additional traded strikes.

## Prerequisites

Option pricing, integration, probability moments, constrained optimization.

## Thesis outline

1. Static replication;

2. Risk-neutral log moments;

3. Synthetic markets;

4. Truncation and partial identification;

5. Conclusions.

## Milestones

W1-3: spanning derivation; W4-6: generator and moments; W7-9: quadrature grids; W10-12: bounds and noise; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
