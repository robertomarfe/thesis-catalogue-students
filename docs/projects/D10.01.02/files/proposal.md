---
title: Commodity Forward Curves and Convenience Yield
---

**D10.01.02 · Derivatives · Synthetic data · Difficulty 3/3 · 16 weeks**

Current research proposal. Supervisor approval and applicable data clearance remain pending.

## Motivation

Physical inventory may provide benefits beyond its resale value: it facilitates production, helps satisfy unexpected demand and reduces the risk of stockouts. A constant cost-of-carry model captures only a restricted relation between spot and forward prices. A stochastic net convenience yield permits the forward curve's slope and sensitivity to shocks to vary over time. The project studies how this additional state changes curve shape and the distribution of curve risk, rather than attempting to infer convenience yields from spot prices alone.

## Research question

How do current net convenience yield, its persistence and its correlation with spot shocks affect the shape and risk of commodity forward curves?

## Model and economic intuition

Let $S_t$ be the spot price, $r$ a constant short rate and $\delta_t$ net convenience yield (inventory benefit less storage cost). Under the pricing measure $\mathbb Q$,

$$d\log S_t=(r-\delta_t-\tfrac12\sigma_S^2)dt+\sigma_SdW_t^S,$$
$$d\delta_t=\kappa(a-\delta_t)dt+\sigma_\delta dW_t^\delta,$$

where $d\langle W^S,W^\delta\rangle_t=\rho\,dt$. For delivery at $T$, $F_{t,T}=\mathbb E_t^{\mathbb Q}[S_T]$ because rates are deterministic. Writing $u=T-t$ and $B(u)=(1-e^{-\kappa u})/\kappa$, the conditional integrated yield has mean $au+(\delta_t-a)B(u)$. Joint Gaussianity gives a closed-form forward price after accounting for the variance of the log-price innovation.

The elasticity of the forward with respect to spot is one, while its log sensitivity to current net convenience yield is $-B(u)$. A larger $\kappa$ attenuates the impact of a given yield shock on longer contracts. Correlation and yield volatility also affect the conditional mean through the lognormal correction.

## Experimental design

Use $S_0=80$, $r=3\%$, $a=4\%$, $\delta_0\in\{-5\%,4\%,15\%\}$, $\kappa\in\{0.5,2\}$, $\sigma_S=30\%$, $\sigma_\delta=10\%$ and $\rho\in\{-0.5,0,0.5\}$. Use deliveries at 1, 3, 6, 12, 24 and 60 months. No futures panel is required for the core synthetic exercise.

\newpage

## Applied research programme

1. **Derive and verify.** Derive the integrated Ornstein--Uhlenbeck representation, its covariance with spot shocks and the conditional lognormal mean. Test the constant net-carry limit.
2. **Validate prices.** Compare analytic forwards with independently simulated Gaussian innovations or fine-grid paths with convergence; use 50,000 paths and report confidence intervals for each maturity.
3. **Explain curve shape.** Plot all three current-yield regimes and the two persistence values. Distinguish contango and backwardation locally and over the chosen delivery range; curves need not be globally monotone.
4. **Quantify curve risk.** Compare analytical sensitivities to one-standard-deviation spot and convenience-yield shocks. Derive and validate the covariance of changes across maturities. Keep the instantaneous, fixed-delivery covariance distinct from finite-horizon rolled-contract returns.
5. **Evaluate the benchmark.** Match a constant-carry model at the same spot and short forward, and assess discrepancies farther along the curve. Vary the shock correlation while keeping the remaining parameters fixed.

## Deliverables and acceptance

Provide curve families, sensitivity term structures, a covariance heatmap, an analytic/MC reconciliation and an economic interpretation. Report rate inputs in annual decimals, prices in currency per commodity unit and delivery times in years. Negative net yields are permitted; the model still implies positive prices. Do not interpret risk-neutral parameters as physical expected returns.

**Minimum viable thesis.** Derivation, analytic implementation, MC check, at least three convenience-yield states, two persistence values and constant-carry benchmark.

Optional extension: estimate a two-factor model only if an authorized contract-level futures panel becomes available. EIA spot prices can contextualize levels but cannot validate the curve. Delivery constraints, negative-price episodes and seasonality are beyond the baseline.

## Work plan and prerequisites

Weeks 1--3: theory and derivations; 4--6: analytic curves and simulator; 7--9: sensitivities; 10--12: numerical checks and covariance; 13--16: interpretation and writing. Prerequisites: stochastic calculus, Gaussian processes, derivatives and Python.

## Core reading

Schwartz (1997), *Journal of Finance* 52, 923--973; Gibson and Schwartz (1990), *Journal of Finance* 45, 959--976; Geman (2005), *Commodities and Commodity Derivatives*, Wiley. Consult the inherited reading guide for full metadata. No new full-text verification is claimed.
