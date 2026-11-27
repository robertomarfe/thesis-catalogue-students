---
title: "Focused methods — Covariance Shrinkage and Portfolio Performance"
subtitle: "A08.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For sample covariance $S$, shrink toward scaled identity: $\widehat\Sigma=(1-a)S+a\operatorname{tr}(S)I/N$.

Unconstrained GMV weights are proportional to $\Sigma^{-1}\mathbf1$; long-only requires constrained optimization. Positive uniform rescaling leaves weights invariant, not predicted variance. Document Ledoit-Wolf intensity and ML denominator versus sample ddof=1. Compare spectra, conditioning, risk and concentration. Record singular windows, not silent replacements. Use paired dates and drift-corrected costs.

## Research checks

Document shrinkage target, intensity and denominator; compare eigenvalues, condition numbers, KKT, weights and predicted risk on common origins. Same costs and drift, equal weight and sample GMV; report singular windows and predefined fallback, compare paired net OOS variance/turnover and block intervals.
