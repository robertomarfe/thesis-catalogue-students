---
title: "Focused methods — Downside versus Upside Market Risk in Factor Investing"
subtitle: "A07.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Asymmetric regression
In up markets the conditional intercept and slope are $(a,b)$; in down markets they are $(a+c,b+d)$. Including the indicator itself prevents a forced equal intercept. Estimate the two state-specific regressions as a check. Summarize conditional means, dispersions and lower partial moments about a declared threshold. Long-short factor payoffs are already spreads; do not subtract RF a second time.

## Inference
The state is contemporaneous, not observable before the month's return. Use common dates and the required minimum count per state. Estimate joint confidence intervals or multiplicity-adjusted tests across factors, preserving common month blocks; inspect rolling estimates without treating overlapping windows as independent. A slope difference describes payoff asymmetry, not necessarily an independently priced factor.

## Research checks

Prespecify the sign cutoff and rolling windows. Report all factors, state counts and crisis sensitivity; distinguish conditional descriptive analysis from a trading signal or a pricing test.
