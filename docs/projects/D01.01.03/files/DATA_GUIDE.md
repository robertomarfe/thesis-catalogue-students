# Data and model setup | D01.01.03

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

S0=100, r=0.02, q=0, T=0.25,1,2 and sigma=0.20. Use Gaussian benchmark, symmetric two-variance mixtures (weights 0.8/0.2, scales 0.6/2), asymmetric location mixtures (weights 0.8/0.2, means 0.3/-1.2, common scale 0.7) and mirror cases. Center/rescale all to same log variance before exponential martingale shift. K/F=0.65 to 1.35 in steps of 0.025. Exact conditional formulas plus MC seed 2027 on 100,000+ paths for selected strikes.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
