# Data and model setup | D06.03.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic GBM, S0=100, r=.02, q=.01, sigma=.2, T=3y, quarterly dates, B=.6,.7,.8. Baseline issuer default-free; optional independent constant intensity .01-.03 with zero recovery to illustrate credit discounting. Simulate exact observation-date paths, 100,000 or more, fixed seeds, common random numbers for bumps; P drift .04-.08 for loss scenarios. No continuous barrier or issuer quotation assumed.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
