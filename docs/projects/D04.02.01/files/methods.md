---
title: "Focused methods — Delta-Vega Hedging under Stochastic Volatility"
subtitle: "D04.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Spanning two innovations
Under Q, $dS/S=(r-q)dt+\sqrt v\,dW_S$ and $dv=\kappa_Q(\theta_Q-v)dt+\xi\sqrt v\,dW_v$, with correlation $\rho$. Match stock and variance derivatives through
$$\begin{pmatrix}1&H_S\\0&H_v\end{pmatrix}\binom{h_S}{h_H}=\binom{C_S}{C_v}.$$
For positive variance and vol-of-vol, $|\rho|<1$ and $H_v\ne0$, this spans both shocks locally. Variance and volatility derivatives differ by $C_{\sqrt v}=2\sqrt v C_v$. Condition numbers depend on units: scale exposure columns before comparison.

## Valuation and execution
Use Q for prices and Greeks, P for realized paths, and a self-financing cash ledger with costs. Close the longer-dated hedge option at its residual-maturity value when the target expires. Separate pricing, Greek, interpolation and path-discretization errors.

## Research checks

Retain small-vega configurations and report unhedged exposures after caps. Compare identical premium, costs and paths; do not treat simulated option liquidity as observed market liquidity.
