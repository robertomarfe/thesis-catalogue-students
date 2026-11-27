# Data and model setup | D05.02.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

S0=100, K=80/100/120, T=0.25/1, r=0.02/0.05, sigma=0.15/0.30. Compare trees with N=50 to 3200 and finite differences with space/time grids separately refined, fixed residual tolerance and expanded Smax. Use independent high-resolution price references from both methods and demand agreement within a specified dollar tolerance (e.g. 0.005) or flag unresolved error. Compare European puts against BSM first; boundaries only where grid resolution supports them.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
