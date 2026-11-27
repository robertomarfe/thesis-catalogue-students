# Data and model setup | D06.04.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic EUR domestic, USD foreign, X EUR/USD=.9, k=.9, S0=K=100 USD, r_d=.02,r_f=.04,q=.01,sigma_S=.25,sigma_X=.05-.20,rho=-.8 to .8,T=.25,1,3. Exact correlated Gaussian terminal simulation under domestic Q, analytic formula and independent foreign-Q option conversion. Compare same k and X0 at inception, then bump rho and sigma_X independently.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
