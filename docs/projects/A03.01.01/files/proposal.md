---
title: "The Equity Premium Puzzle: Theory and Quantitative Evidence"
subtitle: "Research proposal | A03.01.01"
---

**Asset pricing · Consumption-based asset pricing and equity term structures · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

The equity premium and the low safe rate impose different restrictions on the same marginal utility process. A joint exercise is more informative than choosing a risk aversion coefficient that matches only one return.

## Research question

Can a CRRA stochastic discount factor with plausible risk aversion and discounting simultaneously explain the US market excess return and the average risk-free rate? How sensitive is the answer to consumption measurement and time aggregation?

## Economic mechanism

With gross consumption growth $G_{t+1}$, power utility implies $m_{t+1}=\beta G_{t+1}^{-\gamma}$ and $E[m R_i]=1$.

## Research design

Quarterly FRED consumption and PCE inflation plus French monthly market/bill; joint Euler grid and bill-implied beta frontier on complete common quarters.

On a common quarterly calendar report both Euler residuals and beta pricing the bill, then the market residual and covariance identity; resample contiguous joint date blocks. Check compounded nominal gross legs divided by the same inflation ratio and compare beta annualized by beta_q**4. Distinguish arithmetic premium from compound annual growth. Report parameter grid including infeasible beta.

\newpage

## Required exhibits

Moment and covariance table; beta/gamma heatmap of Euler residuals; implied safe-rate and premium plots with empirical comparison; bootstrap intervals; explicit table of real bill proxy caveats. Explain the extent of joint fit, not just the gamma matching one target.

## Minimum viable thesis

Correct SDF and Euler derivation, publicly sourced consumption/market data, grid-based joint moment exercise, risk-free proxy distinction and uncertainty. The puzzle is assessed even if a chosen sample weakens it.

## Scope and feasibility

Distinguish quarterly from annual beta and units. Check sensitivity to 2020 and long sample choices with prespecified alternatives; use revised data for unconditional analysis and note measurement error. If real bill Euler condition fails, do not infer exact real risk-free-rate error without modeling inflation. Avoid treating estimated high gamma as a structural identification result.

**Prerequisites:** Expected utility, stochastic discount factors, covariance/lognormal algebra, empirical return construction, Python. No structural estimation package required.

**Optional extension:** Introduce a simple habit or Epstein-Zin illustration after core CRRA diagnostics; compare mechanisms analytically before attempting a high-dimensional calibration.

## Milestones

W1-3: derive Euler/lognormal restrictions; W4-6: align consumption, inflation and returns; W7-10: compute residuals and parameter grids; W11-13: bootstrap and measurement sensitivities; W14-16: write and validate.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
