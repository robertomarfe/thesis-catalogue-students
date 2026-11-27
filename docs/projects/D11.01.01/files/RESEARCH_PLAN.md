# Research plan | D11.01.01

## Study design and independent work

Construct the required four cases and retain actual portfolio certificates, numerical rank and residuals. Vary collinearity and price perturbations. Keep this theorem-focused project distinct from the claim-specific bounds study.

## Required tasks

1. Solve a complete three-state example by hand and match code.

2. Compute rank, null spaces and state-price solutions in incomplete and redundant economies; verify sum and positivity.

3. Price and replicate a spanning claim and test a nonspanning one via projection residual.

4. Introduce inconsistent prices and construct a zero or negative cost portfolio with nonnegative payoff and a strict gain (including free initial proceeds). Verify feasibility directly.

5. Vary payoff collinearity and price perturbations; report conditioning and numerical tolerance.

## Required exhibits

Payoff matrices, state-price and normalized Q tables, replication weights and residuals, explicit arbitrage certificates, rank/conditioning diagnostics.

## Robustness

A least-squares solution alone does not certify no arbitrage. Strict positivity matters, and tiny epsilon requires numerical checks. Avoid treating objective values of arbitrary LPs as market prices. Distinct from D11.03.01, which centers on bounds for nonreplicable claims rather than FTAP and rank.

## Minimum viable thesis

At least four hand-verifiable economies spanning complete, incomplete, redundant and arbitrage cases, with code certificates and a clear proof sketch of the finite-state theorem.

## Optional extension

Add a two-date tree and examine conditional state prices and dynamic completeness, without transaction costs.

## Prerequisites

Linear algebra, basic probability, introductory derivatives and Python; convex separation can be learned during the project.

## Thesis outline

1. One-period markets and arbitrage;

2. State prices, separation and FTAP;

3. Numerical linear algebra and LP;

4. Experiments on market span;

5. Economic interpretation.

## Milestones

W1-3: finite-state theorem and proof; W4-6: hand examples and code; W7-9: completeness and arbitrage certificates; W10-12: conditioning and extensions; W13-16: documentation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
