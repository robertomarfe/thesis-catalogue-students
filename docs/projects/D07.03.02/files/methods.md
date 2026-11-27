---
title: Hull–White swaption pricing — focused methods note
---

**D07.03.02 · Single-curve, one-factor model · Unit notional**

## 1. Initial curve and Gaussian factor

Define $B_a(s)=(1-e^{-as})/a$ and $f_0(t)=-\partial_t\log P(0,t)$. The short rate is $r_t=x_t+\varphi(t)$, $dx_t=-a x_tdt+\sigma dW_t^{\mathbb Q}$, $x_0=0$, with

$$\varphi(t)=f_0(t)+\frac{\sigma^2}{2}B_a(t)^2.$$

For exercise $u$, let $I_u=\int_0^u x_sds$. The pair $(x_u,I_u)$ is centered Gaussian with

$$v_x=\sigma^2B_{2a}(u),\quad c_{xI}=\frac{\sigma^2}{a}[B_a(u)-B_{2a}(u)],$$
$$v_I=\frac{\sigma^2}{a^2}[u-2B_a(u)+B_{2a}(u)].$$

Consequently $D_u=\exp(-\int_0^u r_s ds)=P(0,u)\exp(-I_u-v_I/2)$. This gives a direct money-market-measure simulation without a short-rate Euler scheme. Under the $u$-forward measure, $x_u$ is normal with mean $-c_{xI}$ and variance $v_x$.

A convenient conditional bond formula is

$$P(u,T)=\frac{P(0,T)}{P(0,u)}\exp\{-B_a(T-u)(x_u+c_{xI})-\tfrac12 B_a(T-u)^2v_x\}.$$

In particular $P(0,T)$ is recovered exactly. The one-factor Gaussian structure admits negative short rates even when the initial curve is positive.

## 2. Swap and payer option

Let $A_u=\sum_i\alpha_iP(u,T_i)$ and $S_u=(1-P(u,T_m))/A_u$. With physically settled payoff and contractual strike $K$, set $c_i=K\alpha_i+\mathbf 1_{i=m}$. The payer exercise value is $(1-\sum_i c_iP(u,T_i))^+$. For $K\ge0$, the coupon-bond value is strictly decreasing in $x_u$ and the exercise root $x^*$ solves $\sum_i c_iP(u,T_i;x^*)=1$.

\newpage

## 3. Jamshidian decomposition and independent check

Set $k_i=P(u,T_i;x^*)$. Since all bond prices fall together with the factor,

$$(1-\sum_i c_iP(u,T_i))^+=\sum_i c_i[k_i-P(u,T_i)]^+.$$

Each term is a bond put. Under the $u$-forward measure its lognormal standard deviation is $B_a(T_i-u)\sqrt{v_x}$; discount by $P(0,u)$. The `swaption_hw` routine uses this decomposition. Independently simulate $(x_u,I_u)$ under $\mathbb Q$ and average $D_u(1-\sum_i c_iP(u,T_i))^+$. For quadrature under the forward measure, split at $x^*$; crossing the payoff kink can distort numerical integration.

The payer minus receiver price equals $P(0,u)-P(0,T_m)-KA_0$, where $A_0=\sum_i\alpha_iP(0,T_i)$. At zero volatility the payer price is the positive part of that quantity. The normal implied volatility is defined by matching the price to $A_0[(F-K)\Phi(d)+\sigma_N\sqrt u\,\phi(d)]$ with $F=[P(0,u)-P(0,T_m)]/A_0$ and $d=(F-K)/(\sigma_N\sqrt u)$. At intrinsic value use the zero-volatility limit.

## 4. Sensitivities and units

For a volatility bump $\epsilon$, the centered sensitivity is $[V(\sigma+\epsilon,K)-V(\sigma-\epsilon,K)]/(2\epsilon)$. Keep $K$ fixed. A parallel curve bump $b$ replaces $P(0,T)$ by $P(0,T)e^{-bT}$ and refits $\varphi$ while keeping $a,\sigma,K$ fixed. Do not recompute ATM strike after either bump. Price basis points are $10^4 V$ per unit notional; rate basis points are $10^4$ times a decimal rate. State units for every table.

## 5. Notation and code crosswalk

| Symbol | Meaning | Code |
|---|---|---|
| $u,T_i$ | Exercise and payments, years | `expiry`, `dates` |
| $P(0,T)$ | Discount factor | `p0` |
| $a,\sigma$ | Mean reversion and rate vol | `a`, `sigma` |
| $K$ | Contractual fixed rate | `strike` |
| $x_u,I_u$ | Joint Gaussian state and integral | `x`, `integral` |

Implement fixed-strike risks, two curves, full expiry–tenor and strike grids, independent replications and identification yourself.
