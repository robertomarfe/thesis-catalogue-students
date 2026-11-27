---
title: "Focused methods — Implied Volatility Surface Dynamics and Forecasting"
subtitle: "D02.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Fixed coordinates and data provenance
At each observation time $t$, define total implied variance $w_t(k,T)=T I_t(k,T)^2$ at fixed log-forward moneyness $k$ and constant maturity $T$. Use contemporaneous forward and discount inputs and only supported strike/maturity interpolation within a snapshot. Keep observed versus interpolated indicators; never fill missing historical sessions using future data. Vendor-smoothed surfaces and raw quotes are different measurement objects, requiring distinct provenance and permission checks.

## Forecasting the factor representation
Let $x_t$ collect supported total-variance nodes, with training mean $\bar x$ and loading matrix $L_m$. Factor scores for levels are $f_t=L_m^\top(x_t-\bar x)$. An AR or ridge VAR predicts scores at a declared horizon $h$, then reconstructs $\hat x_{t+h}=\bar x+L_m\hat f_{t+h}$. If using changes, reconstruction instead starts from the origin level and adds predicted changes over the horizon. Keep the two estimands separate. Compare persistence and nodewise AR on identical origin-target pairs, with rank and penalties chosen on validation only and purge labels overlapping split boundaries. Report per-node losses, paired block uncertainty, and violations of finite-grid forecast arbitrage restrictions; any projection is a distinct method. Adequate history and authorized access are still blocked.

## Research checks

Do not replace missing market history with a synthetic study without approval. Freeze the supported nodes, complete session calendar, chronological boundaries and purge. Preserve measurement masks and compare the same targets, including failed or arbitrage-violating forecasts.
