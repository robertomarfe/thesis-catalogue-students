# Data and model setup | D10.04.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

S0=1.10 USD/EUR, r_d=.04,r_f=.02; T=.08,.25,1y, log(K/F)=-.2 to .2. Target ATM Garman-Kohlhagen vol .12; intensity .1,.5,1.5; log jump mean -.08,0,.08 and sd .08,.15. Truncate Poisson mixture by error bound/check additional terms; independent exact compound-Poisson terminal simulations with confidence intervals. No observed FX option data needed.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Check martingale, parity, zero intensity, truncation including stock-weighted tail, ATM feasibility and independent Monte Carlo. Report infeasible cases; no observed smile claim.

## Timing, accounting and units

Fix currency quote orientation, base currency, return units, settlement dates, funding convention, measure and annualization. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For simulations distinguish expiry from delivery and quote rate from payoff currency.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
