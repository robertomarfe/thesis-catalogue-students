# Research plan | A03.04.02

## Study design and independent work

Show FMP equality and zero covariance zero premium; report matched expected gross growth, covariance and q_d existence across four cases. Separate variance-only and covariance changes (when feasible), and beta-adjusted safe-rate diagnostic with bounds. Verify pricing moments by independent Gaussian integration or MC and report price-existence failures.

## Prespecified implementation

Use iid joint Gaussian log growth; baseline aggregate consumption sigma=.02, shareholder sigma_s grid .02-.10. Mean-adjust mu_s=.02+.5*(.02^2-sigma_s^2) for matched expected gross growth. Dividend marginal unchanged; vary rho or sigma, hold covariance rho*sigma_s*sigma_d fixed only where feasible, or adjust beta to match rf and mark if outside bounds. FMP means pricing with aggregate consumption, not a distinct general-equilibrium model. Verify covariance-zero premium and independent MC; report nonfinite prices.

## Required tasks

1. Derive safe and equity prices and covariance premium.

2. Verify FMP equality and rho=0 zero premium.

3. Map premium, rf and P/D across risk and correlation; flag price nonexistence.

4. Separate volatility from covariance effects using matched covariance or matched rf scenarios.

5. Compare MC and formulas; discuss missing market-clearing restrictions and empirical data needs.

## Required exhibits

Equity premium/rf surfaces, admissibility map, FMP comparison, covariance decomposition and MC check.

## Robustness

Shareholder consumption is exogenous, not derived from equilibrium labor income or participation decisions. Positive shareholder wealth/consumption not a full aggregation identity. Do not interpret increased total volatility as priced covariance automatically.

## Minimum viable thesis

IID CRRA analytic benchmark and four shareholder scenarios with price existence and MC checks.

## Optional extension

Two household types with explicit resource feasibility in a finite-state economy; solve endowment allocation and prices.

## Prerequisites

Consumption-based pricing, lognormal moments, Python.

## Thesis outline

1. Participation and consumption;

2. SDF and pricing;

3. Quantitative scenarios;

4. Premium/rf trade-off;

5. Limits.

## Milestones

W1-3: theory; W4-6: exact pricing; W7-9: scenarios; W10-12: MC and economic checks; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
