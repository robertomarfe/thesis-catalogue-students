---
title: "Focused methods — Utility Indifference Pricing of Nonreplicable Claims"
subtitle: "D11.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Gaussian certainty equivalent
Let $U(w)=-e^{-\gamma w}$, $\gamma>0$. For Gaussian wealth $Z$, the certainty equivalent is $\mathbb E Z-\gamma\operatorname{Var}(Z)/2$. With zero-cost traded gain $G$ and nontraded claim $H$, write $b=\operatorname{Cov}(H,G)/\operatorname{Var}(G)$ and $s^2=\operatorname{Var}(H)-b^2\operatorname{Var}(G)$. Maximizing the certainty equivalent without the claim gives position $\mathbb E G/(\gamma\operatorname{Var}G)$; selling the claim adds $b$. The resulting seller price is
$$p_{sell}=\mathbb E H-b\mathbb E G+\gamma s^2/2.$$
The buyer valuation subtracts the risk charge. For $H=c+bG$, both equal $c$. In the non-Gaussian finite-state extension, compute expected utility via a stable log-sum-exp and verify optimizer conditions; do not impose the Gaussian formula.

## Interpretation
All values are discounted and $\gamma$ has inverse wealth units. Changing notional changes the unhedgeable risk charge nonlinearly. Physical probabilities and the chosen utility are maintained assumptions, not a unique pricing measure.

## Research checks

Compare numerical certainty-equivalent equality and analytic prices, risk-aversion and correlation sensitivity and scaling. If a nonlinear claim is added, distinguish a preference-dependent value from no-arbitrage bounds.
