# Data and model setup | D10.04.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic S=1.10 USD/EUR, rd/rf grid -1%,0%,2%,5%, sigma 8%,12%,20%, T=.25,1,2y; K/S=.9,1,1.1 and K/F matched separately. Optional historical scenario replay uses DEXUSEU and IR3TIB01USM156N/IR3TIB01EZM156N from https://fred.stlouisfed.org/ for three-month horizon, rate proxies not collateral curves. Assume constant volatility, no market option quotes.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Check parity, fixed-strike sensitivities and self-financing ledger. Separate matched moneyness comparisons from Greeks. Keep quote orientation and foreign accrual explicit.

## Timing, accounting and units

Fix currency quote orientation, base currency, return units, settlement dates, funding convention, measure and annualization. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For simulations distinguish expiry from delivery and quote rate from payoff currency.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
