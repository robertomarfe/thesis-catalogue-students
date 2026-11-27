# Research plan | D08.01.01

## Study design and independent work

Verify the diffusion limit and jump moments, isolate monitoring, jump and option-strip errors, and report MC intervals even if a small correction is unresolved.

## Required tasks

1. Derive analytical expectations of sampled variance, continuous QV and log-contract payoff.

2. Verify Q martingale numerically and compare simulated fair strikes to exact expressions with MC uncertainty.

3. Decompose log-contract minus discrete fair strike into jump and sampling terms across scenarios; contrast the direction of each.

4. Approximate the log contract via OTM option integration using analytic or independently converged jump-mixture prices; vary strike truncation and quadrature density so integration bias is not confused with monitoring bias.

## Required exhibits

Table of fair strikes, MC errors and confidence intervals, monitoring-frequency convergence figures, jump correction plots and strip integration convergence. Include exact GBM baseline and at least one compound-Poisson case with economically interpreted variance notional.

## Robustness

Use common nested increments when comparing monitoring frequency; independent seeds for uncertainty checks. Maintain risk-neutral compensator, payoffs in log-return variance and exact contract convention. Distinguish quadratic variation, log-contract price, variance risk premium and volatility swap; no calibration to traded quotes.

## Minimum viable thesis

Exact GBM and jump formulas with independent simulation validation; at least two frequencies and jump scenarios, decomposition and numerical log-contract/option-strip illustration. Report MC uncertainty even if bias is not statistically resolvable.

## Optional extension

Add stochastic volatility or explore daily return conventions, business-day versus calendar scaling and discretization under stochastic rates.

## Prerequisites

Ito calculus, risk-neutral pricing, compound Poisson processes, Monte Carlo and numerical integration.

## Thesis outline

1. Variance derivatives and replication;

2. Diffusion and jump model fair strikes;

3. Simulation and quadrature design;

4. Monitoring and jump correction results;

5. Contract limitations.

## Milestones

W1-3: derive variance/log-contract formulas; W4-6: implement and test exact increments; W7-10: run pricing and integration grids; W11-13: convergence and jump sensitivity; W14-16: interpretation and thesis.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
