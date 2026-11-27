---
title: "Focused methods — Mean-Variance Optimization and the Cost of Estimation Error"
subtitle: "A08.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

Maximize $U(w)=w^\top\mu-\gamma w^\top\Sigma w/2$ on the long-only simplex using monthly excess means and covariance.

True-moment oracle regret $U(w^*)-U(\widehat w)\geq0$ is distinct from realized sample CE. Cross true and estimated means and covariance on paired draws. Calculate wealth from total returns, Sharpe from excess returns; charge trading costs against drifted weights. Normal simple-return draws can imply nonpositive wealth; freeze admission policy and report failures.

## Research checks

Run paired known-moment cells: true/estimated mean crossed with true/estimated covariance, same random draws and out-of-sample returns, verify oracle objective and feasibility. For actual data record long-only weights, exact OOS dates, drifted trades, net wealth and CE units; date blocks and estimation uncertainty; report failed cells.
