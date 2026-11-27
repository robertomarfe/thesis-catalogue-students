# Research plan | D04.02.01

## Study design and independent work

Retain small-vega configurations and report unhedged exposures after caps. Compare identical premium, costs and paths; do not treat simulated option liquidity as observed market liquidity.

## Required tasks

1. Verify BSM deterministic variance limit, parity and Greek finite differences; cache/interpolate prices with documented error.

2. Initialize replicating stock/option/cash at target Q price; implement no-external-cash rebalances, close hedge option at target maturity.

3. Compare delta-only (Heston delta) and delta-vega discounted terminal residuals on identical paths.

4. Vary xi, rho, v0, hedge strike and rebalance interval; report variance, expected shortfall, turnover and tail ratios.

5. Test threshold for H_v and capped h_H, with conditioning diagnostics and common-path cost comparisons.

## Required exhibits

Heston pricer checks, hedge exposure panels, P&L distributions, tail/turnover/cost tables, condition-number/vega threshold diagnostics.

## Robustness

This is a coherent simulated market, not evidence of traded option liquidity. A variance derivative is not volatility vega unless consistently rescaled. Distinguish Q pricer accuracy, P simulation bias, discrete hedging and cash-account errors; near-expiry Greeks and small vega can destabilize hedges.

## Minimum viable thesis

One target and two hedge strikes, validated prices and sensitivities, delta versus delta-vega on common paths at two frequencies, cost and ill-conditioning sensitivity. Distinct from single-stock discrete hedging studies.

## Optional extension

Hedge under model misspecification or optimize a constrained minimum-variance hedge with transaction costs.

## Prerequisites

Stochastic calculus, options Greeks, Fourier integration, simulation and Python.

## Thesis outline

1. Heston market and two-factor exposure;

2. Pricer and Greeks;

3. Self-financing simulation;

4. Hedge performance and conditioning;

5. Costs and conclusions.

## Milestones

W1-3: derive hedge ratios; W4-6: validate Heston pricer and DGP; W7-9: cash-ledger hedges; W10-12: sensitivity and costs; W13-16: tests, interpretation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
