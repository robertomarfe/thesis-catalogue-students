---
title: "Focused methods — No-Arbitrage Bounds for Contingent Claims in Incomplete Markets"
subtitle: "D11.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Duality and strict feasibility
With unrestricted frictionless portfolios, first verify some $q>0$ satisfies $X^\top q=p$. Closed lower and upper endpoints over $q\ge0$ match respectively the maximum cost $p^\top w$ of subreplicating portfolios $Xw\le H$ and minimum cost of superreplicating portfolios $Xw\ge H$ under finite-state LP feasibility and boundedness. If $H=Xw$, both equal $p^\top w$. The closure optimizer may assign zero probability to a possible state: for an unspanned claim an endpoint need not be arbitrage-free when the claim becomes traded.

## Additional restrictions
Adding consistent asset prices shrinks the feasible set and cannot widen the closed interval. Bid-ask dual bands $p^{bid}\le X^\top q\le p^{ask}$ enlarge the feasible set relative to consistent exact mids; justify their long/short trading interpretation separately. Finite support and numerical tolerances qualify all bounds. Here $q$ is a state-price vector, not a normalized probability.

## Research checks

Verify primal/dual matching, strict feasibility separately, and nested intervals on consistent grids. Report statewise residuals and the role of new payoff directions; do not interpret a failed LP as an economic bound.
