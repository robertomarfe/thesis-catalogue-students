---
title: "Risk-Neutral Probabilities and Change of Numeraire"
subtitle: "Research proposal | D11.01.02"
---

**Derivatives · Credit risk and incomplete markets · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Stochastic discounting makes the choice of pricing measure economically meaningful but not a source of pricing disagreement. A change of numeraire reallocates probability weights to make a different traded unit the reference asset. Verify the equivalence locally, including self-financing replication.

## Research question

How can one verify that money-market and forward-measure valuation give identical prices even when interest rates are stochastic?

## Economic mechanism

For positive traded numeraires $B,N$, $V_t=B_t\mathbb E_t^{\mathbb Q^B}[H_T/B_T]=N_t\mathbb E_t^{\mathbb Q^N}[H_T/N_T]$.

## Research design

Build the prescribed nonrecombining two-period tree with the stated money-market accrual and terminal stock payoffs. Compute intermediate bond and stock values consistently and transform transitions for the forward and stock numeraires. Compare claim values and replication residuals at every node.

Check all three measure transformations at every node, local payoff rank, transition sums, price equality and replication residuals. Extend only after the two-period benchmark is independently reproduced.

\newpage

## Required exhibits

Annotated tree, transition and density tables, claim-price invariance residuals, replication check and rate-dependence illustrations.

## Minimum viable thesis

Complete two-period example, money-market/forward/stock measure transformations, at least three claim types, nodewise pricing equality and replication residuals below numerical tolerance.

## Scope and feasibility

Numeraires must be strictly positive self-financing traded assets. B is path dependent with stochastic rates; no arbitrary renormalization or P probabilities substituted for Q. Nonrecombination is acceptable; verify local martingales before computing measures.

**Prerequisites:** Conditional probability, discrete-time asset pricing, linear algebra and Python.

**Optional extension:** Use a longer short-rate tree and price a bond option or caplet with an appropriate forward measure.

## Milestones

W1-3: derive pricing and RN density; W4-6: build and check tree; W7-9: measure changes and claims; W10-12: rate-dependence and diagnostics; W13-16: proofs, code and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
