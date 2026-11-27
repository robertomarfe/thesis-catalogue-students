# Data and model setup | A03.04.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Synthetic annual mu=.02, sigma_c=.02, mu_s=.02, sigma_s=.02-.10, rho=.25-1, mu_d=.02, sigma_d=.12, beta=.96-.99,gamma=2,5,8. Evaluate exact lognormal expectations and independent MC. For higher shareholder risk, also mean-adjust mu_s to match expected gross consumption growth. No claim that these exogenous processes clear aggregate goods markets or represent a calibrated two-agent equilibrium. FRED consumption illustration optional.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Distinguish physical growth laws, state-price kernels and traded payoff definitions. Optional external context does not change the synthetic core.

## Frozen research design (original catalogue)

Synthetic annual mu=.02, sigma_c=.02, mu_s=.02, sigma_s=.02-.10, rho=.25-1, mu_d=.02, sigma_d=.12, beta=.96-.99,gamma=2,5,8. Evaluate exact lognormal expectations and independent MC. For higher shareholder risk, also mean-adjust mu_s to match expected gross consumption growth. No claim that these exogenous processes clear aggregate goods markets or represent a calibrated two-agent equilibrium. FRED consumption illustration optional.

## Design-specific acceptance

Show FMP equality and zero covariance zero premium; report matched expected gross growth, covariance and q_d existence across four cases. Separate variance-only and covariance changes (when feasible), and beta-adjusted safe-rate diagnostic with bounds. Verify pricing moments by independent Gaussian integration or MC and report price-existence failures.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Separate model-implied curves from traded prices, real safe payoffs from ex post real returns, and conditional from unconditional moments.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
