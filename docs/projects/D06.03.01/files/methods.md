---
title: "Focused methods — Pricing and Risk Decomposition of Capital-Protected Notes"
subtitle: "D06.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Floor and participation
The stylized maturity payoff is $N[b+\alpha(S_T/S_0-1)^+]$ conditional on issuer performance. With deterministic discount $D$ and call $C$ of strike $S_0$, default-free value is $N[bD+\alpha C/S_0]$. Net proceeds are $N(1-f)$. Solve the budget only for positive call value and nonnegative residual proceeds. A floor alone costing more than net proceeds is infeasible, not negative participation. Fees are upfront wedges.

## Credit and physical risk
Independent constant pricing intensity $\lambda_Q$ with zero recovery multiplies both components by $e^{-\lambda_QT}$. A cheaper survival-contingent floor can allow more advertised participation but lower repayment reliability. Physical drift and intensity are separate scenario inputs. Protection applies at maturity, conditional on performance, not to interim value or unsecured default. This is a stylized model, not a dealer quote.

## Research checks

Reconcile components and proceeds for feasible scenarios; retain infeasible ones. Separate Q prices and P losses. The optional GSW curve is sovereign, not issuer funding or collateral.
