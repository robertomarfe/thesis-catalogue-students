---
title: "Focused methods — Habit, Risk Aversion and the Volatility of Asset Prices"
subtitle: "A03.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For a symmetric two-state Markov chain with stay probability $p$, the stationary law is $(1/2,1/2)$ for $0<p<1$, and the nontrivial eigenvalue is $2p-1$.

Use $m=\beta(G S_{t+1}/S_t)^{-\gamma}$ and $R=G(1+v_j)/v_i$. The law of total variance gives $\operatorname{Var}(R)=E[\operatorname{Var}(R\mid i)]+\operatorname{Var}(E[R\mid i])$. Changing persistence changes the feasible shock-surplus coupling; report actual covariance at each cell. The stationary log price-ratio variance and gross return variance are distinct. Compare independent coupling and constant surplus, not just high versus low persistence.

## Research checks

For every persistence value record transition probabilities, realized conditional shock-surplus covariance, stationary law, mean and SD of log P/D, conditional rate and premium, and stationary second moments including between-state variation. Compare independent-coupling and constant-surplus controls; independently simulate one interior case with burn-in and MC uncertainty.
