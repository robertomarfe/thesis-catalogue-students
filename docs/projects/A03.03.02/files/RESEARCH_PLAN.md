# Research plan | A03.03.02

## Study design and independent work

Within each fixed a compare rho holding all other primitives fixed; report VR(h), stationary premium and rate, P/D and return volatility, matched CRRA and strict iid, spectral margins and all rejected cells. Independent finite-horizon wealth convergence and quadrature SDF kernels; if pricing with approximate wealth, report its own Euler errors and both premium/yield implications. No claim this replicates BY stochastic-volatility calibration.

## Prespecified implementation

Annual mu=.02, beta=.98,.99, gamma=2,5,10, psi=.75,1.5,2; a=.005,.01, rho=0,.5,.9,.98; fix total SD(g)=.02 with sigma=sqrt(.02^2-a^2). Dividends mu_d=.02, phi=1,3, phi_e=1,2, sigma_d=.06; no cointegration assumed. Compare iid expected-growth state (rho=0; still known x_t) with strict iid growth a=0, matching unconditional mean/SD; CRRA psi=1/gamma and persistent cases. Optional empirical consumption and real stock returns from FRED and French; illustrative annual targets mean real rf 0-2%, equity premium 4-7%, stock vol 15-20%, not guaranteed fit.

## Required tasks

1. Derive finite-state wealth equation, analytic conditional moments and iid benchmark.

2. Solve in logs with residual and positivity checks, verify Euler equations; compare log-linear approximation around stationary ratio to exact solution.

3. Price dividend claim using spectral radius(K)<1 and linear solve; reject invalid cases, verify expected simple returns and risk-free.

4. Compute stationary moments, valuation ratio, growth variance ratios and premium across matched-persistence/preferences grid; separate cash-flow leverage effect.

5. Compare CRRA vs EZ and a=0 counterfactuals; show cases where targets fail; optional calibration of 2-3 parameters only with held-out moments.

## Required exhibits

Euler residuals/admissibility table; comparative statics of wealth and dividend premia, real rf and valuation volatility; growth variance-ratio and approximation error plots.

## Robustness

Finite-state model is stylized; no claim to replicate BY 2004. Fixed unconditional consumption SD does not fix higher-horizon variance; annual parameters not monthly. Solve exact benchmark before log-linearization, report spectral radius and ill-conditioning. No time-varying volatility baseline; extension separate.

## Minimum viable thesis

Two-state exact EZ solution, verified pricing kernel and dividend claim, matched consumption mean/SD comparison across persistence and preferences, log-linear diagnostic. Distinct from A03.03.01 preference separation itself.

## Optional extension

Add two volatility states or estimate a/rho from consumption; retain fixed preferences and avoid weakly identified overfitting.

## Prerequisites

Recursive preferences, Markov chains, asset pricing, nonlinear equations and numerical linear algebra.

## Thesis outline

1. Long-run risk mechanism;

2. Recursive utility and finite-state model;

3. Exact and approximate pricing;

4. Quantitative counterfactuals;

5. Economic limitations.

## Milestones

W1-3: EZ and BY reading; W4-6: exact wealth solver; W7-9: dividend claims and Euler tests; W10-12: persistence and preferences; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
