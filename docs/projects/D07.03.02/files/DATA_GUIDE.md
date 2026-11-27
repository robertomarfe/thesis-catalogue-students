# Data and model setup | D07.03.02

No empirical input bytes are included or validated.

## Input contract

Synthetic flat 2% and upward zero curves, annual fixed payments, option expiries 1,2,5 years, swap tenors 2,5,10 years; ATM and +/-50 bp strikes (keep K>=0 for decomposition). HW a=.03,.10,.30, sigma=.005,.01,.02 rate units/year^0.5. Optional G2++ fit same curve and one ATM quote. MC exact Gaussian factor/integral transitions and discount, 100k paths. GSW curves optional illustration https://www.federalreserve.gov/data/nominal-yield-curve.htm, not swaption market quotes.

## Input handling

All required inputs are synthetic. Preserve parameters, seed, units, model assumptions, rejected configurations and an independently generated reference. Optional external context requires supervisor agreement and authorized access.

## First-meeting acceptance record

Record actual source version or simulation specification, acquisition rights, date and SHA-256 for any local inputs, schema/units, exclusions, sample or parameter grid and independently designed acceptance checks. Stop and agree a revised design if the specified input is not obtainable. No automatic data or assignment approval.
