# Model setup guide

**Gate: no mandatory external data.** Work in annual units. Use the iid lognormal mean 0.02 and SD 0.02; beta 0.96, 0.98, 0.99; gamma 2, 5, 10; psi 0.5, 1.5, 2.5. Two-state baseline means 0.005 and 0.035, stay 0.9, conditional SD 0.02. Its unconditional SD is 0.025; match variance with iid as a separate sensitivity. For the consumption-wealth benchmark, set dividend growth equal to consumption growth if including that claim. Use the Euler-derived equation in the focused methods note. Do not use singular gamma=1 or psi=1 formulas without separately derived limits. Report rejected parameter cells, positivity, spectral margins, log and arithmetic returns. Optional source for context only: FRED real PCE per capita A794RX0Q048SBEA (https://fred.stlouisfed.org/series/A794RX0Q048SBEA); no empirical file required or supplied.

## First-meeting acceptance record

Record actual source version or simulation specification, acquisition rights, date and SHA-256 for any local inputs, schema/units, exclusions, sample or parameter grid and independently designed acceptance checks. Stop and agree a revised design if the specified input is not obtainable. No automatic data or assignment approval.
