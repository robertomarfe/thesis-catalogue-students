# Research plan | D04.01.02

## Study design and independent work

Distinguish explanatory accuracy from D04.01.01's convergence study. Verify the sign on a single ledger, then report paired residuals, RMSE, variance ratio and tail errors normalized by spot as well as dollars.

## Required tasks

1. Derive Taylor/PDE cancellation and check sign on a one-step deterministic ledger.

2. Simulate and compute hedge P&L, pathwise gamma approximation and its conditional variance sum.

3. Compare approximation error, correlation, RMSE and variance ratio across moneyness/maturity cells.

4. Plot time profiles of dollar gamma and error contribution, paying attention to near-expiry behavior.

5. Test finer grids and volatility/drift changes; report independent-replication uncertainty and tail observations rather than dropping them.

## Required exhibits

Tested cash ledger, gamma/error scatterplots, contract-grid heatmaps, predicted versus realized variance tables and approximation residual distributions.

## Robustness

A leading-order expansion is asymptotic, especially delicate near expiry. Avoid using terminal information to compute gamma. Same paths and notional across contracts; no transaction-cost optimization (D04.03.01) or general convergence-only study (D04.01.01).

## Minimum viable thesis

Verified sign and cash ledger, three strikes, three maturities and three nested grids, quantitative approximation accuracy and failure diagnostics.

## Optional extension

Compare a gamma-neutral hedge with a second option under the same diffusion, incorporating the additional rebalancing requirements explicitly.

## Prerequisites

Stochastic calculus, BSM Greeks, Monte Carlo and numerical Python.

## Thesis outline

1. Delta and gamma;

2. Error expansion and conditional variance;

3. Contract-grid simulation;

4. Gamma diagnostics and approximation failure;

5. Implications for risk management.

## Milestones

W1-3: Taylor/PDE derivation; W4-6: ledger and matched paths; W7-9: contract grid and approximation; W10-12: tail and refinement tests; W13-16: interpretation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
