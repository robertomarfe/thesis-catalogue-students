# Research plan | D07.02.02

## Study design and independent work

Freeze the ATM match before comparing other strikes; report domain and uncertainty rather than forcing implied volatilities for zero prices. Distinct from A05.01.01 physical transition estimation.

## Required tasks

1. Derive bond prices and shift, verify initial curve and forward option parity.

2. Implement Gaussian analytic and CIR reference pricers, compare MC with time-step refinement.

3. Match ATM price by one volatility parameter; report unmatched cases.

4. Compare price/forward-moneyness grids, implied Black vol where defined and finite-difference rate sensitivities.

5. Stress low initial rates, negative shifted rates and large volatility; keep expiry/delivery fixed. Compare parallel initial-zero-curve sensitivities for at least one ATM and one non-negligible OTM option; keep contractual strike and stochastic parameters fixed and refit only the deterministic curve shift. Treat shifted-CIR support restrictions as structural zeros.

## Required exhibits

Curve fit table; parity and MC error table; option price and implied volatility plots; Greek and tail-scenario comparisons. Bump-convergence table and sensitivity per basis point; document unmatched prices and structural zeros.

## Robustness

Match curves and ATM price before attributing differences to diffusion. Shifted CIR need not have positive total rates. Do not infer Q parameters from P estimates. Use CIR boundary/Feller diagnostics; distinguish bond option from caplet.

## Minimum viable thesis

Two affine models on the same synthetic curve, analytic/Monte Carlo cross-check, one ATM price match and option smile comparison; compare at least one ATM and one non-negligible OTM parallel zero-yield sensitivity with strike and stochastic parameters frozen and deterministic curve fitting updated. Report convergence in bump size, pricing-domain failures and unmatched cases. Distinct from A05.01.01 (physical rate dynamics).

## Optional extension

Compare caplets or Jamshidian swaption decomposition under one-factor dynamics.

## Prerequisites

Stochastic calculus, affine processes, fixed-income pricing, Python.

## Thesis outline

1. No-arbitrage bond pricing;

2. Vasicek and CIR;

3. Bond options and matching;

4. Numerical study;

5. Model risk.

## Milestones

W1-3: affine derivations; W4-6: reference pricers; W7-9: matching and validation; W10-12: scenarios and Greeks; W13-16: write and reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
