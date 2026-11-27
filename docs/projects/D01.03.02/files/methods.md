---
title: "Focused methods — Stochastic Volatility versus Jump Risk: Explaining the Implied Volatility Skew"
subtitle: "D01.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Competing risk-neutral mechanisms
In Heston, $dv=\kappa(\theta-v)dt+\xi\sqrt v\,dW^v$ and $dS/S=(r-q)dt+\sqrt v\,dW^S$, with correlation $\rho$. Merton instead adds Poisson log jumps $Y\sim N(m,s_J^2)$ with intensity $\lambda$ and compensator $\lambda(\mathbb E[e^Y]-1)$ in the stock drift. The first model gives continuous prices and a variance state; the second has discontinuities even with constant diffusion variance. Use an independent characteristic-function inversion and conditional Poisson-mixture reference respectively. In both cases $\mathbb E^Q[S_T]=F$.

## Discriminating tests
Let $i$ index option contracts with the same forward conventions. Define a common calibration loss $\sum_{i\in\mathcal T}[(C_i(\vartheta)-C_i^{obs})/s_i]^2$, with $s_i$ predeclared vega or noise scales bounded away from zero. Match approximate ATM variance term structures on training contracts and assess the remaining shape. Freeze training maturities and alternating strikes before fitting either model. Compare out-of-sample short wings and long-maturity shape on the same contracts; summarize uncertainty across noise draws and multistart dispersion. Neither model nests the other in general. An indistinguishable result is informative: it limits what the selected vanilla quotes identify.

## Research checks

Generate a separate Heston and Merton truth panel. Use the same objective, bounds policy, numerical precision and untouched test grid across fitted models; report model-dependent failures and do not select short maturities after inspecting errors.
