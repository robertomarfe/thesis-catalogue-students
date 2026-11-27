# Data and model setup | D11.02.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

F=100, r=.02,T=1, lognormal Q sigma=.2 and two-lognormal mixture with weights .8/.2, component forwards 105/80 (weighted F=100), vol .15/.30. Generate analytic call/put prices and exact log moments. Strike ranges K/F .5-1.5, .7-1.3, .85-1.15; 11/41/101 strikes, price noise 0/1/5 cents, seed 2027. Compare trapezoid, quadrature and explicitly labeled lognormal-tail extrapolation. No external data.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Report absolute moment errors and cancellation across strip, tail and noise choices. Compare central moments only on admissible inputs. Record the exact support and quote tolerance for conditional bounds.

## Timing, accounting and units

Specify physical versus risk-neutral probability, discounted versus undiscounted cash flows, maturity and year fractions, and whether rates and spreads are decimals, percentages or basis points. Document default timing and recovery. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For finite-state models define the state support, probability mass and numerical tolerance before fitting.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
