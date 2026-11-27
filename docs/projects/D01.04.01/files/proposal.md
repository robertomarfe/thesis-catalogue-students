---
title: Option Pricing with Lévy Processes — Beyond Gaussian Returns
subtitle: 'Research proposal | D01.04.01'
---

**Derivatives · Advanced option pricing · 16 weeks · Level 3/3**  
**Data:** synthetic. **Status:** current draft; not approved for assignment.

## Motivation

In the Black–Scholes model, the same volatility parameter prices European options of all strikes and maturities. Exponential Lévy models relax Gaussianity while retaining independent, stationary increments. A comparison at a common forward and log-return variance isolates differences in higher cumulants and their consequences for the option smile. The aim is not to fit market quotes, but to establish what different jump mechanisms imply for prices and for numerical accuracy in a controlled experiment.

## Research question

Can variance-gamma and finite-activity jump models with comparable variance reproduce different strike and maturity patterns, and which pricing properties are robust to tail and discretization choices?

## Model and economic mechanism

Let $S_0$ denote the spot, $r$ and $q$ the continuously compounded risk-free and dividend yields, and $T$ the maturity in years. Under the risk-neutral measure $\mathbb Q$, let $X$ be a Lévy process with cumulant exponent $\kappa(u)$, defined by $\mathbb E^{\mathbb Q}[e^{uX_T}]=e^{T\kappa(u)}$ on its moment domain. Then

$$ S_T=F_{0,T}\exp\{X_T-T\kappa(1)\},\quad F_{0,T}=S_0 e^{(r-q)T}. $$

This correction ensures $\mathbb E^{\mathbb Q}[S_T]=F_{0,T}$ if the exponential moment exists. In the variance-gamma (VG) model, $X_T=\theta G_T+\sigma W_{G_T}$, where the independent gamma clock $G_T$ has shape $T/\nu$ and scale $\nu$. Its cumulant exponent is

$$ \kappa(u)=-\nu^{-1}\log(1-\theta\nu u-\tfrac12\sigma^2\nu u^2). $$

Its annual log-return variance is $v=\sigma^2+\theta^2\nu$. In a Merton jump-diffusion with Gaussian log jumps of mean $\mu_J$ and standard deviation $s_J$, intensity $\lambda$, and diffusion volatility $\sigma_M$, the same variance requires $\sigma_M^2=v-\lambda(\mu_J^2+s_J^2)\geq0$. The Gaussian benchmark uses volatility $\sqrt v$. Matching variance and forward does not match skewness, kurtosis or the option smile. Independent increments also constrain how cumulants scale with maturity.

## Experimental design

Use $S_0=100$, $r=2\%$, $q=1\%$, $T\in\{0.05,0.25,1,2\}$ years and forward log-moneyness $k=\log(K/F_{0,T})$ between $-0.30$ and $0.30$, where $K$ is strike. Start with $\theta=-0.12$, $\nu=0.2$, $\sigma=0.18$. Vary $\theta,\nu$ subject to a feasible variance match and an admissible exponential moment. Use conditional Gaussian mixture quadrature for VG and a Poisson mixture for Merton; check each with an independent characteristic-function or simulation reference. For simulation diagnostics start at 100,000 paths and seed 101401. Separate numerical error from changes in the risk-neutral law.



## Research tasks and required outputs

1. Derive cumulants, the martingale correction and the Gaussian limit as $\nu\to0$.
2. Implement the VG and Merton pricing integrals and independent reference methods. Report truncation, integration and sampling errors separately.
3. Verify put–call parity, monotonicity and convexity in strike and implied-volatility inversion. Flag quotes where inversion is ill-conditioned.
4. Construct smile and cumulant panels at matched forward and annual variance. Discuss how skewness and kurtosis relate to prices without assuming a universal ranking.
5. Compare convergence and computation time under alternative tail parameters and maturities. Document the domain of the pricing transform and retain failed or inadmissible cases.

Submit the smile panels, price/reference error tables, convergence and timing tables, and a parameter-domain diagnostic. The Merton comparison must include at least two maturities and three log-moneyness points. Report price errors in currency per share and implied-volatility errors in volatility points.

## Minimum viable thesis and acceptance criteria

VG, Gaussian and one finite-activity Merton benchmark with common forward and annual log-return variance at two maturities and at least three forward log-moneyness points; one independent pricing reference for each non-Gaussian model, martingale and put-call parity checks, and comparative smile and convergence analysis.

## Research plan and scope

| Weeks | Deliverable |
|:--|:--|
| 1–3 | Lévy exponents, moments and martingale correction |
| 4–6 | Pricing methods, independent references and limits |
| 7–9 | Matched-moment smile and cumulant experiments |
| 10–12 | Convergence, tail robustness and computation cost |
| 13–16 | Interpretation, reproducibility and thesis writing |

Prerequisites: stochastic processes, characteristic functions, option pricing and quadrature. Optional extension: NIG or CGMY, only after establishing moment admissibility. A synthetic exercise cannot establish market calibration quality or an unrestricted dynamic smile. Do not match a moment that does not exist. Before assignment, agree on the parameter domain and reference-method precision with the supervisor.

## Core reading

Madan, Carr and Chang (1998), *European Finance Review*, 2, 79–105. Variance gamma and option pricing.  
Cont and Tankov (2004), *Financial Modelling with Jump Processes*. Chapman & Hall/CRC. Lévy cumulants and pricing.  
Carr, Geman, Madan and Yor (2002), *Journal of Business*, 75, 305–332. Context for the empirical relevance of Lévy models.  
Use the original workspace reading guide for bibliographic details and source routes. Full-text review remains pending.
