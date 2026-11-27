---
title: "Focused methods — Time-Series Momentum across Asset Classes"
subtitle: "A09.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Portfolio of published trend payoffs
Time-series momentum takes a direction based on an instrument's own past trend, unlike cross-sectional ranking across securities. Here the inputs are published asset-class strategy payoffs rather than raw futures trades. Keep four distinct sleeves and document the provider's existing risk normalization. Use a reported aggregate only as a separate benchmark. For a trailing allocation, estimate volatilities using data through month $t$, normalize weights under a fixed gross exposure convention, and multiply by realized sleeve payoffs in $t+1$.

## Stress and holdout
Estimate the market-tail threshold using training data only; conditioning on realized market returns in test is descriptive. Keep 2008 and 2020 event windows separate from the predeclared stress test. Report common dates, regime counts, risk and return, portfolio covariance and paired block uncertainty. A published excess strategy payoff is not a funded wealth return unless a capital and risk-free convention is added. Inverse-volatility weighting changes risk contributions and can change leverage: report both, not simply the Sharpe ratio.

## Research checks

Verify four sleeves, monthly units, risk scaling and market benchmark. Use only trailing data in weights and training thresholds, with fixed holdout. No independent futures-position replication claim.
