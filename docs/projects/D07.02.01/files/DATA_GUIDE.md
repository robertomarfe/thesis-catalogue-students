# Data and model setup | D07.02.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Core S-class: construct P0(T)=exp(-integral f0) from smooth flat, upward and humped instantaneous forwards, e.g. f0=0.02+0.01*(1-exp(-T)) plus optional hump 0.015*T*exp(-T). Maturities 0-30y. a=0.03/0.15/0.5, sigma=0.005/0.01/0.02. Bond options t_e=1,2,5; T=t_e+5; K at 0.9/1/1.1 times forward. Optional public GSW dated curve via https://www.federalreserve.gov/data/nominal-yield-curve.htm; smooth log discounts, no OIS claims. Compare exact-curve model with Vasicek constant drift fitted by least squares.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Report curve recovery, price and numerical error separately; evaluate all prescribed curves and a range of option parameters. Do not present an exact fit as evidence that option values are identified.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
