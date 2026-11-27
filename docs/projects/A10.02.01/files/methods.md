---
title: "Focused methods — Tree-Based Models for Stock Market Return Predictability"
subtitle: "A10.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

A regression tree partitions feature space into leaves $A_j$ and predicts $f(x)=\sum_j c_j\mathbf1\{x\in A_j\}$. A shallow ensemble averages or sequentially combines trees with fixed complexity constraints. Compare the final prediction loss with an expanding mean and ridge. Hyperparameters such as maximum depth and minimum leaf size are selected solely within time-ordered inner folds; test loss is not a tuning objective.

## Identification and implementation

The forest and boosting menus differ in regularization. Retain depth 1–3, leaf 24/48, 200 forest trees, boosting rates .03/.1 and 50/100 iterations as the original grid. Compare gains against ridge rather than against a weak linear baseline alone. Report unsuccessful fits and validation-only importance.

## Research checks

No random cross-validation; identical dates/features and mature label rules; perturb future inputs and labels; verify depth/minimum leaf constraints; record seeds and failed fits, not only successful winners.
