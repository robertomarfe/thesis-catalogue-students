# Data and model setup | D05.02.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

S0=100,K=100,r=0.03,q=0.01,sigma=0.2/0.6,T=0.02,0.25,1; x centered at log K with domain +/- 5-8 sigma sqrt(T) plus drift margin, test wider domain. European call and digital cash payoff; analytic BSM references. Use 50,100,200,400 intervals; dt on both sides of explicit stability limit, and stable fixed dt paths. Enforce asymptotic Dirichlet boundaries; compare strike at grid node and half-node, payoff cell average for digital. Tridiagonal solves and wall-time measured consistently.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
