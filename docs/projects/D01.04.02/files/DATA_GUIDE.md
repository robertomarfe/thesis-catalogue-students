# Data and model setup | D01.04.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

xi0=.04, S0=100, r=q=0, eta=1.2, rho=-.7, H=.1,.25,.5; maturities 1,2,4,8,16,32 weeks. Use hybrid convolution or exact joint Gaussian covariance of Y-grid and Brownian increments on modest grids, left-point variance in log-price Euler. Log strikes +/- c sqrt(T) with c=.05,.10,.20; examine c sensitivity toward ATM. Start 100,000 paired paths with antithetics/conditional MC; seed 101402; refine grids at shortest maturities and check discounted stock mean. Avoid positive-rho martingale complications.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
