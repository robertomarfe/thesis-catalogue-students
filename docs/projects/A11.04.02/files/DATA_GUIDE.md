# Data and model setup | A11.04.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic annual state persistence .85, R_f=1.02, mu(low)=.02, mu(high)=.08, s=.20. Simulate 5000 samples of 80 and 200 periods, common paths for both SDF interpretations; baseline regression of excess return on lagged observed state. Add noisy consumption proxy independent of epsilon and a correlated proxy as controlled auxiliary evidence. Goyal predictor data optional illustration only, not needed for identification result.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Preserve 5,000 common samples at the specified 80/200 horizons, positivity and conditional moments, and prespecified noisy proxies. Compare paired inference, and distinguish a failure of the constant kernel from an identification of market inefficiency.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
