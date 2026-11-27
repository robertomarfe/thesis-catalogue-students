# Research plan | D06.03.01

## Study design and independent work

Reconcile components and proceeds for feasible scenarios; retain infeasible ones. Separate Q prices and P losses. The optional GSW curve is sovereign, not issuer funding or collateral.

## Required tasks

1. Derive replication and feasibility condition; verify call price, par cost and payoff by scenarios.

2. Plot alpha versus rates, maturity, implied vol and fees, including infeasible cells.

3. Compare sensitivities of note value and participation holding contract versus redesigning at issue.

4. Simulate terminal nominal and real (fixed inflation scenario) returns for note, stock and bond, include default loss.

5. Vary hazard and recovery convention in clearly separate scenarios; compare independent default to optional adverse state dependence.

## Required exhibits

Payoff and decomposition diagrams, participation surfaces, feasibility and risk tables, simulated terminal return distributions.

## Robustness

Principal protection holds only at maturity and conditional on issuer performance unless genuinely collateralized. Q fair value and P loss distribution distinct; zero recovery is a scenario. Not investment advice or a dealer quote. Fixed fees and rates are assumptions, not observed spreads.

## Minimum viable thesis

Default-free replication, feasible budget grid and unsecured zero-recovery scenario; no observed structured-note data required. Distinct from D06.03.02's autocallable complexity.

## Optional extension

Compare capped participation, collateralization or alternative market-consistent recovery specification.

## Prerequisites

BSM, discount curves, default intensity basics, simulation.

## Thesis outline

1. Structured payoff and replication;

2. Budget and pricing;

3. Participation comparative statics;

4. Credit and terminal risk;

5. Limitations.

## Milestones

W1-3: derive note price; W4-6: code validation; W7-9: participation and Greeks; W10-12: P payoff/credit scenarios; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
