# Research plan | D10.02.02

## Study design and independent work

Check the constant-volatility limit, separate expiry from delivery and hold forward/discount fixed. Use independent seeds, report sampling error and keep both matching designs distinct.

## Required tasks

1. Derive forward price, martingale and total variance; check kappa->0 limit numerically.

2. Price calls and puts analytically and by independent Monte Carlo with confidence intervals.

3. Plot ATM option time value and implied forward volatility against expiry and delivery lag.

4. Decompose effects of changing kappa versus re-matching the reference contract volatility.

5. Add a two-factor Gaussian log-spot/convenience yield scenario, using the integrated squared forward diffusion and correlation term; test whether maturity patterns remain monotonic.

## Required exhibits

Formula checks, option price/error table, expiry-delivery heatmaps, volatility term structures, matched-variance comparison.

## Robustness

Use deterministic rates and European payoff on F(u,T), not S_u unless u=T. Ensure Q drift and initial curve are consistent; forward and futures equality needs deterministic rates. Gaussian model is an illustrative positive-price model, not calibrated oil data.

## Minimum viable thesis

One-factor derivation, two matching designs, analytic/Monte Carlo agreement and economic interpretation of delivery lag; two-factor extension optional. Distinct from D10.01.02, which studies the forward curve itself.

## Optional extension

With lawful historical options and futures quotes, estimate volatility term structure and test one-factor restrictions.

## Prerequisites

Gaussian processes, risk-neutral pricing, Black formula, Monte Carlo.

## Thesis outline

1. Commodity forward economics;

2. Mean-reverting model and Black pricing;

3. Synthetic experiment;

4. Maturity and matching comparisons;

5. Limitations.

## Milestones

W1-3: derive dynamics and pricing; W4-6: implement analytic benchmark and simulation; W7-9: maturity grids and matched comparisons; W10-12: robustness and optional second factor; W13-16: write and reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
