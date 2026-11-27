---
title: "Credit Default Swap Pricing and Recovery Risk"
subtitle: "Research proposal | D09.02.02"
---

**Derivatives · Credit risk and incomplete markets · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Recovery affects the premium for new protection and the value of an existing CDS. These sensitivities have different meanings depending on whether one holds the default model fixed or recalibrates it to the same observed quote. Keep contractual coupon and par coupon distinct throughout.

## Research question

How do changes in assumed recovery alter fair CDS spreads, mark-to-market and inferred default intensity, under an otherwise identical hazard model?

## Economic mechanism

From the protection buyer's perspective $V=(1-R)\mathcal L-c\mathcal A$, with $c$ the contractual annual premium.

## Research design

Use the prescribed quarterly synthetic CDS maturities, hazards, recoveries and off-market coupons. Compute fixed-hazard recovery sensitivity, then hold the reference spread fixed and recalibrate hazard. Compare the resulting mark-to-market under fixed contractual coupon.

Check zero par MTM, buyer/seller antisymmetry and alternate-recovery repricing. In the continuous-premium flat-hazard limit, $s=(1-R)\lambda$; quarterly accrual is evaluated using its own convention.

\newpage

## Required exhibits

Leg PV and repricing tests; recovery/hazard identification contours; MTM and DV01 tables; sensitivity plots.

## Minimum viable thesis

Constant intensity CDS with quarterly accrual, fair spread and inverse calibration; fixed-input versus recalibrated recovery sensitivity and one off-market MTM example.

## Scope and feasibility

A fair-spread identity is not an observed recovery estimate. Distinguish default probabilities under Q from physical probabilities. Account for accrual and cashflow timing; no double counting recovery. Distinct from D09.02.01, which centers on hazard-curve bootstrap.

**Prerequisites:** Fixed income, survival functions, numerical integration and Python.

**Optional extension:** Bootstrap hazard buckets and study recovery term structure or a simple dependent default/recovery state model.

## Milestones

W1-3: pricing and accrual; W4-6: implementation; W7-9: inversion; W10-12: sensitivities; W13-16: writing and reproducibility.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
