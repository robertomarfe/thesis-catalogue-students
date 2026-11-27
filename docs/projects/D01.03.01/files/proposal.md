---
title: "Jump Risk and the Pricing of Equity Options"
subtitle: "Research proposal | D01.03.01"
---

**Derivatives · Vanilla pricing and surfaces · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

A diffusion with rare jumps and a Gaussian diffusion can have equal instantaneous log-return variance but very different short-maturity tail probabilities. Holding total variance fixed isolates the price implications of discontinuity rather than simply increasing the overall level of risk. The project studies how intensity, jump asymmetry and jump dispersion reshape the risk-neutral smile.

## Research question

How do jump intensity, mean jump size and jump dispersion affect equity option prices and implied-volatility skew at a fixed total instantaneous log-return variance?

## Economic mechanism

For log jump $Y\sim N(m,s_J^2)$, intensity $\lambda$ and diffusion volatility $\sigma$, annual log variance is $\sigma^2+\lambda(m^2+s_J^2)$. Hold it fixed when varying the jump mechanism.

## Research design

Use a fixed annual log-return variance of 0.09, varying Poisson intensity, jump mean and dispersion, with nonnegative residual diffusion variance. Compare maturities from very short to two years and strike-to-forward ratios 0.7–1.3 using a compensated mixture and independent terminal simulation.

Build admissible variance-matched configurations before calculating prices. Hold forward fixed and compare several maturities; report ordinary and stock-weighted truncation diagnostics. Keep jump-size and intensity perturbations distinct.

\newpage

## Required exhibits

Price/IV curves by maturity; skew heatmap; matched-variance table; mixture truncation and MC diagnostic.

## Minimum viable thesis

Compensated mixture, independent MC, matched-variance BSM and three jump scenarios over three maturities, with error checks.

## Scope and feasibility

Use Q rather than historical jump estimates for pricing; matching log variance does not match higher moments or option prices. Check no-arbitrage bounds and negligible wing vega. Distinct from D01.01.02 (hedging misspecification).

**Prerequisites:** BSM, Poisson processes, numerical integration, Python.

**Optional extension:** Contrast Heston and jump-diffusion under matched ATM term structure; test identifiability on synthetic quotes.

## Milestones

W1-3: derive model; W4-6: implement mixture/MC; W7-9: implied vol and controls; W10-12: maturity and jump grid; W13-16: robustness and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
