# Data and model setup | D05.04.02

No empirical input bytes are included or validated.

## Input contract

Synthetic BSM S0=100,r=.02,q=.01,sigma=.20, K=80,100,120, T=.25,1. Arithmetic Asian 12 fixings, geometric Asian control. Compare central bumps at relative sizes 1e-1 to 1e-5 with common random numbers, pathwise for continuous payoffs and LR; digital analytic reference and European analytic Greeks; Asian independent high-precision reference using repeated runs and controlled bump bias.

## Input handling

All required inputs are synthetic. Preserve parameters, seed, units, model assumptions, rejected configurations and an independently generated reference. Optional external context requires supervisor agreement and authorized access.

## First-meeting acceptance record

Record actual source version or simulation specification, acquisition rights, date and SHA-256 for any local inputs, schema/units, exclusions, sample or parameter grid and independently designed acceptance checks. Stop and agree a revised design if the specified input is not obtainable. No automatic data or assignment approval.
