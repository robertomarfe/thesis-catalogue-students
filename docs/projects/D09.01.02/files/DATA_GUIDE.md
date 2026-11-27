# Data and model setup | D09.01.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

V0=100,F=60,r=0.03,sigma=0.15/0.30/0.50,H=30/45/55,R=0/0.3/0.5 where R F<=H; T=0.25,0.5,1,2,5,10. Simulate 100,000+ exact log-GBM endpoints with seed 2027 and bridge conditional survival weights; independent analytic survival and Merton closed-form benchmarks. Use maturity-contingent recovery for baseline, clearly not a standard traded covenant specification.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Show the analytic hit check, bridge versus endpoint-only monitoring and common-path paired intervals. Compare the maturity-only benchmark under identical terminal inputs. Preserve unsuccessful or high-error grid cases and quantify both default timing and loss effects.

## Timing, accounting and units

Specify physical versus risk-neutral probability, discounted versus undiscounted cash flows, maturity and year fractions, and whether rates and spreads are decimals, percentages or basis points. Document default timing and recovery. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For finite-state models define the state support, probability mass and numerical tolerance before fitting.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
