# Data and model setup | D01.04.03

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Generate three known-truth surfaces (BSM, Merton, Heston) with S0=100, r=.02,q=.01, maturities .1,.25,.5,1,2Y, strikes k=-.25 to .25. Use independent high-precision pricers, 20 seeded panels with synthetic heteroskedastic bid/ask-like noise, and fixed training/validation/holdout strikes plus one interior maturity withheld. Holdouts not used for tuning. Report noise-free target error and noisy quote error separately; seed 101403. Include no-noise exact nested limits where admissible; Heston need not contain Merton.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
