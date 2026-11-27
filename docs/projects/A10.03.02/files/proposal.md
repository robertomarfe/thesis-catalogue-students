---
title: "Sparse Predictors and the Factor Zoo"
subtitle: "Research proposal | A10.03.02"
---

**Asset pricing · Predictability and machine learning · Level 3/3**

**Data:** Empirical design conditional on actual access and coverage. **Status:** current review draft; supervisor approval pending.

## Motivation

A large zoo of proposed factors creates a high-dimensional pricing problem. Sparse selection can reduce redundancy but may be unstable; the decisive distinction is performance on new dates for known assets versus new dates and different assets. Data rights and exact factor definitions are binding.

## Research question

Do sparse factor selections learned on one set of test assets and historical dates reduce pricing errors for different assets on future dates relative to FF3/FF5 and dense shrinkage?

## Economic mechanism

For centered factor vector $f-\mu_f$, the normalized linear kernel $m=1-b^\top(f-\mu_f)$ gives excess-payoff pricing moment $g(b)=E[r^e]-\operatorname{Cov}(r^e,f)b$ on the training sample.

## Research design

Use authorized pinned OSAP dictionary/returns, 30–60 metadata-selected signals and French industries plus size/BM. Fit on industries and past dates, tune on chronological industry blocks; evaluate same assets later and different assets later in 2016–2025. FF3/FF5 and ridge benchmarks.

Use one shared OSAP revision and distinct file hashes; freeze candidate selection and common SPD weight on training only. Check KKT, scale and unpenalized FF3. Compare same assets future and different assets future, fixed kernel, mean and scale, common metric. No post-selection p-values. Conditional access; no silent substitution.

\newpage

## Required exhibits

Factor selection path, held-out moment table, overlap/conditioning audit, selection stability and uncertainty.

## Minimum viable thesis

One pinned candidate panel, two held-out asset/date tests, FF3 and ridge comparison, training-only tuning.

## Scope and feasibility

Shared underlying stocks and correlated factors limit independent validation. No post-selection classical p-values; no claim of unique true factors. Pin OSAP release and exact definitions; equal weighting across assets as baseline.

**Prerequisites:** Linear algebra, regularization, SDF moments, Python.

**Optional extension:** Elastic net and grouped factors by documented economic families, with nested chronological validation.

## Milestones

W1-3: data and moments; W4-6: synthetic/benchmark; W7-9: nested fit; W10-12: held-out and stability; W13-16: writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
