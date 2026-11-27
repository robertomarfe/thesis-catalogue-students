---
title: "Focused methods — State Prices and the Fundamental Theorem of Asset Pricing"
subtitle: "D11.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Positive valuation and span
Rows of $X$ are states and columns are assets; all states are possible. With unrestricted frictionless trading and a strictly positive bond, no arbitrage is equivalent to $X^\top q=p$ for some strictly positive state-price vector $q$. With a unit payoff bond of price $B_0$, $\sum_j q_j=B_0$ and pricing probabilities are $q_j/B_0$. If $\operatorname{rank}X=J$ the market spans all claims and $q$ is unique when consistent. Redundant assets impose price restrictions even in incomplete markets.

## Certificates
For a spanning claim $H=Xw$, price is $p^\top w=q^\top H$. Test numerical rank using scale-aware singular values. Strict feasibility can be assessed by maximizing $\epsilon$ subject to $X^\top q=p$, $q_j\ge\epsilon$, $q\ge0$. A boundary feasible vector with zero entries alone does not establish no arbitrage. If consistency fails, find and verify a portfolio with nonpositive initial cost, nonnegative state payoffs and a strict gain (including initial proceeds).

## Research checks

Construct the required four cases and retain actual portfolio certificates, numerical rank and residuals. Vary collinearity and price perturbations. Keep this theorem-focused project distinct from the claim-specific bounds study.
