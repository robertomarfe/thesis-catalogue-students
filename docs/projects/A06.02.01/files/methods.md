---
title: "Focused methods — The Term Structure of Equity Yields: Evidence from Synthetic Dividend Strips"
subtitle: "A06.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For positive dividend normalization $D_t$, let $P_t^{(n)}$ price the dividend at maturity $n$. Define $e_t(n)=-n^{-1}\log(P_t^{(n)}/D_t)$.

Match continuously compounded nominal zero yields $b_t(n)$ and equity yields only after checking the provider definitions. The difference $f_t(n)=e_t(n)-b_t(n)$ is a bond-adjusted equity yield, not a forward rate between maturities and not an expected excess return: growth is embedded. Use centered PCA on complete common maturity dates with a fixed sign convention. Inference on generated curves is conditional on their estimation, not independent validation of strip prices.

## Research checks

Verify archive/version and Eq.32/33, complete 1-15 annual maturity grid, positive dividend normalization and decimals, exact common month-end GSW SVENY, not par yields. Report common sample, model-implied caveat, slope and fixed curvature definition, centered PCA with sign convention and recession episode counts. Inference conditional on estimated curves; no independent validation of the underlying GKK estimator.
