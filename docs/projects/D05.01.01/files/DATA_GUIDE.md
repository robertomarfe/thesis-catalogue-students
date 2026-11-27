# Data and model setup | D05.01.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

S0=100, r=2%, q=0, sigma=20%, T=1, K=80,100,120; arithmetic and geometric averages over 12 equally spaced dates excluding t=0. Draw exact log-price increments under Q. Test 2^10, 2^12, 2^14 and 2^16 raw paths with 30-100 independent replications, common seeds within comparisons and pilot samples for control coefficients. Use BSM European analytic price; for Asian arithmetic price use a separately computed high-precision estimate with MC uncertainty, never label it exact. Record hardware and timing rules.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
