# Data and model setup | D11.02.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Generate normalized calls from BSM and a two-component lognormal mixture with positive weights and means chosen to average to one. T=0.25,1,2; 15/31/61 strikes on k=0.65..1.35 and optional wider tails. Add centered price noise of 0, 0.0001, 0.001 normalized price units (100 replicates per setting, seed 2027). Compare naive finite differences, convex least squares on quotes with interpolated survival, and constrained density recovery on x=0..4; extend support to 8 as check. Reference exact mixture density and CDF.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Do not silently clip negative density estimates and call them calibrated distributions. Track feasibility, normalization, tail sensitivity and uncertainty across the prescribed grids. Distinguish distribution recovery from smile interpolation.

## Timing, accounting and units

Specify physical versus risk-neutral probability, discounted versus undiscounted cash flows, maturity and year fractions, and whether rates and spreads are decimals, percentages or basis points. Document default timing and recovery. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For finite-state models define the state support, probability mass and numerical tolerance before fitting.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
