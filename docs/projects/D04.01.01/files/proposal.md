---
title: The Economics of Discrete-Time Delta Hedging
---

**D04.01.01 · Derivatives · Synthetic data · Difficulty 1/3 · 16 weeks**

Current research proposal. Supervisor approval and applicable data clearance remain pending.

## Motivation

In the Black--Scholes economy, continuous trading eliminates replication risk. A trader who can rebalance only at discrete dates must instead bear the residual price risk accumulated between trades. More frequent trading reduces this exposure, but the trading volume needed to achieve a given precision can be substantial even when transaction costs are excluded. This project studies the economic magnitude and distribution of the residual risk, rather than simply reproducing the continuous-time formula.

## Research question

How rapidly does terminal replication error decline as delta rebalancing becomes more frequent, and which strikes, maturities and volatility states remain difficult to hedge?

## Model and intuition

Let $S_t$ denote a non-dividend-paying stock, $r$ the constant short rate and $\sigma$ annual volatility. Under the physical measure $\mathbb P$, $dS_t/S_t=\mu\,dt+\sigma\,dW_t^{\mathbb P}$. Under the pricing measure $\mathbb Q$, the drift is $r$. Write $C(t,S_t)$ for the Black--Scholes call price with fixed strike $K$ and maturity $T$. The stock holding is $\Delta_t=\partial C(t,S_t)/\partial S_t$. Let $B_j$ be the cash balance immediately after trading at date $t_j$.

$$B_0=C(0,S_0)-\Delta_0S_0,\qquad B_j=B_{j-1}e^{r(t_j-t_{j-1})}-(\Delta_j-\Delta_{j-1})S_{t_j}.$$

At maturity, liquidate the stock and pay the short call. The discounted seller's error is $E=e^{-rT}[B_{n-1}e^{r(T-t_{n-1})}+\Delta_{n-1}S_T-(S_T-K)^+]$. Positive $E$ is a gain; negative $E$ is a loss. The local error is approximately minus one half of gamma times the unexpected squared price increment. This approximation helps explain why high-gamma states are difficult to hedge.

## Experimental design

Set $S_0=100$, $r=2\%$, $\mu=6\%$ (and $\mu=r$ for robustness), $\sigma\in\{15\%,30\%\}$, $K\in\{90,100,110\}$ and $T\in\{0.25,1\}$ years. Simulate exact GBM on a 256-step grid and subsample the same paths at 4, 16, 64 and 256 hedge intervals. Use at least 20,000 paths per scenario and independent replication. The primary exercise is frictionless; report gross turnover without fees.

\newpage

## Applied research programme

1. **Validate the hedge ledger.** Derive the delta and cash-account updates; check a deterministic path by hand. Reconcile the discounted cash recursion and gains representation.
2. **Measure replication error.** Estimate mean, standard deviation, RMSE and tail quantiles at each frequency. Retain common paths across frequencies and report uncertainty from independent replications or paired resampling.
3. **Study convergence.** Plot RMSE against the number of intervals on log--log axes. Compare with the usual square-root-order benchmark under regularity; do not impose an exact finite-grid exponent.
4. **Explain heterogeneity.** Compare strikes, maturities, volatility and gamma. Terminal-moneyness classifications describe realized errors and must not be treated as information available to the trader.
5. **Quantify trading intensity.** Include opening, intermediate and terminal liquidation in turnover. Do not infer actual transaction costs from this frictionless design.

## Deliverables and acceptance

Provide a tested ledger, distribution and convergence figures, tail loss and turnover tables and a gamma-based interpretation. Express errors in currency per option and relative to spot; premium normalization is sensitive to small option values. Change drift and volatility and repeat with independent seeds. No empirical claim is required.

**Minimum viable thesis.** Exact GBM, verified self-financing hedge, four frequencies and three strikes, quantitative convergence and distribution analysis with Monte Carlo precision.

Optional extension: deliberately misspecify the pricing volatility while retaining the model-consistent frictionless experiment as the baseline. Frequency optimization with actual fees belongs to the separate project D04.03.01.

## Work plan and prerequisites

Weeks 1--3: replication and error expansion; 4--6: ledger; 7--9: simulations; 10--12: gamma and tail diagnostics; 13--16: robustness and writing. Prerequisites: stochastic calculus, Black--Scholes, simulation, Python arrays and basic inference.

## Core reading

Black and Scholes (1973), *Journal of Political Economy* 81, 637--654. Boyle and Emanuel (1980), *Journal of Financial Economics* 8, 259--282. Glasserman (2004), *Monte Carlo Methods in Financial Engineering*, Springer. Consult the original reading guide for the source metadata and reading sequence. No new full-text verification is claimed here.
