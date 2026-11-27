---
title: "Least-Squares Monte Carlo for Bermudan Options"
subtitle: "Research proposal | D06.02.02"
---

**Derivatives · Numerical pricing and exotics · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Least-squares Monte Carlo learns a stopping policy by approximating conditional continuation. Regression fit need not predict policy quality: exercise is a nonlinear decision, and evaluating on training paths invites selection bias. The project evaluates frozen policies independently.

## Research question

How do regression basis, training size and exercise frequency affect the value and quality of a least-squares Monte Carlo stopping policy?

## Economic mechanism

At exercise date $t_j$ compare $g(S_j)$ with an estimate $\widehat c_j(S_j)$ of conditional discounted continuation. The expected value of an admissible frozen policy is at most the optimum, not necessarily its finite-sample estimate.

## Research design

Use the original Bermudan put exercise grid, basis choices and training sizes. Train, select on validation paths and freeze before independent evaluation. Align a refined tree reference with the exact exercise dates.

Do not use realized future cashflows in test decisions. Compare three basis settings and three training sizes after one validated case. Distinguish regression conditioning from stopping-policy performance.

\newpage

## Required exhibits

Tree convergence, price and policy gap table, independent evaluation intervals, exercise-boundary figures, regression conditioning and computation time.

## Minimum viable thesis

One-dimensional Bermudan put, three basis settings, three training sizes, independent test paths, tree reference and uncertainty. Distinct from early-exercise economics (D06.02.01).

## Scope and feasibility

A better in-sample fit need not improve stopping policy. Use only information at exercise time, no future cash-flow leakage in evaluation; ensure correct discount times and distinguish policy gap from reference/MC noise. No exact optimality claim for LSM.

**Prerequisites:** Conditional expectation, Monte Carlo, least squares and Python.

**Optional extension:** Bermudan max/average option on two correlated assets; compare with a dual upper bound only after validating the martingale construction.

## Milestones

W1-3: stopping and tree; W4-6: implement LSM; W7-9: policy validation and independent value; W10-12: basis, sample and exercise sensitivity; W13-16: code and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
