# Data and model setup | D06.02.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic GBM under Q; S0=100, K=70,85,100,115,130; T=0.25,1,2 years; r=0,0.02,0.05; q=0,0.02,0.06; sigma=0.15,0.30,0.50. Use CRR with 250,500,1000,2000 steps and adjacent-tree averaging where oscillatory. Enforce valid risk-neutral probabilities. European BSM and same-tree European prices are benchmarks. Use a dense spot grid near the exercise boundary; document continuous dividend assumption.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
