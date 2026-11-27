# Data and model setup | A06.03.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic value cash-flow profile c_j=5*exp(.01*(j-1)); growth profile c_j=1*exp(.15*(j-1)) through year 10, then .02 growth; normalize each to common P at y=.08. Compute 50-year and 100-year truncation, y=.04..12, parallel +/-50/100 bp and maturity-dependent rate shifts. Optional but recommended historical comparison: French 25 size/BM VW portfolios and FF3 monthly https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; GSW SVENY02/10 https://www.federalreserve.gov/data/nominal-yield-curve.htm, common 1963-2025. Average low/high BM portfolios across size bins, compare growth-minus-value returns with monthly yield changes controlling for market.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Distinguish physical growth laws, state-price kernels and traded payoff definitions. Optional external context does not change the synthetic core.

## Frozen research design (original catalogue)

Synthetic value cash-flow profile c_j=5*exp(.01*(j-1)); growth profile c_j=1*exp(.15*(j-1)) through year 10, then .02 growth; normalize each to common P at y=.08. Compute 50-year and 100-year truncation, y=.04..12, parallel +/-50/100 bp and maturity-dependent rate shifts. Optional but recommended historical comparison: French 25 size/BM VW portfolios and FF3 monthly https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; GSW SVENY02/10 https://www.federalreserve.gov/data/nominal-yield-curve.htm, common 1963-2025. Average low/high BM portfolios across size bins, compare growth-minus-value returns with monthly yield changes controlling for market.

## Design-specific acceptance

Normalize two positive cash-flow profiles to identical PV, confirm weights sum to one and analytic duration/convexity via central differences at multiple step sizes. Compare parallel/nonparallel shifts and explicit changed cash-flow scenario; test 50/100y truncation. Historical evidence is optional; no claim about observed growth/value beta without matched data.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Separate model-implied curves from traded prices, real safe payoffs from ex post real returns, and conditional from unconditional moments.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
