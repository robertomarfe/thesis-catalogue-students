---
title: "Cash Flow News and Discount Rate News in Aggregate Stock Returns"
subtitle: "Research proposal | A06.04.02"
---

**Asset pricing · Consumption-based asset pricing and equity term structures · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Unexpected returns can reflect revisions in future cash flows or discount rates. A VAR provides one operational decomposition whose dependence on information and horizon is itself a research object.

## Research question

How much of unexpected aggregate equity return variation is associated with discount-rate versus cash-flow news under alternative parsimonious VAR information sets?

## Economic mechanism

For centered return-first VAR $X_{t+1}=AX_t+u_{t+1}$, discount-rate news at horizon $H$ is $N_{DR}=e_1^\top\sum_{j=1}^H\rho^j A^j u_{t+1}$.

## Research design

Goyal real annual return-first VAR with dividend-price and short rate, alternative term spread; finite 5/10/20 and stable long-run decomposition with uncertainty.

Use return-first VAR, stable roots, same calendar and real gross convention; verify direct discounted sums and signed Var(CF)+Var(DR)-2Cov identity, report finite and infinite estimates, horizon and information-set sensitivity. Refit rho and VAR inside bootstrap, retain inadmissible draws and note weak stability near unit roots.

\newpage

## Required exhibits

VAR estimates and eigenvalues, time series of both news components, variance decomposition including covariance term, intervals and finite-horizon robustness.

## Minimum viable thesis

One stable annual VAR, exact algebra checks, news series, variance/covariance table, finite versus infinite horizon and two information sets with uncertainty.

## Scope and feasibility

Infinite sum requires spectral radius of rho*A below one; near-unit-root results fragile. Residual N_CF not a structural cash-flow shock and absorbs omitted news and approximation error; no causal attribution. Annual sample modest; avoid many predictors and do not impose nonnegative variance shares. Distinct from A06.01.02 forecast-level decomposition of valuation ratios.

**Prerequisites:** Asset valuation, VAR, matrix algebra, bootstrap and Python.

**Optional extension:** Use a richer monthly VAR with explicit cash-flow proxy and compare with a direct dividend-growth forecast system or GKK equity duration.

## Milestones

W1-3: derive news formulas; W4-6: construct annual data; W7-9: VAR and decomposition; W10-12: bootstrap and robustness; W13-16: interpret and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
