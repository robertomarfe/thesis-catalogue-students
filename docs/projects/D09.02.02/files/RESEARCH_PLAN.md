# Research plan | D09.02.02

## Study design and independent work

Check zero par MTM, buyer/seller antisymmetry and alternate-recovery repricing. In the continuous-premium flat-hazard limit, $s=(1-R)\lambda$; quarterly accrual is evaluated using its own convention.

## Required tasks

1. Derive legs and verify zero-hazard/zero-recovery limits and continuous flat spread approximation s=(1-R)*lambda.

2. Implement discrete premium plus accrual and exact piecewise protection integration.

3. Compare fixed hazard and fixed spread experiments; invert five-year quote for hazard at each recovery.

4. Mark to market a legacy coupon across maturity and spread shocks; report spread DV01 and recovery bump holding specified inputs fixed.

5. Compare term-structure prices under alternative recovery assumptions and document non-identification with a recovery-hazard contour.

## Required exhibits

Leg PV and repricing tests; recovery/hazard identification contours; MTM and DV01 tables; sensitivity plots.

## Robustness

A fair-spread identity is not an observed recovery estimate. Distinguish default probabilities under Q from physical probabilities. Account for accrual and cashflow timing; no double counting recovery. Distinct from D09.02.01, which centers on hazard-curve bootstrap.

## Minimum viable thesis

Constant intensity CDS with quarterly accrual, fair spread and inverse calibration; fixed-input versus recalibrated recovery sensitivity and one off-market MTM example.

## Optional extension

Bootstrap hazard buckets and study recovery term structure or a simple dependent default/recovery state model.

## Prerequisites

Fixed income, survival functions, numerical integration and Python.

## Thesis outline

1. Credit derivatives;

2. Intensity pricing;

3. CDS leg implementation;

4. Recovery identification and MTM;

5. Limitations.

## Milestones

W1-3: pricing and accrual; W4-6: implementation; W7-9: inversion; W10-12: sensitivities; W13-16: writing and reproducibility.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
