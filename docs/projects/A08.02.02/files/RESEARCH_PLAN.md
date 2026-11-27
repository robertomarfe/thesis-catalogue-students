# Research plan | A08.02.02

## Study design and independent work

Verify support function with explicit worst-case mean vector; radius zero nests plug-in and compare two-asset grid with KKT. Freeze radius menu, window and caps before final sample, report binding constraints, paired OOS net CE and costs with failed windows. If interpreting statistical coverage, justify dependence adjustment separately.

## Prespecified implementation

Use uncertainty U=Sigma/n_eff (iid baseline), delta=0,1,2,4; gamma=5, optional cap .25. Compare support function and worst perturbation, delta=0 must equal MV. 500 simulations seed 2027 with 10 assets, perturbations aligned with U, separate actual true utility from worst-case objective. Rolling 120-month, choose delta on 1985-99 validation net CE, then lock through 2000-25 test. Same covariance estimate, cost and asset set; U diagonal and alternative n_eff sensitivity. Report infeasible/failed optimizers.

## Required tasks

1. Derive support function and implement convex solver; verify feasibility, delta=0 and numerical worst-case perturbation.

2. Use simulation to quantify oracle utility loss under mean perturbations, and differences between model worst case and actual realized risk.

3. Run monthly chronological backtest; fix delta/gamma before test, drift portfolio weights before rebalancing, charge common 0/10/25 bp on absolute traded weight.

4. Compare net certainty equivalent, Sharpe, volatility, turnover, drawdown and concentration using paired block-bootstrap intervals.

5. Vary uncertainty set U (diagonal vs covariance), training window and radius; distinguish delta effect from covariance shrinkage and constraint effects.

## Required exhibits

Optimization validation, sensitivity frontier, simulated utility-loss table, historical net performance and weights, turnover/ambiguity trade-off.

## Robustness

Mean uncertainty set does not robustify covariance unless extended; iid U may understate estimation risk. No test-set tuning or short-selling asymmetry. Historical return panels are not investable products; transaction costs illustrative. Distinct from BL subjective views and covariance-estimator comparison.

## Minimum viable thesis

Convex robust formulation, plug-in/GMV/equal benchmarks, fixed radius protocol, controlled simulation and monthly historical backtest with net utility and turnover.

## Optional extension

Use bootstrap-based uncertainty sets or add covariance ambiguity, with matched constraints and nested selection.

## Prerequisites

Portfolio theory, convex optimization, statistics and Python/CVXPY.

## Thesis outline

1. Estimation risk and robust optimization;

2. Uncertainty sets and solver;

3. Simulation;

4. Historical backtest;

5. Economic trade-offs.

## Milestones

W1-3: derive robust counterpart; W4-6: solver checks and data; W7-9: controlled simulations; W10-12: OOS and costs; W13-16: robustness and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
