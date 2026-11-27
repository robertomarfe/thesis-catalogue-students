# Data and model setup | A11.01.01

No empirical input bytes are included or validated.

## Input contract

Synthetic 4/8/20 equiprobable or unequal-probability states, positive reference SDF, 1 riskless and 1-6 risky payoffs with fixed seeds; construct nested spans, redundant and nearly collinear assets, complete benchmark. Compute prices from reference m; solve weighted least squares and nonnegative constrained QP, use LP for strictly positive feasibility. Optional French factor moments only as illustration.

## Input handling

All required inputs are synthetic. Preserve parameters, seed, units, model assumptions, rejected configurations and an independently generated reference. Optional external context requires supervisor agreement and authorized access.

## First-meeting acceptance record

Record actual source version or simulation specification, acquisition rights, date and SHA-256 for any local inputs, schema/units, exclusions, sample or parameter grid and independently designed acceptance checks. Stop and agree a revised design if the specified input is not obtainable. No automatic data or assignment approval.
