# Research plan | A03.02.01

## Study design and independent work

Verify each conditional joint row sums to one, shock marginals and P are identical across coupling cases, same stationary weights, CRRA constant-surplus and Euler checks. Show covariance identity by state and distinguish SDF volatility from priced covariance; retain nonfinite present-value cells.

## Prespecified implementation

Use three surplus states and quarterly symmetric growth, compare joint and independently coupled transition with same P and growth marginals. External habit marginal utility assumption: m=beta*(G*s_next/s_now)^(-gamma); compute exact conditional stock returns with D=C. Check stationary distribution, positivity, spectral radius and Euler residual. Vary move probability and gamma only after verifying base; no claim full Campbell–Cochrane equilibrium or engineered constant rf. Show state-specific SDF moments and premium; conditional countercyclicality is a result, not an imposed sign.

## Required tasks

1. Derive SDF and finite-state pricing matrix; verify CRRA one-state analytical limit and Euler residuals.

2. Solve prices, risk-free rates and conditional equity returns for feasible parameter scenarios; report infeasible/nonfinite cases.

3. Compare conditional premia and SDF volatility by surplus state and compute stationary average and variability.

4. Vary transition sensitivity, persistence and gamma; inspect risk-free volatility trade-off and whether countercyclicality actually emerges.

5. Compare dependent versus independent transitions holding growth moments and marginal state dynamics fixed.

## Required exhibits

Transition matrices, pricing and Euler tests, state-dependent SDF and return tables, spectral radius diagnostics and comparative-static plots.

## Robustness

The bounded surplus process is exogenous external habit, not the original continuous surplus law or full general equilibrium calibration. Countercyclical premia are a hypothesis, not imposed; boundary effects and risk-free variation must be reported. Keep annual/quarterly preference units consistent.

## Minimum viable thesis

Exact finite-state solution with CRRA benchmark, dependent/independent surplus cases, state-dependent risk prices and comparative statics, including feasibility and risk-free diagnostics.

## Optional extension

Approximate the Campbell-Cochrane surplus sensitivity function on a refined grid and compare risk-free stabilization; optionally match public consumption moments after acquisition.

## Prerequisites

Consumption-based asset pricing, Markov chains, linear algebra, numerical methods and Python.

## Thesis outline

1. Consumption risk and habit;

2. External-habit SDF and finite-state model;

3. Numerical solution and checks;

4. Conditional premia and trade-offs;

5. Model limits.

## Milestones

W1-3: habit and SDF derivation; W4-6: finite-state transitions and solver; W7-9: benchmarks and state outcomes; W10-12: comparative statics; W13-16: economic interpretation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
