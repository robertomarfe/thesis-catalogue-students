---
title: "Focused methods — Value and Momentum Everywhere: Common Risk or Diversification?"
subtitle: "A09.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Comparable factor sleeves
Keep value and momentum payoffs in documented units and currency. Equity regions alone are not three asset classes. Do not include a provider aggregate alongside its constituents. If $f_t$ contains $N$ sleeves, fit training means $\bar f$, positive standard deviations $s_i$ and the correlation matrix of $z_t=(f_t-\bar f)/s$. Estimate PCA eigenvectors on training only; project held-out rows with those same means, scales and loadings. Report explained variation in training and reconstruction error in test, not a new fit on test.

## Diversification and scaling
For predetermined weights $w_t$, a composite payoff is $w_t^\top f_{t+1}$. A fixed-weight benchmark distinguishes diversification from dynamic risk scaling. If weights depend on past volatility, document gross notional, volatility floors and funding assumptions. Compare portfolios on identical observations; block-resample paired payoff and covariance statistics. Published factors may already target risk, and historical data do not reveal tradable positions or transaction costs. The original workbook must not be silently replaced with an updated vintage.

## Research checks

Inspect workbook tabs and exact periods; preserve common dates and no imputation. Fit all scales/loadings on training. Report sleeves, overlap, risk normalization and holdout uncertainty.
