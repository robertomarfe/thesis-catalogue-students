# Data and model setup | D07.03.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic annuity A=1 initially, expiries .25,1,5y, F=-.005,0,.005,.02,.05; strikes F plus/minus 100 and 50 bp, ATM. Fix normal vol 50 bp/sqrt(year). Match shifted Black ATM price for s=.02,.05 via root solving when feasible; unshifted Black only for positive F,K. Use analytic formula and Gaussian/lognormal quadrature. No market vol surface required.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Keep infeasible targets and strikes in a domain map. Distinguish rate-volatility pricing convention from D07.03.02 one-factor model calibration and curve risk.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
