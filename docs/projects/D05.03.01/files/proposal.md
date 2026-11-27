---
title: "Fourier-Based Option Pricing: Accuracy and Computational Efficiency"
subtitle: "Research proposal | D05.03.01"
---

**Derivatives · Numerical pricing and exotics · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Transform methods are useful when the terminal law has a characteristic function but no simple option formula. A large batch of strikes may justify FFT setup, while a few queries may favor quadrature. The thesis compares speed at controlled pricing error, not merely the elapsed time of two implementations.

## Research question

At a specified error tolerance, when is FFT inversion more efficient than direct quadrature for European option pricing?

## Economic mechanism

With $x=\log S_T$, $k=\log K$ and $\phi(u)=\mathbb E^{\mathbb Q}e^{iux}$, damped inversion requires a finite moment of order $\alpha+1$. FFT grids obey $\Delta u\Delta k=2\pi/N$.

## Research design

Use Black–Scholes and Heston at three maturities, with 1/25/201 strike queries including off-grid strikes. Compare adaptive quadrature and FFT at matched tolerance; cross-check a Heston reference independently.

Separate characteristic-function, cutoff, aliasing and interpolation error. Freeze tolerance and hardware protocol. Use absolute currency errors near zero; calibration is outside scope.

\newpage

## Required exhibits

Convergence plots, error/time Pareto frontiers, parameter grid and failure table, reproducible timing script.

## Minimum viable thesis

BSM exact validation, one Heston reference, FFT and direct quadrature comparisons across strike counts at matched tolerance. Distinct from D05.01 and D05.02 numerical methods.

## Scope and feasibility

Do not compare a coarse FFT with a high-accuracy reference without reporting tolerance. Reference inversion may share characteristic-function error; use independent limiting cases. Price error primary; relative errors near zero and IV error secondary. Keep model calibration out of scope.

**Prerequisites:** Complex numbers, Fourier transforms, stochastic volatility, numerical analysis.

**Optional extension:** Add COS method and compare tail truncation or characteristic functions of jump models.

## Milestones

W1-3: derive inversion; W4-6: implement and validate CF; W7-9: FFT and quadrature grids; W10-12: stress and timing; W13-16: document.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
