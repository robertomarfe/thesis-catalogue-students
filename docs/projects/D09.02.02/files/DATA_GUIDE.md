# Data and model setup | D09.02.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic par CDS 1,3,5,7,10y, quarterly payments, r=.025, flat hazard .01,.03,.08 or piecewise constant; recovery .2,.4,.6. Generate quotes from known parameters. Integrate default accrual exactly or accurately with piecewise quadrature. Test calibrated hazard at alternate R, off-market contract with coupon 100 or 500 bp. No live spreads or ISDA production-pricer claim.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Check zero par MTM, buyer/seller antisymmetry and alternate-recovery repricing. In the continuous-premium flat-hazard limit, $s=(1-R)\lambda$; quarterly accrual is evaluated using its own convention.

## Timing, accounting and units

Specify physical versus risk-neutral probability, discounted versus undiscounted cash flows, maturity and year fractions, and whether rates and spreads are decimals, percentages or basis points. Document default timing and recovery. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For finite-state models define the state support, probability mass and numerical tolerance before fitting.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
