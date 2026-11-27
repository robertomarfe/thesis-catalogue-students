---
title: "Focused methods — Dynamic versus Static Stock-Bond Asset Allocation"
subtitle: "A08.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For continuous zero yield $y_t(n)$, $P_t(n)=e^{-ny_t(n)}$; monthly gross return is $P_{t+1}(n-1/12)/P_t(n)$.

Use exact aging and consistent interpolation; synthetic zeros are not a traded fund. Fit covariance on past returns only; freeze EWMA half-life in validation. Compare rebalanced 60/40, expanding and dynamic GMV on identical dates. Baseline half-L1 turnover equals full-L1 turnover with half the rate. Document revised yield vintage, cost and funding conventions.

## Research checks

Hand-check P_(t+1)(5-1/12)/P_t(5) and common monthly market total return. Verify EWMA versus direct weighted covariance, lag estimates and training-only tuning. Compare same capital/constraints/costs and out-of-sample periods, net performance with paired block inference.
