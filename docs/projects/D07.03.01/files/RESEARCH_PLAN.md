# Research plan | D07.03.01

## Study design and independent work

Keep infeasible targets and strikes in a domain map. Distinguish rate-volatility pricing convention from D07.03.02 one-factor model calibration and curve risk.

## Required tasks

1. Derive formulas, parity, limiting cases and units.

2. Compute matched ATM implied vols, report unattainable premiums and invalid strikes, never clip rates.

3. Compare price differences, smile in common normal-vol units and Greeks across strikes.

4. Vary shift, maturity and rates, decompose annuity and forward changes with a simple curve.

5. Validate inversion residuals and finite-difference Greeks, quantify when first-order sigma_N approx F*sigma_B is inaccurate.

## Required exhibits

ATM conversion table; price and common-unit smile plots; domain/failure map; delta and vega comparisons.

## Robustness

Do not compare normal bp vol directly with percentage Black vol. Shift is a modeling choice, not empirical identification. Same premium and annuity required for fair comparison. Quoted convention does not determine dynamics of the underlying yield curve.

## Minimum viable thesis

Three rate regimes including negative, normal versus shifted Black matched ATM, parity and independent price/Greek checks.

## Optional extension

Use optional GSW initial curves for annuity construction; caplet/swaption conventions and joint shift calibration.

## Prerequisites

Fixed income, option pricing, normal distribution, numerical roots and Python.

## Thesis outline

1. Forward measures and rate options;

2. Normal/lognormal formulas;

3. ATM matching;

4. Price and hedge comparisons;

5. Practical conventions.

## Milestones

W1-3: pricing derivations; W4-6: pricers and inversions; W7-9: grids; W10-12: Greeks and curve effects; W13-16: reproducibility and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
