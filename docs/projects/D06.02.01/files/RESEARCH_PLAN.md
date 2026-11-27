# Research plan | D06.02.01

## Study design and independent work

Use adjacent lattice refinements, verify q=0 with nonnegative r and the maturity limit. Report boundary resolution separately from price precision. Discrete dividends require different cashflow treatment.

## Required tasks

1. Derive backward induction and verify European prices against BSM.

2. Compute American-minus-European premiums for calls and puts; map absolute and relative premiums by strike, carry and maturity (avoid ratios to near-zero values).

3. Extract exercise boundaries at common dates and record indeterminate nodes close to indifference.

4. Decompose the premium into discounted expected exercise benefits using the recursion V=continuation+max(intrinsic-continuation,0), and verify its sum under Q.

5. Stress the rate/dividend trade-off and distinguish high intrinsic value from optimal exercise.

## Required exhibits

Premium heatmaps, exercise boundaries, carry sensitivity plots, convergence table and numerical premium decomposition.

## Robustness

Test no-dividend call equality, American>=European, intrinsic lower bound and maturity limit. Exercise boundary errors can be material even when prices converge. A discrete-dividend extension needs separate ex-date treatment. Do not equate the Q probability of exercise to a physical exercise frequency.

## Minimum viable thesis

Validated tree, calls and puts, at least three carry scenarios, premium and boundary maps plus convergence. The focus is economic comparative statics rather than comparing solvers (D05.02.01).

## Optional extension

Compare continuous yield with known cash dividends using a suitably adjusted tree or finite differences.

## Prerequisites

Derivatives pricing, probability, Python arrays and basic numerical methods.

## Thesis outline

1. Exercise rights and optimal stopping;

2. CRR valuation and benchmarks;

3. Design and verification;

4. Exercise boundaries and premia;

5. Carry and practical limitations.

## Milestones

W1-3: stopping theory and recursion; W4-6: European and American implementation; W7-9: comparative statics; W10-12: premium decomposition and convergence; W13-16: interpretation, code and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
