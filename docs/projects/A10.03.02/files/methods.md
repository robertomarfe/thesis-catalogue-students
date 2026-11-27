---
title: "Focused methods — Sparse Predictors and the Factor Zoo"
subtitle: "A10.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For centered factor vector $f-\mu_f$, the normalized linear kernel $m=1-b^\top(f-\mu_f)$ gives excess-payoff pricing moment $g(b)=E[r^e]-\operatorname{Cov}(r^e,f)b$ on the training sample.

## Identification and implementation

Let $B$ be the training covariance matrix with factors standardized using training scale. Minimize $\frac12 g(b)^\top Wg(b)+\alpha\sum_{j\in\mathcal P}|b_j|$ with a common SPD training weight $W$ and unpenalized FF3 terms. For active penalized coefficients, $B_j^\top Wg=\alpha\operatorname{sign}(b_j)$; inactive terms satisfy absolute score at most $\alpha$; core scores vanish. On held-out data compute $E_{test}[m r^e]$ with frozen training centering, not a re-centered test covariance. The kernel is not guaranteed positive or gross-payoff normalized.

## Research checks

Use one shared OSAP revision and distinct file hashes; freeze candidate selection and common SPD weight on training only. Check KKT, scale and unpenalized FF3. Compare same assets future and different assets future, fixed kernel, mean and scale, common metric. No post-selection p-values. Conditional access; no silent substitution.
