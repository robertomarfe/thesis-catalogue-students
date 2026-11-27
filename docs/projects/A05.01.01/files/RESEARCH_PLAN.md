# Research plan | A05.01.01

## Study design and independent work

Compare held-out log scores, PIT calibration and parameter uncertainty on identical positive observations. Record optimizer failures and missing months. Distinct from A05.01.03: primary target is the whole conditional density, not conditional variance alone.

## Required tasks

1. Derive both transition densities and check numerical integration and simulated conditional moments.

2. Estimate physical parameters by exact transition maximum likelihood with multiple starts, report boundary/condition diagnostics and uncertainty.

3. Compare log likelihood, AIC, one-month conditional quantiles, PIT and predictive log score on holdout.

4. Simulate stationary or long-run distributions, compare moments, autocorrelation, conditional volatility and negative-rate probability.

5. Plot illustrative Q bond curves using explicitly hypothetical Q parameters; show why P fit alone cannot validate bond prices.

## Required exhibits

Parameter, fit and forecast score tables, density/QQ plots, conditional variance and PIT diagnostics, simulation comparisons and illustrative affine yield curves.

## Robustness

Try alternative start dates and monthly average proxy only as robustness (not exact point observation); compare crisis regimes and discretization of monthly intervals. CIR noncentral chi-square likelihood at zero needs explicit treatment; report unsupported observations. Real bill maturities differ from instantaneous short rate; no direct estimation of market price of risk.

## Minimum viable thesis

Two exact P transition estimators on a verified positive-rate sample, held-out density comparison, simulated rate moments and a clear P/Q distinction with illustrative curves.

## Optional extension

Jointly estimate risk-neutral parameters using GSW zero yields under a measurement-error specification; separate from baseline.

## Prerequisites

Stochastic calculus, likelihood, noncentral chi-square distributions, numerical optimization and Python SciPy.

## Thesis outline

1. Short-rate dynamics and affine pricing;

2. Exact transitions and identification;

3. Proxy data and estimation;

4. Fit and forecast comparison;

5. Pricing implications and limitations.

## Milestones

W1-3: derive transitions and bond formulas; W4-6: acquire and transform rates; W7-9: MLE and simulation; W10-12: holdout and stress analysis; W13-16: Q illustrations and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
