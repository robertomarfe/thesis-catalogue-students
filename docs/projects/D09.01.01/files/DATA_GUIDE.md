# Data and model setup | D09.01.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic firm with V0=100, F/V0 from 0.3 to 1.2, sigma_V=10%,20%,40%, r=2%, mu=6%, T=1,3,5 years. Fix assumptions in annual units. Compute equity and debt analytically; verify with independent Q simulation discounted min(V_T,F) and P simulation default frequencies. Include limiting cases near zero volatility and low leverage; use log-tail-safe methods for small spreads. No firm data needed.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Verify asset-value conservation, the upper bound on debt and probability intervals. Report simulation uncertainty in rare-default cases and physical-drift sensitivity separately from risk-neutral pricing. Keep all other parameters fixed in each comparative static.

## Timing, accounting and units

Specify physical versus risk-neutral probability, discounted versus undiscounted cash flows, maturity and year fractions, and whether rates and spreads are decimals, percentages or basis points. Document default timing and recovery. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For finite-state models define the state support, probability mass and numerical tolerance before fitting.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
