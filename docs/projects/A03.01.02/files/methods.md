---
title: "Focused methods — The Risk-Free Rate Puzzle under Time-Additive Utility"
subtitle: "A03.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

If $g_{t+1}=\mu+\phi(g_t-\mu)+\sigma\epsilon_{t+1}$ is conditionally Gaussian, then $\log R_{f,t}=-\log\beta+\gamma E_t[g_{t+1}]-\gamma^2\sigma^2/2$.

For $|\phi|<1$, the stationary standard deviation of the annualized quarterly log safe rate is $4\gamma|\phi|\sigma/\sqrt{1-\phi^2}$. The precautionary term lowers the mean log safe rate. In the iid limit the model conditional rate is constant; realized real nominal bills can nevertheless fluctuate with inflation. Solve beta from the mean rate, retaining inadmissible values; do not treat ex post quarterly bills as a real zero yield. Refit the conditional growth model in joint calendar-aware blocks.

## Research checks

Provide calendar-aware pair counts and separate fitted conditional rate mean/SD from ex-post real bill mean/SD; test the Gaussian formula by quadrature. Derive beta frontier, retain beta outside (0,1) as inadmissible, and include uncertainty in AR persistence and conditional variance; a rate-volatility mismatch need not imply rejection solely of gamma.
