---
title: Stochastic net convenience yield — focused methods note
---

**D10.01.02 · Deterministic rates · Risk-neutral valuation**

## 1. Integrated yield and Gaussian law

Fix the observation time $t$ and delivery time $T=t+u$. Suppress time $t$ in conditional quantities. The OU solution is

$$\delta_{t+s}=a+(\delta_t-a)e^{-\kappa s}+\sigma_\delta\int_0^s e^{-\kappa(s-v)}dW^\delta_{t+v}.$$

With $B(s)=(1-e^{-\kappa s})/\kappa$, stochastic Fubini gives

$$\int_t^T\delta_sds=au+(\delta_t-a)B(u)+\sigma_\delta\int_0^u B(u-v)dW^\delta_{t+v}.$$

The terminal log spot is conditionally normal with mean $m=\log S_t+(r-a-\sigma_S^2/2)u-(\delta_t-a)B(u)$ and variance

$$v=\sigma_S^2u+\sigma_\delta^2J(u)-2\rho\sigma_S\sigma_\delta I(u),$$

where the integrals have closed forms

$$I(u)=\int_0^u B(s)ds=\frac{u-B(u)}{\kappa},$$
$$J(u)=\int_0^u B(s)^2ds=\frac{u-2B(u)+B_{2\kappa}(u)}{\kappa^2},$$

and $B_{2\kappa}(u)=(1-e^{-2\kappa u})/(2\kappa)$. These differences may lose numerical precision when $\kappa u$ is very small; quadrature or stable series can be used for checks. Under constant rates the forward equals the conditional mean spot,

$$F_{t,T}=\exp(m+v/2).$$

For deterministic constant yield ($\sigma_\delta=0$, $\delta_t=a$), this reduces to $S_te^{(r-\delta_t)u}$. If the initial yield differs from its long-run mean, a deterministic but time-varying carry remains. This distinction is essential for the constant-carry benchmark.

\newpage

## 2. Independent price verification

Numerical quadrature of $I$ and $J$ provides a reference. Independently evaluate the closed forms above, then generate $\log S_T=m+\sqrt v Z$ with $Z\sim N(0,1)$. For antithetic simulation, average the pair $e^m\cosh(\sqrt v Z)$ and compute the standard error across independent pair means (not across correlated individual draws). This checks marginal prices, not the joint covariance of the forward curve. A separate OU path simulation with correlated innovations is needed to validate the joint dynamics.

## 3. Sensitivities and curve covariance

At fixed delivery,

$$\partial_{\log S_t}\log F_{t,T}=1,\qquad \partial_{\delta_t}\log F_{t,T}=-B(u).$$

The diffusion of the log forward for a fixed delivery is $\sigma_SdW_t^S-B(u)\sigma_\delta dW_t^\delta$. Therefore the instantaneous covariance rate for deliveries $T_i,T_j$ is

$$c_{ij}=\sigma_S^2+B_i B_j\sigma_\delta^2-\rho\sigma_S\sigma_\delta(B_i+B_j).$$

This covariance matrix is positive semidefinite and has rank at most two. It is an instantaneous fixed-delivery result, not the covariance of monthly rolled-futures returns. To compare a one-factor constant-carry curve, choose its carry $c=\log(F_{t,T_1}/S_t)/(T_1-t)$ and compute $S_te^{cu}$ for every delivery. The match at the first delivery is mechanical; differences elsewhere reflect curve shape.

## 4. Notation and code crosswalk

| Symbol | Meaning | Code |
|---|---|---|
| $u$ | Time to delivery, years | `T` in routine |
| $\delta_t,a$ | Net yield, long-run level | `delta`, `a` |
| $\kappa$ | Mean reversion, per year | `k` |
| $\sigma_S,\sigma_\delta$ | Diffusion loadings | `sigS`, `sigd` |
| $B(u)$ | Yield sensitivity magnitude | `B` |

Implement the full grid, independent path simulation, covariance diagnostics and economic interpretation. A synthetic pricing law does not identify physical commodity risk premia.
