---
title: Black-Litterman Portfolio Choice under Uncertain Expected Returns
---

**A08.02.01 / Asset pricing / Empirical / Difficulty 2/3 / 16 weeks / Data gate: pending**

Current research proposal. Not approved for assignment.

## Motivation

Portfolio choice based on estimated expected returns is vulnerable to sampling error. Black-Litterman uses a reference portfolio and noisy relative-return views to regularize estimates of the mean. Its economic value depends on whether those views improve held-out allocation decisions after constraints and costs. The project distinguishes a genuine sensitivity to prior uncertainty from a parameter that cancels by construction.

## Research question

How do prior strength and uncertainty in relative-return views affect Black-Litterman posterior allocations and their held-out economic performance?

## Model and economic intuition

Let $\Sigma$ be the monthly return covariance, $w_0$ a reference portfolio and $\pi=\delta\Sigma w_0$ a prior mean. Assume $\mu\sim N(\pi,\tau\Sigma)$ and noisy views $Q=P\mu+\epsilon$, $\epsilon\sim N(0,\Omega)$. The posterior mean is

$$\mu_{BL}=\pi+\tau\Sigma P^\top(P\tau\Sigma P^\top+\Omega)^{-1}(Q-P\pi).$$

Keep the return covariance fixed when comparing mean updates. If $\Omega=c\tau\operatorname{diag}(P\Sigma P^\top)$, the factor $\tau$ cancels from the posterior mean. An anchored $\Omega$ permits a distinct sensitivity to prior uncertainty.

## Data and research design

Use monthly value-weighted ten-industry French total returns and FF3 risk-free returns, 1970--2025 subject to valid common coverage. Use trailing 120-month excess-return means/covariances, identical shrinkage across methods, equal-weight reference and delta=3. Predeclare relative views using lagged sample means; verify portfolio labels. Freeze the evaluation design before 2005--2025 held-out evaluation. No data or empirical results are provided.

\newpage

## Applied research programme

1. Derive the Gaussian posterior and check zero-innovation and weak-view limits.
2. At one prespecified origin compare confidence settings 0.1, 1, 10 and the anchored versus proportional Omega experiment.
3. Compute long-only fully invested rolling allocations with common covariance and risk aversion; compare equal-weight, prior-only and sample-mean benchmarks.
4. Compute drift-adjusted turnover and 10/25 bp trading cost sensitivity; report Sharpe, certainty equivalent, concentration and performance.
5. Use paired date-block uncertainty and prespecified alternative view definitions. No test-sample tuning.

## Deliverables and acceptance

Posterior diagnostic and sensitivity curves; rolling weight and performance tables; cost-adjusted results, turnover, concentration and reproducible code. Reference weights are stylized, not observed market-equilibrium weights.

**Minimum viable thesis.** Validated posterior, one relative-view pair, at least three confidence settings and long-only rolling comparison with prior/equal/sample-mean benchmarks; show tau invariance under proportional Omega and a separate prior-strength sensitivity at one prespecified origin with Omega anchored at a fixed tau reference. Keep the return covariance and risk aversion fixed in mean comparisons.

## Work plan

Weeks 1--3: theory and source review; 4--6: data or numerical setup; 7--10: core implementation; 11--13: robustness; 14--16: writing and replication. Preserve the more detailed canonical milestones.

## Core reading

Black and Litterman (1992); He and Litterman (1999); DeMiguel, Garlappi and Uppal (2009). Consult inherited reading guide and verify source metadata before final citation.
