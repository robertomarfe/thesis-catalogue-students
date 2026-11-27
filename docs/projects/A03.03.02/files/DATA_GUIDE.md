# Data and model setup | A03.03.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Annual mu=.02, beta=.98,.99, gamma=2,5,10, psi=.75,1.5,2; a=.005,.01, rho=0,.5,.9,.98; fix total SD(g)=.02 with sigma=sqrt(.02^2-a^2). Dividends mu_d=.02, phi=1,3, phi_e=1,2, sigma_d=.06; no cointegration assumed. Compare iid expected-growth state (rho=0; still known x_t) with strict iid growth a=0, matching unconditional mean/SD; CRRA psi=1/gamma and persistent cases. Optional empirical consumption and real stock returns from FRED and French; illustrative annual targets mean real rf 0-2%, equity premium 4-7%, stock vol 15-20%, not guaranteed fit.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Distinguish physical growth laws, state-price kernels and traded payoff definitions. Optional external context does not change the synthetic core.

## Frozen research design (original catalogue)

Annual mu=.02, beta=.98,.99, gamma=2,5,10, psi=.75,1.5,2; a=.005,.01, rho=0,.5,.9,.98; fix total SD(g)=.02 with sigma=sqrt(.02^2-a^2). Dividends mu_d=.02, phi=1,3, phi_e=1,2, sigma_d=.06; no cointegration assumed. Compare iid expected-growth state (rho=0; still known x_t) with strict iid growth a=0, matching unconditional mean/SD; CRRA psi=1/gamma and persistent cases. Optional empirical consumption and real stock returns from FRED and French; illustrative annual targets mean real rf 0-2%, equity premium 4-7%, stock vol 15-20%, not guaranteed fit.

## Design-specific acceptance

Within each fixed a compare rho holding all other primitives fixed; report VR(h), stationary premium and rate, P/D and return volatility, matched CRRA and strict iid, spectral margins and all rejected cells. Independent finite-horizon wealth convergence and quadrature SDF kernels; if pricing with approximate wealth, report its own Euler errors and both premium/yield implications. No claim this replicates BY stochastic-volatility calibration.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Separate model-implied curves from traded prices, real safe payoffs from ex post real returns, and conditional from unconditional moments.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
