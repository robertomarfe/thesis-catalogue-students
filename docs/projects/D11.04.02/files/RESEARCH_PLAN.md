# Research plan | D11.04.02

## Study design and independent work

Compare numerical certainty-equivalent equality and analytic prices, risk-aversion and correlation sensitivity and scaling. If a nonlinear claim is added, distinguish a preference-dependent value from no-arbitrage bounds.

## Required tasks

1. Derive Gaussian indifference price, buyer-seller spread and hedge.

2. Implement independent numerical utility optimization against closed form.

3. Vary correlation, gamma and market Sharpe ratio with common inputs.

4. Compare nonlinear finite-state prices to bounds and minimum-variance hedge, check no-arbitrage and replicability limits.

5. Report sensitivity to payoff scale and physical probabilities, not a unique market price.

## Required exhibits

Price and hedge surfaces, buyer-seller spread, exact-versus-numeric residuals, payoff-state diagram, sensitivity to nontraded risk.

## Robustness

Do not treat P as Q; utility prices can differ across agents and order sizes. Use discounted payoffs consistently; exclude position constraints from the analytic benchmark. Utility specification and endowment are maintained assumptions.

## Minimum viable thesis

Gaussian derivation and independent optimizer, replicability limit, risk-aversion and correlation sensitivity, one nonlinear finite-state claim if time permits.

## Optional extension

Study random initial endowment and the interaction with the nontraded claim using joint finite-state probabilities.

## Prerequisites

Expected utility, asset pricing, Gaussian moments, convex optimization.

## Thesis outline

1. Incomplete-market pricing;

2. Utility and Gaussian formula;

3. Numerical method;

4. Comparative statics and nonlinear example;

5. Interpretation.

## Milestones

W1-3: derivation; W4-6: certainty-equivalent and optimizer tests; W7-9: sensitivities; W10-12: finite-state case; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
