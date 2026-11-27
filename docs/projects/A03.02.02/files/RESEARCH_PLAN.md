# Research plan | A03.02.02

## Study design and independent work

For every persistence value record transition probabilities, realized conditional shock-surplus covariance, stationary law, mean and SD of log P/D, conditional rate and premium, and stationary second moments including between-state variation. Compare independent-coupling and constant-surplus controls; independently simulate one interior case with burn-in and MC uncertainty.

## Prespecified implementation

Use two surplus states with symmetric stay probabilities; joint high-surplus positive-shock mass = .5*P_iH + coupling*.5*min(P_iH,1-P_iH), so coupling=.8 reproduces proposal c_i=.4*min. Use constant-surplus CRRA and independent joint controls. Compute stationary mean and variance of log ratio and gross return using exact transition-weighted first/second moments; separately report state variation of risk-free and conditional premium. Student runs full persistence grid, reports inadmissible cells and verifies selected moments via long simulation (seed 2027).

## Required tasks

1. Verify joint probabilities, positivity of surplus, stationarity and growth moments; solve q only when spectral radius<1.

2. Compute exact transition-weighted mean and SD of log P/D, stock return, Rf and premium.

3. Vary persistence at fixed surplus marginal, gamma and coupling; report mechanism via state prices and valuation sensitivities, not automatic monotonicity.

4. Plot feasible parameter grid and trade-offs; compare CRRA and independent habit shocks.

5. Simulate selected valid cases 50,000 years, seed 2027, to verify moments; optional public targets compare annual units.

## Required exhibits

Admissibility map, state-by-state q/Rf, moment tables, persistence/gamma comparative statics and CRRA diagnostics.

## Robustness

Stylized finite-state external habit, not Campbell-Cochrane's nonlinear surplus process. No negative consumption or surplus; check price existence and numerical residual. Mean-preserving persistence experiment also changes coupling feasibility; report realized growth-surplus correlation. Do not discard failed parameters silently or claim exact empirical calibration.

## Minimum viable thesis

Finite-state solution with fixed marginal surplus, at least four persistence values, CRRA benchmark, exact moments and price-existence checks. Distinct from A03.02.01 by persistence comparative statics and valuation volatility trade-off.

## Optional extension

Use a three-state surplus grid or minimize a small moment criterion against observed consumption and valuation moments subject to admissibility.

## Prerequisites

Consumption-based asset pricing, Markov chains, matrix algebra and Python.

## Thesis outline

1. Habit and risk aversion;

2. Finite-state economy;

3. Solution and admissibility;

4. Persistence and risk-volatility trade-offs;

5. Empirical relevance.

## Milestones

W1-3: derive SDF and prices; W4-6: construct transition law and checks; W7-9: compute moments; W10-12: parameter trade-offs and optional targets; W13-16: interpretation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
