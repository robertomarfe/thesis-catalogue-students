---
title: "Focused methods — Are Stocks and Bonds Effective Inflation Hedges?"
subtitle: "A04.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For log discount price $p_t(n)=-n y_t(n)$, the log return of an $n$-year zero held for $H$ months is $r^B_{t,t+H}=p_{t+H}(n-H/12)-p_t(n)$.

Use the same fitted nominal curve at both endpoints, $p_t(0)=0$, and no extrapolation. With a flat unchanged curve, return equals $(H/12)y$. Real log holding return equals nominal log holding return minus $\log(I_{t+H}/I_t)$. In identical regressions on realized log inflation the nominal slope minus real slope equals one. Inflation surprise subtracts a forecast available at origin; if the last observed month is $t-1$, forecast through $t+H$ and omit the $t$ term. Distinguish monthly/annual buy-and-hold zeros from rolling constant-maturity strategies; use paired blocks and overlap-aware inference. CPI monthly averages proxy point-in-time prices.

## Research checks

Compute both bond prices for n and n-h using the same documented GSW Svensson convention; verify flat-curve log holding return h*y. Compound monthly gross legs and deflate with exact adjacent CPI; fit inflation AR only on available history, use overlapping-horizon HAC or nonoverlap sensitivity and paired date blocks. Label retrospective hedge exposure, not expected return.
