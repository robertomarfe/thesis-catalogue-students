---
title: "Focused methods — Limits to Arbitrage and the Persistence of Mispricing"
subtitle: "A12.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

Let $d=P-F$, noise demand $n-\beta d$, arbitrage $x=\operatorname{clip}(-d/a,-K,K)$; clearing is $n-\beta d+x=0$.

Interior $d=n/(\beta+1/a)$, binding $d=(n+x)/\beta$. Verify continuity, independent scalar root and cap limits. Liquidation at known F is imposed. Wealth changes by position times price change, not a preference penalty unless explicitly charged. Gaussian noise may give nonpositive prices; report all invalid rates and label conditional results.

## Research checks

Verify analytical regime boundaries, continuity and clearing with independent scalar root solution; verify trading gains and wealth identities including cap=0/infinity. Use matched noise and report binding rates, loss/negative wealth and invalid price rates for every cell. Full 50k-path experiment and endogenous wealth constraint remain student work.
