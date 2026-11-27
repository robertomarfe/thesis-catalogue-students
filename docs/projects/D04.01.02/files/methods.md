---
title: "Focused methods — The Role of Gamma in Delta-Hedging Errors"
subtitle: "D04.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Curvature and replication
For matched BSM parameters and no dividends, the PDE gives $C_t+rSC_S+\sigma^2S^2C_{SS}/2-rC=0$. Subtract the second-order expansion of the claim from stock and cash gains, with $\Gamma=C_{SS}$. The leading discounted increment is
$$e_{i+1}\simeq-\tfrac12 e^{-rt_i}\Gamma_i S_i^2\sigma^2[(\Delta W_i)^2-h].$$
The centered square has conditional variance $2h^2$. The predictable variance sum of the leading martingale approximation is $\sum_i e^{-2rt_i}\Gamma_i^2S_i^4\sigma^4h^2/2$. Its expectation describes the variance of the approximate error, not exact conditional terminal variance.

## Failure diagnostics
Use the exact ledger as primary error. Gamma must be evaluated before the step. Near expiry, derivatives vary sharply; the approximation need not describe tails. Right-end discount differs at higher order: label and test it against left-end discount.

## Research checks

Distinguish explanatory accuracy from D04.01.01's convergence study. Verify the sign on a single ledger, then report paired residuals, RMSE, variance ratio and tail errors normalized by spot as well as dollars.
