# Research plan | A06.04.02

## Study design and independent work

Use return-first VAR, stable roots, same calendar and real gross convention; verify direct discounted sums and signed Var(CF)+Var(DR)-2Cov identity, report finite and infinite estimates, horizon and information-set sensitivity. Refit rho and VAR inside bootstrap, retain inadmissible draws and note weak stability near unit roots.

## Prespecified implementation

Original VAR state first log real total return, then log D/P and short rate, alternative term spread. Deflate nominal gross returns by December CPI ratio, preserve year timing and avoid Shiller interpolated payout as annual exact. Center stationary VAR; return_news(A,rho,H) uses H future dates, excluding t, returns CF residual and DR. N_CF=u_r+N_DR; residual CF absorbs terminal and approximation/omitted news. Report Var(CF)+Var(DR)-2Cov and signed shares; bootstrap VAR and rho with joint innovations, retain invalid draw counts, compare finite and infinite horizons and two information sets. Optional direct dividend-news check requires actual g and alternative state order; not an independent identified shock.

## Required tasks

1. Derive Campbell-Shiller return-news identity, state selector and sign; audit returns and D/P timing.

2. Estimate stationary VAR; report eigenvalues, residual covariance and forecast diagnostic.

3. Compute N_DR and residual N_CF; verify accounting identity observation by observation and variance/covariance shares.

4. Re-estimate all parameters within residual or moving-block bootstrap (common innovations); report unstable draws and finite-horizon results without silently deleting them.

5. Compare alternative information sets, rho, rolling/subperiod estimates and optional realized dividend-growth forecast revisions as diagnostic.

## Required exhibits

VAR estimates and eigenvalues, time series of both news components, variance decomposition including covariance term, intervals and finite-horizon robustness.

## Robustness

Infinite sum requires spectral radius of rho*A below one; near-unit-root results fragile. Residual N_CF not a structural cash-flow shock and absorbs omitted news and approximation error; no causal attribution. Annual sample modest; avoid many predictors and do not impose nonnegative variance shares. Distinct from A06.01.02 forecast-level decomposition of valuation ratios.

## Minimum viable thesis

One stable annual VAR, exact algebra checks, news series, variance/covariance table, finite versus infinite horizon and two information sets with uncertainty.

## Optional extension

Use a richer monthly VAR with explicit cash-flow proxy and compare with a direct dividend-growth forecast system or GKK equity duration.

## Prerequisites

Asset valuation, VAR, matrix algebra, bootstrap and Python.

## Thesis outline

1. Log-linear return identity;

2. VAR information set and timing;

3. News construction;

4. Decomposition and uncertainty;

5. Economic interpretation.

## Milestones

W1-3: derive news formulas; W4-6: construct annual data; W7-9: VAR and decomposition; W10-12: bootstrap and robustness; W13-16: interpret and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
