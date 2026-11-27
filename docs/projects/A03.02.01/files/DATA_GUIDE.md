# Data and model setup | A03.02.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Quarterly finite-state example: g=0.005 +/-0.01 with equal probabilities, s in {0.05,0.10,0.20}, beta per quarter from annual 0.96-0.995, gamma 2-8. With probability 0.2 conditional on growth shock, move surplus one grid step in the same direction (reflect by staying at bounds); otherwise stay. Vary this probability and grid spacing; compute exact conditional expectations and stationary state weights, not simulated moments alone. Compare CRRA s constant and an independent surplus transition with the same marginal probabilities. Check spectral radius and positivity before reporting any prices; not an exact Campbell-Cochrane calibration.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Distinguish physical growth laws, state-price kernels and traded payoff definitions. Optional external context does not change the synthetic core.

## Frozen research design (original catalogue)

Quarterly finite-state example: g=0.005 +/-0.01 with equal probabilities, s in {0.05,0.10,0.20}, beta per quarter from annual 0.96-0.995, gamma 2-8. With probability 0.2 conditional on growth shock, move surplus one grid step in the same direction (reflect by staying at bounds); otherwise stay. Vary this probability and grid spacing; compute exact conditional expectations and stationary state weights, not simulated moments alone. Compare CRRA s constant and an independent surplus transition with the same marginal probabilities. Check spectral radius and positivity before reporting any prices; not an exact Campbell-Cochrane calibration.

## Design-specific acceptance

Verify each conditional joint row sums to one, shock marginals and P are identical across coupling cases, same stationary weights, CRRA constant-surplus and Euler checks. Show covariance identity by state and distinguish SDF volatility from priced covariance; retain nonfinite present-value cells.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Separate model-implied curves from traded prices, real safe payoffs from ex post real returns, and conditional from unconditional moments.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
