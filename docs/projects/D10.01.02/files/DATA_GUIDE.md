# Data and model setup | D10.01.02

No empirical input bytes are included or validated.

## Input contract

Synthetic curves only: S0=80, r=0.03, a=0.04, delta0=-0.05,0.04,0.15; kappa=0.5,2; sigma_S=0.30, sigma_d=0.10, rho=-0.5,0,0.5; maturities 1,3,6,12,24,60 months. Use jointly Gaussian exact innovations for log spot and delta, or fine-grid integration with convergence; 50,000 MC paths seed 31415. For risk experiments compare analytical curve changes under one-standard-deviation spot and yield shocks.

## Input handling

All required inputs are synthetic. Preserve parameters, seed, units, model assumptions, rejected configurations and an independently generated reference. Optional external context requires supervisor agreement and authorized access.

## First-meeting acceptance record

Record actual source version or simulation specification, acquisition rights, date and SHA-256 for any local inputs, schema/units, exclusions, sample or parameter grid and independently designed acceptance checks. Stop and agree a revised design if the specified input is not obtainable. No automatic data or assignment approval.
