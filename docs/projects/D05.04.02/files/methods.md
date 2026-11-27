---
title: Monte Carlo Greeks — estimators and numerical checks
subtitle: 'Focused methods supplement | D05.04.02'
---
**Synthetic experiment · Decimal volatility · Prices per contract**

## 1. European reference sensitivities

Write $D=e^{-rT}$, $Z=W_T/\sqrt T\sim N(0,1)$, and let $\Phi$ and $\phi$ denote the standard normal CDF and density. Set
$$d_1=\frac{\log(S_0/K)+(r-q+\sigma^2/2)T}{\sigma\sqrt T},\qquad d_2=d_1-\sigma\sqrt T.$$
A call has $\Delta_C=e^{-qT}\Phi(d_1)$ and $\mathcal V_C=S_0e^{-qT}\phi(d_1)\sqrt T$. A cash-or-nothing digital has $V_D=D\Phi(d_2)$, so that
$$\Delta_D=\frac{D\phi(d_2)}{S_0\sigma\sqrt T},\qquad \mathcal V_D=-\frac{D\phi(d_2)d_1}{\sigma}.$$
These formulas provide independent reference values for the European experiment.

## 2. Bump, pathwise and likelihood ratio

For parameter $a\in\{S_0,\sigma\}$ and relative bump $b>0$, use
$$\widehat G_b=\frac{D[H(a(1+b),Z)-H(a(1-b),Z)]}{2ab}.$$
Average across independent draws. The same $Z$ in both terms reduces variance; this does not remove finite-difference bias. The call's pathwise sample contributions are
$$G_{\Delta}^{PW}=D\mathbf1_{\{S_T>K\}}S_T/S_0,$$
$$G_{\mathcal V}^{PW}=D\mathbf1_{\{S_T>K\}}S_T(-\sigma T+\sqrt T Z).$$
Differentiation under the expectation is justified for the continuous call under these assumptions. The digital's individual derivative is zero almost everywhere, although its price derivative need not vanish. It is not a valid estimator here.

For likelihood-ratio estimation, differentiate the lognormal density of the **observed price** holding it fixed. The scores are
$$s_{S_0}=\frac{Z}{S_0\sigma\sqrt T},\qquad s_\sigma=\frac{Z^2-1}{\sigma}-Z\sqrt T.$$
Multiply each score by $DH$ and take its sample mean. Both digital and call payoffs are admissible. A likelihood-ratio estimator may be noisy even if unbiased.

\newpage

## 3. Arithmetic Asian sensitivities

Let $0=t_0<t_1<\cdots<t_m=T$, $\delta t_j=t_j-t_{j-1}$ and $Z_j=(W_{t_j}-W_{t_{j-1}})/\sqrt{\delta t_j}$. The joint density factors into lognormal conditional transition densities. Holding all fixing levels fixed, only the first transition depends directly on $S_0$; every transition contributes to the volatility score:
$$s_{S_0}=\frac{Z_1}{S_0\sigma\sqrt{t_1}},\qquad s_\sigma=\sum_{j=1}^m\left[\frac{Z_j^2-1}{\sigma}-Z_j\sqrt{\delta t_j}\right].$$
For $A=m^{-1}\sum_j S_{t_j}$, the pathwise samples are
$$G_{\Delta}^{PW}=D\mathbf1_{\{A>K\}}A/S_0,$$
$$G_{\mathcal V}^{PW}=\frac{D\mathbf1_{\{A>K\}}}{m}\sum_{j=1}^m S_{t_j}(W_{t_j}-\sigma t_j).$$
The arithmetic payoff kink matters: on a fixed sample, a bump can move paths across the strike. Refine the bump and count crossings; equality with the pathwise derivative for sufficiently small bumps is a diagnostic, not a proof of small population bias. The geometric average admits an analytic lognormal price and may be used as a control.

## 4. Error, uncertainty and cost

For $L$ independent replications $\widehat G_\ell$ and reference $G^*$, report mean error and $\mathrm{RMSE}=\sqrt{L^{-1}\sum_\ell(\widehat G_\ell-G^*)^2}$. For an Asian numerical reference, report its own uncertainty separately; differences smaller than this uncertainty cannot establish a ranking. Time independent replications with the same hardware and exclude unrelated setup. Record both RMSE and elapsed time. Confidence intervals must reflect independent draws or replications, not treat paired antithetic samples as independent.

| Symbol | Code convention |
|:--|:--|
| $S_0,K,T,r,q,\sigma$ | `S, K, T, r, q, sigma` |
| $Z$, $Z_j$ | `z` (one terminal draw or increment array) |
| $b$ | `bump` (relative) |
| $G_\Delta,G_{\mathcal V}$ | `*_delta`, `*_vega` |
| fixing grid | `times` in years; excludes time zero |

Derive and validate the Asian reference, refine path budgets and bump sizes, and complete the original research design independently.
