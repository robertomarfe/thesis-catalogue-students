---
title: Counterparty Credit Risk and the Pricing of Uncollateralized Derivatives
---

**D09.04.01 · Derivatives · Synthetic data · Difficulty 2/3 · 16 weeks**

Current research proposal. Supervisor approval and applicable data clearance remain pending.

## Motivation

A forward contract can be fairly priced at inception yet expose its holder to a loss if the counterparty defaults before settlement. The potential loss depends on the future replacement value at the time of default, not on the contractual notional alone. A useful valuation adjustment therefore requires both a model of market risk and a model of default. This project quantifies their joint importance, and asks whether an independence approximation remains informative when default intensity responds to the underlying price.

## Research question

How do maturity, market volatility, hazard and recovery jointly shape unilateral CVA for an uncollateralized forward, and how sensitive is independence-based CVA to wrong-way risk?

## Model and economic intuition

Let $S_t$ be an equity price, $r$ the constant short rate, $q$ the dividend yield and $\sigma$ annual volatility. Under the pricing measure $\mathbb Q$, $dS_t/S_t=(r-q)dt+\sigma dW_t^{\mathbb Q}$. For a long forward with contractual delivery price $K$ and maturity $T$, the clean replacement value is

$$V_t=S_te^{-q(T-t)}-Ke^{-r(T-t)}.$$

With unilateral counterparty default time $\tau_d$, recovery fraction $R$ and clean closeout, the valuation adjustment is

$$\mathrm{CVA}=(1-R)\mathbb E^{\mathbb Q}[e^{-r\tau_d}V_{\tau_d}^+\mathbf 1_{\{\tau_d\le T\}}].$$

The credit-adjusted value is the clean value minus CVA. If default is independent with constant intensity $h$, the default density is $he^{-ht}$. The expected discounted positive exposure can be computed using a lognormal call-form expression. Dependence requires a joint model, not simply a change in hazard: comparisons should preserve the marginal survival curve if their purpose is to isolate dependence.

## Experimental design

Use synthetic forwards with $S_0=100$, $K=S_0e^{(r-q)T}$, $r=2\%$, $q=1\%$, $\sigma=15$--$40\%$, maturities 1, 3 and 5 years, $h=0.5$--$5\%$ and baseline $R=40\%$. Hold the contractual strike fixed when comparing risk perturbations at each maturity. No proprietary quotes are required.

\newpage

## Applied research programme

1. **Verify clean value and exposure.** Derive the discounted positive exposure and check against lognormal integration; test $h=0$, $R=1$, $\sigma=0$ and long/short sign conventions.
2. **Reconcile continuous and grid valuation.** Compare quadrature, exact GBM paths and independently drawn exponential default times. Separate grid bias from sampling uncertainty.
3. **Map credit and market risks.** Report CVA per unit notional across maturity, volatility, hazard and recovery. Contrast fixed-hazard and fixed-credit-spread scenarios without treating recovery and spread as independently identified.
4. **Isolate wrong-way risk.** At one maturity use an adapted Cox intensity depending on the preceding log price; calibrate its deterministic baseline on separate paths to match survival at all grid nodes. Compare signed dependence with fixed-baseline cases and independence; report both marginal default probability and CVA. Refine the grid and verify with independently sampled default clocks.
5. **Interpret the limits.** A risk-neutral hazard is not a physical forecast. Clean closeout, deterministic rates and no own default, collateral, funding or netting are deliberate restrictions.

## Deliverables and acceptance

Submit exposure curves, CVA/notional heatmaps, benchmark and sensitivity tables, and survival-curve and simulation-uncertainty diagnostics. Document seeds and calibration/evaluation separation. Keep dependence as a bounded robustness exercise; the distinct D09.04.02 project makes the dependence mechanism the central question.

**Minimum viable thesis.** One equity forward, independent default, analytic exposure and independent Monte Carlo check, four hazard/volatility scenarios; at one maturity, compare independent and two signed adapted Cox-intensity cases after matching the marginal survival curve on a common grid. Report default probabilities, CVA, simulation and time-grid uncertainty and the separate fixed-baseline comparison.

Optional extension: portfolio netting or collateral thresholds under matched exposure and closeout conventions.

## Work plan and prerequisites

Weeks 1--3: pricing and closeout; 4--6: exposure and MC; 7--9: CVA validation; 10--12: sensitivity and dependence; 13--16: robustness and writing. Prerequisites: Black--Scholes, credit intensity, numerical integration and Python.

## Core reading

Brigo, Morini and Pallavicini (2013), *Counterparty Credit Risk, Collateral and Funding*, Wiley; Gregory (2020), *The xVA Challenge*, 4th ed., Wiley; Duffie and Singleton (2003), *Credit Risk*, Princeton University Press. See the inherited reading guide. No new full-text verification is claimed.
