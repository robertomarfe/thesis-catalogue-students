---
title: "Focused methods — Fourier-Based Option Pricing: Accuracy and Computational Efficiency"
subtitle: "D05.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Damped inversion
Define $C(k)=e^{-rT}\mathbb E^{\mathbb Q}[(S_T-e^k)^+]$. For positive damping $\alpha$ with finite $\mathbb E S_T^{\alpha+1}$, its damped transform is
$$\Psi(u)=\frac{e^{-rT}\phi(u-i(\alpha+1))}{\alpha^2+\alpha-u^2+i(2\alpha+1)u}.$$
Recover $C(k)=e^{-\alpha k}\pi^{-1}\int_0^\infty\Re[e^{-iuk}\Psi(u)]du$. The FFT evaluates a uniform log-strike family using phases and quadrature weights; document frequency spacing, log-strike origin, damping and interpolation. Use a consistent complex branch and admissible moment domain for Heston.

## Matched accuracy
Vary cutoff and spacing, and evaluate both methods at identical requested strikes. An alternative inversion using the same characteristic function only isolates inversion error. Cross-check against BSM and an independent Heston reference. Include setup and interpolation in runtime; preserve failed tolerance matches.

## Research checks

Separate characteristic-function, cutoff, aliasing and interpolation error. Freeze tolerance and hardware protocol. Use absolute currency errors near zero; calibration is outside scope.
