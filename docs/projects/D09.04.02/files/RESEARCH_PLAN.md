# Research plan | D09.04.02

## Study design and independent work

Check marginal survival at all grid dates, exposure distributions, paired loss differences and grid refinement; distinguish dependence from changes in hazard or recovery. Contrast long and short forwards. A common latent horizon across maturities is a possible redesign, not part of the current frozen scope.

## Required tasks

1. Validate clean forward and marginal default survival against exp(-lambda t).

2. Reproduce independent CVA from analytic lognormal EPE and default increments.

3. Estimate paired CVA change under the copula with unchanged marginals and uncertainty intervals.

4. Study exposure at default, maturity and rare-default Monte Carlo error.

5. Decompose change from dependence versus separate hazard/recovery sensitivity and contrast long/short forward.

## Required exhibits

Survival and EPE checks, CVA by rho in bp of notional, exposure-at-default and paired MC interval plots, grid convergence.

## Robustness

Latent terminal shock construction is an ex-ante joint law, not an adapted intensity or a dynamic trading model; no claim about real counterparty correlations. Conditional exposure at default differs from EPE. No bilateral DVA, collateral or funding; use the same closeout convention.

## Minimum viable thesis

Independent-CVA benchmark and fixed-marginal dependence sensitivity for one forward, with sign convention, marginal checks and confidence intervals.

## Optional extension

Replace the copula with a Cox intensity driven by adapted market states, recalibrating deterministic baseline to preserve marginal survival before comparing.

## Prerequisites

Risk-neutral pricing, copulas, credit risk, probability and MC.

## Thesis outline

1. Unilateral CVA and exposure;

2. Joint default/exposure law;

3. Independent benchmark;

4. Wrong-way experiments;

5. Model risk.

## Milestones

W1-3: CVA derivation and dependence design; W4-6: analytic exposure and survival checks; W7-9: paired simulation; W10-12: grid and rare-event tests; W13-16: documentation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
