---
title: "Focused methods — One-Factor versus Two-Factor Models for Interest Rate Hedging"
subtitle: "D07.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Key-rate and factor exposure
For one unit face of a zero at maturity $\tau_j$, $P_j=e^{-\tau_j y_j}$ and $\partial P_j/\partial y_j=-\tau_j P_j$. A key-rate vector $d$ therefore has currency units per unit decimal yield. For $m$ maturities and $k$ retained PCA factors, $L_k\in\mathbb R^{m\times k}$ and $D\in\mathbb R^{m\times k}$ for $k$ hedge instruments. Use matching yield units and loading normalization when solving the exposure equations.

## Feasible hedges
Inspect rank and conditioning of $L_k^\top D$, apply declared notional limits, and report infeasibility. Estimate only from data available before the evaluated shock. Reprice original quantities under the next curve at fixed maturities; no elapsed holding-period return. Compare residual P&L, omitted-factor and convexity effects and sensitivity to loading estimation.

## Research checks

Do not treat physical PCA loadings as risk-neutral parameters. Unlike D07.01.02, compare statistical factor spanning with zero-bond hedges rather than single-curve swap DV01.
