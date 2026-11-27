---
title: "Focused methods — Risk-Neutral Probabilities and Change of Numeraire"
subtitle: "D11.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Change of measure
For a strictly positive self-financing traded numeraire $N$, the Radon--Nikodym density under the money-market measure is
$$L_T=\frac{N_T/B_T}{N_0/B_0}.$$
Since $N/B$ is a $\mathbb Q^B$ martingale, for child $j$ of node $i$ the transition is $p^N_{ij}=p^B_{ij}(N_j/B_j)/(N_i/B_i)$. Verify positive probabilities summing to one nodewise. In the $T$-bond measure $N_T=1$, so the payoff is measured in units of the bond and $V_t=P(t,T)\mathbb E_t^{\mathbb Q^T}[H_T]$.

## Replication and consistency
Use the node's stock and locally riskless money-market investment to solve the two child payoff equations whenever the local payoff matrix is nonsingular. The portfolio cost must agree with each measure's conditional valuation. A stock numeraire must be positive and tradable including reinvested cash flows; the design has no dividends. Do not discount by the initial constant rate when future short rates differ by node.

## Research checks

Check all three measure transformations at every node, local payoff rank, transition sums, price equality and replication residuals. Extend only after the two-period benchmark is independently reproduced.
