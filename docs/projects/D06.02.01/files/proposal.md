---
title: "The Early Exercise Premium of American Options"
subtitle: "Research proposal | D06.02.01"
---

**Derivatives · Numerical pricing and exotics · Level 1/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

An American exercise right depends on the opportunity cost of waiting, forgone dividends and future payoff uncertainty. The focus is economic comparative statics, not algorithm rankings. The project studies the value of exercise for calls and puts and the response of the boundary to carry.

## Research question

When is early exercise optimal and how much does the exercise right contribute to the value of American calls and puts?

## Economic mechanism

On the same lattice the exercise premium is $V^A-V^E\ge0$. Positive intrinsic value and a meaningful advantage over continuation identify an exercise region; zero-payoff ties do not.

## Research design

Use the prescribed CRR call/put grid across strikes, expiries, rates, dividends and volatility. Compare American and European prices on the same lattice and refine premium and exercise-boundary maps.

Use adjacent lattice refinements, verify q=0 with nonnegative r and the maturity limit. Report boundary resolution separately from price precision. Discrete dividends require different cashflow treatment.

\newpage

## Required exhibits

Premium heatmaps, exercise boundaries, carry sensitivity plots, convergence table and numerical premium decomposition.

## Minimum viable thesis

Validated tree, calls and puts, at least three carry scenarios, premium and boundary maps plus convergence. The focus is economic comparative statics rather than comparing solvers (D05.02.01).

## Scope and feasibility

Test no-dividend call equality, American>=European, intrinsic lower bound and maturity limit. Exercise boundary errors can be material even when prices converge. A discrete-dividend extension needs separate ex-date treatment. Do not equate the Q probability of exercise to a physical exercise frequency.

**Prerequisites:** Derivatives pricing, probability, Python arrays and basic numerical methods.

**Optional extension:** Compare continuous yield with known cash dividends using a suitably adjusted tree or finite differences.

## Milestones

W1-3: stopping theory and recursion; W4-6: European and American implementation; W7-9: comparative statics; W10-12: premium decomposition and convergence; W13-16: interpretation, code and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
