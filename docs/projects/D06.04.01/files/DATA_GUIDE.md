# Data and model setup | D06.04.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Two or three assets, initial normalized prices 1, equal weights, r=.02, q=.01, sigma=.2 or (.15,.30,.25), T=.5,1,3, K=.8,1,1.2. Equicorrelation -.4,0,.3,.7,.95,1 (three assets lower bound -.5); exact terminal MC, common Gaussian draws with stable eigendecomposition, 100k paths, independent replicates. Use control variate for geometric basket call where analytic available.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
