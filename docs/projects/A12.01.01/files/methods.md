---
title: "Focused methods — Liquidity-Related Anomalies and Factor Pricing"
subtitle: "A12.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For a zero-investment spread, $r_{i,t}=a_i+b_i^\top f_t+c_i z_{t-1}+d_i^\top f_t z_{t-1}+e_{i,t}$.

Conditional alpha is $a_i+c_i z$ and beta $b_i+d_i z$. Do not subtract RF again. Illiquidity, bid-ask and liquidity beta are distinct signals. Pin three named series and direction in a matching dictionary; FF3/5 SMB definitions differ. Use release-aware NFCI, same monthly rows, joint blocks and multiplicity sensitivity.

## Research checks

Pin same OSAP dictionary and return revision, exactly three named signals and direction; match factors/RF conventions and release-aware NFCI. Fit unconditional and interaction models on same dates; conditional alpha=a+c*z, conditional beta=b+d*z. Joint blocks and multiple-comparison sensitivity; defer if no authorized bytes.
