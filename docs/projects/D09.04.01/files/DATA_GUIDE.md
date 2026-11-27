# Data and model setup | D09.04.01

No empirical input bytes are included or validated.

## Input contract

Synthetic equity forward S0=100, K=100*exp((r-q)*T), r=.02, q=.01, sigma=.15-.40, T=1,3,5 years, h=.005-.05, R=.4. Analytic EPE plus quadrature; independent exact GBM Monte Carlo on time grid and independently sampled exponential default times. Required wrong-way-risk comparison at one maturity: adapted Cox intensity with a deterministic baseline fitted to the independent survival curve on the grid; compare separately with fixed baseline. GSW optional illustration only.

## Input handling

All required inputs are synthetic. Preserve parameters, seed, units, model assumptions, rejected configurations and an independently generated reference. Optional external context requires supervisor agreement and authorized access.

## First-meeting acceptance record

Record actual source version or simulation specification, acquisition rights, date and SHA-256 for any local inputs, schema/units, exclusions, sample or parameter grid and independently designed acceptance checks. Stop and agree a revised design if the specified input is not obtainable. No automatic data or assignment approval.
