# Data and model setup | D07.02.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic flat 3% continuously compounded curve; r0=b=.03,a=.5,sigma=.01,eta=sigma/sqrt(.03); expiries .5,1,2y, underlying maturities u+2,u+5; K/F=.85,.95,1,1.05,1.15. Use deterministic shift to match curve, then match one ATM option. Use exact transition or fine-step discounted MC, convergence and 95% intervals. Optional empirical curve from https://www.federalreserve.gov/data/nominal-yield-curve.htm; no option quotes required.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Freeze the ATM match before comparing other strikes; report domain and uncertainty rather than forcing implied volatilities for zero prices. Distinct from A05.01.01 physical transition estimation.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
