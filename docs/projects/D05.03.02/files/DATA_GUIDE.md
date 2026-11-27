# Data and model setup | D05.03.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

S0=100, r=.02, q=0; T=.02,.25,1,3y, K/S0=.7,.9,1,1.1,1.4. BSM baseline sigma=.20; Merton jumps with intensity .5 or 2, mean log jump -.08, sd .15 and compensator; optional Heston. N=16 to 1024, several interval widths; analytic BSM and converged Poisson-mixture Merton values as independent references. Python float64, warm repeated wall-clock timing and fixed hardware.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
