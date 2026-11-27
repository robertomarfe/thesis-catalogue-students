---
title: "The Black-Scholes Model and the Economic Implications of Its Assumptions"
subtitle: "Research proposal | D01.01.01"
---

**Derivatives · Vanilla pricing and surfaces · Level 1/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

The Black–Scholes price is an equilibrium restriction in a frictionless diffusion economy, not a general description of the option market. Its Greeks quantify local exposures to model inputs; they need not predict the effect of a large change in those inputs. A second issue is whether two terminal distributions with the same forward and stock-price variance imply the same price. This project separates these two questions: comparative statics within the model and valuation across alternative terminal laws.

## Research question

How do volatility, interest rates, dividends and time to maturity change European option prices and Greeks? How large are the pricing differences when the lognormal assumption is relaxed while matching forward and terminal variance?

## Economic mechanism

With discount $D$, forward $F$ and strike $K$, the no-arbitrage call price is $C=D\mathbb E^{\mathbb Q}[(S_T-K)^+]$. The Black–Scholes model specifies a lognormal law; a mixture may satisfy the same forward and second moment without preserving this expectation.

## Research design

Use synthetic European options with spot 100, strikes from 70% to 130% of spot and four maturities from one month to two years. Vary volatility, rate, dividends and maturity independently. Compare a two-component terminal mixture to the Gaussian benchmark with common forward and arithmetic second moment.

Separate each input perturbation from a change in the terminal law. Hold other inputs fixed for Greeks; for the mixture preserve the forward and arithmetic second moment at every maturity. Report units and distinguish small perturbations from scenario repricing.

\newpage

## Required exhibits

Price and Greek maps, analytical-versus-numerical error table, sensitivity and mixture smile panels, documented Python functions and fixed parameter grid.

## Minimum viable thesis

BSM derivation and validated implementation, four input sensitivity experiments, one controlled non-lognormal comparison and an economic interpretation of the observed differences.

## Scope and feasibility

Use at least two maturities and volatility regimes; handle near-expiry limits separately rather than dividing by zero. Validate parity and bounds for both distributions. Do not infer a market pricing error, realistic probabilities or dynamic mixture hedge performance.

**Prerequisites:** Probability, basic stochastic calculus, derivatives pricing and Python NumPy/SciPy. No external quotes required.

**Optional extension:** Repeat the terminal experiment using a compensated jump-diffusion with an independent price reference; keep the main thesis distinct from empirical Heston calibration.

## Milestones

W1-3: derive pricing and sensitivities; W4-6: implement and test BSM; W7-9: run parameter grids; W10-12: build matched-moment mixture and diagnostics; W13-16: interpret and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
