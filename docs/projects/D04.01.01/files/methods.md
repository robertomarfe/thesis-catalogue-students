---
title: Discrete delta hedging — focused methods note
---

**D04.01.01 · Synthetic diagnostic · Companion to the research proposal**

## 1. Pricing and simulation are different operations

Under $\mathbb P$, the exact stock transition over $\delta t_j=t_{j+1}-t_j$ is

$$S_{t_{j+1}}=S_{t_j}\exp\{(\mu-\sigma^2/2)\delta t_j+\sigma\sqrt{\delta t_j}Z_j\},\quad Z_j\sim N(0,1).$$

Pricing uses $\mathbb Q$ with drift $r$. For $\tau=T-t>0$, set $d_1=[\log(S/K)+(r+\sigma^2/2)\tau]/(\sigma\sqrt\tau)$ and $d_2=d_1-\sigma\sqrt\tau$. Then

$$C=S\Phi(d_1)-Ke^{-r\tau}\Phi(d_2),\qquad \Delta=\Phi(d_1),\qquad \Gamma=\frac{\phi(d_1)}{S\sigma\sqrt\tau}.$$

Here $\Phi$ and $\phi$ denote the standard normal cdf and density. Avoid computing delta or gamma at $\tau=0$. Terminal liquidation is not a new hedge decision.

## 2. Two equivalent cash ledgers

Let $\widetilde S_j=e^{-rt_j}S_{t_j}$, and let $h_j^{S}$ be the shares held from $t_j$ to $t_{j+1}$. In a frictionless market, discounted terminal seller's error equals

$$E=C(0,S_0)+\sum_{j=0}^{n-1}h_j^{S}(\widetilde S_{j+1}-\widetilde S_j)-e^{-rT}(S_T-K)^+.$$

This telescoping gains representation and the cash-account recursion in the proposal must agree path by path. Verify the identity using a separate implementation before interpreting simulations. Implement both representations separately.

The discounted traded notional, with liquidation, is

$$U=|h_0^{S}|S_0+\sum_{j=1}^{n-1}|h_j^{S}-h_{j-1}^{S}|\widetilde S_j+|h_{n-1}^{S}|\widetilde S_n.$$

It is not a cost unless multiplied by a specified fee. Keep fee optimization out of this thesis's baseline.

\newpage

## 3. Local gamma error and convergence

Use the Black--Scholes PDE $C_t+rSC_S+\tfrac12\sigma^2S^2C_{SS}=rC$ and a second-order Taylor expansion. Over one hedge interval, the change in option value minus the change in the delta-and-cash portfolio is approximately $\tfrac12\Gamma_j[(S_{j+1}-S_j)^2-\sigma^2 S_j^2 \delta t_j]$. Thus the leading seller's terminal error is

$$E_\Gamma=-\frac12\sum_{j=0}^{n-1}e^{-rt_{j+1}}\Gamma_j[(S_{j+1}-S_j)^2-\sigma^2S_j^2\delta t_j].$$

The approximation omits higher-order terms and is not an exact replication identity. High gamma near expiry can make finite-grid behavior depart from the asymptotic picture. Test the approximation against the exact ledger, not against another Taylor expansion.

For $M$ paths, report $\widehat{\mathrm{RMSE}}=\sqrt{M^{-1}\sum_{i=1}^{M} E_i^2}$. The convergence reference $n^{-1/2}$ is illustrative under regularity, not a fitted restriction. Replicate the entire experiment on independent path samples to assess uncertainty in slopes and tail statistics. Nested grids enable paired comparisons: frequencies must not use unrelated paths.

## 4. Notation and code crosswalk

| Symbol | Meaning | Code |
|---|---|---|
| $t_j$ | Time grid, years | `times` |
| $S_{t_j}$ | Stock price, currency | `spots` |
| $h_j^S$ | Shares held over next interval | `holdings` |
| $E$ | Discounted gain to short-call seller | `error` |
| $U$ | Discounted stock traded notional | `stock_turnover` |
| $n$ | Number of hedge intervals | `n` |

## 5. Starter boundary

Implement the prescribed scenario grid, independent replications, distribution and gamma diagnostics; do not choose the sample solely because the slope looks favorable. All inputs are simulated and no external market dataset is needed.
