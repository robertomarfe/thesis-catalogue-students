# Data and model setup | D10.02.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic market: F(0,T)=80, r=2%, sigma=30%, kappa=0.1,0.5,1,2; T=0.5,1,2,5 years; expiry u=T or T/2; strike/F=0.8,1,1.2. Compare matched initial F and matched instantaneous spot sigma, then matched one-year forward variance. Simulate Gaussian X exactly (100,000 paths, seed 2027) and compute F(u,T); compare discounted payoff with Black-76. Use the constant-volatility forward as limiting benchmark.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Check the constant-volatility limit, separate expiry from delivery and hold forward/discount fixed. Use independent seeds, report sampling error and keep both matching designs distinct.

## Timing, accounting and units

Fix currency quote orientation, base currency, return units, settlement dates, funding convention, measure and annualization. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For simulations distinguish expiry from delivery and quote rate from payoff currency.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
