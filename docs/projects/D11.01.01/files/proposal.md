---
title: "State Prices and the Fundamental Theorem of Asset Pricing"
subtitle: "Research proposal | D11.01.01"
---

**Derivatives · Credit risk and incomplete markets · Level 1/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

The fundamental theorem connects absence of arbitrage to a positive valuation functional, and completeness to its uniqueness. Finite-state economies allow the link between payoff span, redundancy and pricing consistency to be made explicit and checked by portfolios, not only by solver output.

## Research question

How does changing the payoff span or asset prices affect existence and uniqueness of state prices, replication and the possibility of arbitrage?

## Economic mechanism

For payoff matrix $X\in\mathbb R^{J\times N}$ and price vector $p$, no arbitrage requires $X^\top q=p$ for some $q>0$.

## Research design

Construct the prescribed three- and five-state examples, generate consistent prices from positive state prices, add/remove independent columns and perturb redundant prices. Verify rank, strict feasibility, replication and an explicit arbitrage certificate.

Construct the required four cases and retain actual portfolio certificates, numerical rank and residuals. Vary collinearity and price perturbations. Keep this theorem-focused project distinct from the claim-specific bounds study.

\newpage

## Required exhibits

Payoff matrices, state-price and normalized Q tables, replication weights and residuals, explicit arbitrage certificates, rank/conditioning diagnostics.

## Minimum viable thesis

At least four hand-verifiable economies spanning complete, incomplete, redundant and arbitrage cases, with code certificates and a clear proof sketch of the finite-state theorem.

## Scope and feasibility

A least-squares solution alone does not certify no arbitrage. Strict positivity matters, and tiny epsilon requires numerical checks. Avoid treating objective values of arbitrary LPs as market prices. Distinct from D11.03.01, which centers on bounds for nonreplicable claims rather than FTAP and rank.

**Prerequisites:** Linear algebra, basic probability, introductory derivatives and Python; convex separation can be learned during the project.

**Optional extension:** Add a two-date tree and examine conditional state prices and dynamic completeness, without transaction costs.

## Milestones

W1-3: finite-state theorem and proof; W4-6: hand examples and code; W7-9: completeness and arbitrage certificates; W10-12: conditioning and extensions; W13-16: documentation and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
