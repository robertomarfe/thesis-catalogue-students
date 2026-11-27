---
title: "Focused methods — Quasi-Monte Carlo Methods for Path-Dependent Options"
subtitle: "D05.01.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Integration and coordinate ordering
At fixing dates $t_j$, exact GBM is $S_{t_j}=S_0\exp[(r-q-\sigma^2/2)t_j+\sigma W_{t_j}]$. The arithmetic call price is $e^{-rT}\mathbb E^{\mathbb Q}[(m^{-1}\sum_j S_{t_j}-K)^+]$. Independent normals generate chronological increments or conditional bridge points after sampling $W_T$. Either construction must reproduce $\operatorname{Cov}(W_{t_i},W_{t_j})=\min(t_i,t_j)$. Bridge ordering changes effective dimension, not the contract.

## Replication and uncertainty
Transform scrambled Sobol points through the inverse normal cdf, documenting endpoint handling. Each independent scramble yields a price estimate; use between-scramble dispersion rather than IID formulas for points. A geometric average has a lognormal law, whereas a separately controlled arithmetic reference is numerical. Distinguish single-replicate RMSE from the SE of an average of replicates. Compare identical path counts, include construction cost and bound memory by batching without changing the point set.

## Research checks

Check Gaussian covariance before pricing. If reference uncertainty prevents ranking, increase the reference budget or label the result unresolved. The exercise measures integration error, not continuous-monitoring discretization.
