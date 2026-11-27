---
title: "Focused methods — Recovering Risk-Neutral Densities from Option Prices"
subtitle: "D11.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Distribution identities
For deterministic rates, the right derivative $-c'_+(k)=\Pr(x>k)$; the second derivative is the distribution as a measure, and a density only if absolutely continuous. At normalized forward one, $c(0)=1$, $c$ is decreasing and convex, and slope is in $[-1,0]$. For a discrete grid $x_j\ge0$ and weights $w_j$,
$$\widehat c(k_i)=\sum_j w_j(x_j-k_i)^+,$$
$$w_j\ge0,\quad\sum_j w_j=1,\quad\sum_jx_jw_j=1.$$
Smoothness penalties depend on grid spacing; on a nonuniform grid distinguish mass from density. A convex fitted slice alone does not identify the full tail outside observed strikes.

## Validation
Report quote error, probability mass, first moment, density/measure discrepancies and tail CDF errors relative to the known synthetic truth. Repeat noise draws and support endpoints; report whether extrapolation rather than observed prices drives the result.

## Research checks

Do not silently clip negative density estimates and call them calibrated distributions. Track feasibility, normalization, tail sensitivity and uncertainty across the prescribed grids. Distinguish distribution recovery from smile interpolation.
