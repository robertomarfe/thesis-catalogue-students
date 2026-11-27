# Data and model setup | D04.01.01

No empirical input bytes are included or validated.

## Input contract

S0=100, r=0.02, q=0, mu=0.06 (and mu=r robustness), sigma=0.15/0.30, K=90/100/110, T=0.25/1. Exact GBM on a finest uniform grid of 256 steps; use nested 4,16,64,256 rebalancing intervals and common paths. At least 20,000 paths per scenario, documented random seed and independent replication. Frictionless baseline; compute gross dollar turnover without charging costs, since D04.03.01 studies cost optimization.

## Input handling

All required inputs are synthetic. Preserve parameters, seed, units, model assumptions, rejected configurations and an independently generated reference. Optional external context requires supervisor agreement and authorized access.

## First-meeting acceptance record

Record actual source version or simulation specification, acquisition rights, date and SHA-256 for any local inputs, schema/units, exclusions, sample or parameter grid and independently designed acceptance checks. Stop and agree a revised design if the specified input is not obtainable. No automatic data or assignment approval.
