---
title: "Focused methods — The COS Method for Pricing Options with Non-Gaussian Returns"
subtitle: "D05.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Expansion and payoff coefficients
Write $\phi_X(u)=\mathbb E^{\mathbb Q}e^{iuX}$ and $u_j=j\pi/(b-a)$. Truncating the density on $[a,b]$ gives
$$V\approx e^{-rT}\sum_{j=0}^{N-1}{}'\Re[\phi_X(u_j)e^{-iu_ja}]G_j,$$
where $G_j=2(b-a)^{-1}\int_a^b g(x)\cos(u_j(x-a))dx$ and the prime halves the zero term. For a put $g(x)=K(1-e^x)^+$; derive the elementary integrals over the overlap with $x<0$. Obtain calls by parity and examine cancellation in deep OTM cases. If the characteristic function is for log forward return, shift to log strike exactly once.

## Width versus resolution
Cumulants motivate truncation intervals but do not guarantee error bounds. Vary width separately from $N$ against independent BSM and converged Poisson-mixture prices. Retain negative computed prices in the diagnostics. Include coefficient setup in fair timing.

## Research checks

Inspect short maturity, rare jumps and deep strikes before asserting convergence. A wider interval may require more terms; do not claim universal exponential convergence.
