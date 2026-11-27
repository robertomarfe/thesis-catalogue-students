---
title: "Focused methods — Long-Horizon Stock Return Predictability and Statistical Inference"
subtitle: "A02.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For a prespecified return convention define $y_{t,h}=\sum_{j=1}^{h}r^e_{t+j}$ and $y_{t,h}=a_h+b_h x_t+u_{t,h}$, for $h\in\{1,3,12\}$. Use additive log excess returns throughout the baseline; an alternative compounded gross-return convention must be consistent in data and simulation. Under the null, simulate $x_{t+1}=a+\rho x_t+v_{t+1}$ and $r^e_{t+1}=\mu+e_{t+1}$ with correlated innovations. With $\widehat t_h$ computed by the same estimator on each path, the joint statistic is $M=\max_h|\widehat t_h|$. Compare the observed statistic with the simulated joint distribution; marginal critical values do not control joint size. HAC covariance depends on the declared kernel and bandwidth, not merely on the number of overlapping months.

## Identification and implementation

Under iid one-month innovations with variance $\sigma^2$, $\operatorname{Cov}(y_{t,h},y_{t+k,h})=(h-k)\sigma^2$ for $0\le k<h$ under the constant-mean null. The slope score also depends on the persistent predictor. Use HAC with bandwidth at least $h-1$ as a starting point, not a finite-sample guarantee. Report $b_h/h$, Monte Carlo uncertainty and prespecified nonoverlap phases.

## Research checks

Check that h=1 target uses only t+1; h=12 uses exactly 12 consecutive months; incomplete paths are excluded. Compare simple and HAC inference on a toy sequence. Verify joint critical value is based on max absolute t from the same path, not independent marginal draws. Preserve negative and insignificant results.
