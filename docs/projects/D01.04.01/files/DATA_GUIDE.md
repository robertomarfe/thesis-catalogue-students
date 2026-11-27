# Data and model setup | D01.04.01

No empirical input bytes are included or validated.

## Input contract

S0=100, r=.02, q=.01, maturities .05,.25,1,2Y; forward log-moneyness -0.30 to 0.30. VG theta=-.12, nu=.2, sigma=.18; compare BSM and Merton with the same annual variance and forward, vary theta/nu while adjusting sigma feasibly. Price VG by conditional Gaussian mixture quadrature over gamma clock, check with characteristic-function integration or independently sampled gamma MC, use stable short-maturity near-zero quadrature. Seed 101401; 100,000+ paths for diagnostics only.

## Input handling

All required inputs are synthetic. Preserve parameters, seed, units, model assumptions, rejected configurations and an independently generated reference. Optional external context requires supervisor agreement and authorized access.

## First-meeting acceptance record

Record actual source version or simulation specification, acquisition rights, date and SHA-256 for any local inputs, schema/units, exclusions, sample or parameter grid and independently designed acceptance checks. Stop and agree a revised design if the specified input is not obtainable. No automatic data or assignment approval.
