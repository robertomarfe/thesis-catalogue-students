# Data and model setup | D05.01.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Use S0=100, r=0.02, q=0, sigma=0.2/0.4, T=1, K=80/100/120, m=12,52,252 equally spaced fixings. Compare IID MC, scrambled Sobol with chronological increments, and scrambled Sobol with Brownian bridge using N=2^10 to 2^16 per replication and at least 24 independent replications. Use same payoff and path conventions. Reference: independently coded high-budget MC with geometric-Asian control variate and uncertainty sufficiently smaller than candidate errors; increase budget or flag unresolved differences.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
