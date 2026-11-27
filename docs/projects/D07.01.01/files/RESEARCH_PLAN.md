# Research plan | D07.01.01

## Study design and independent work

Verify node reproduction, discount positivity, zero PV at par and bump convergence. Separate interpolation and short-end extrapolation; synthetic fallback requires an explicit approved redesign.

## Required tasks

1. Parse GSW CSV metadata, zero vs par columns, missing dates and units; construct discount factors and forwards on the payment grid.

2. Compute par rates under both interpolation methods; verify receive-fixed PV=0 at par and annual-coupon cases agree across interpolation at observed nodes.

3. Compute signed PV change for parallel +1 bp and localized key-rate bumps with fixed contractual coupon; compare actual changes and first-order approximation for larger shocks.

4. Analyze across curve regimes; report differences in bp and dollars, stress ±100 bp and steepening; relate exposures to coupon annuity and maturity.

## Required exhibits

Curve and forward plots for selected dates; swap rate/DV01 table and time series of interpolation differences; key-rate exposure chart; unit/zero-PV tests. Report exact discounting conventions, and treat all prices as hypothetical examples rather than market quotes.

## Robustness

Check nonpositive discount factors and implausibly oscillating forwards; do not impose positive forwards merely as no-arbitrage under negative-rate regimes. Compare short-end extrapolation, payment frequencies and bump shape; ensure key-rate and parallel bumps are consistently defined. Government curves are not OIS, and floating projection is an explicit single-curve simplification.

## Minimum viable thesis

A downloaded verified zero curve, two interpolation schemes, correct par identity, at least three swap maturities and curve regimes, plus DV01 sensitivity and economic interpretation. Fallback: transparent synthetic curves if the dataset cannot be obtained, with amended empirical claim.

## Optional extension

Add a separate stylized projection curve and explain basis risk, or compare ECB AAA government zero curves without inferring actual USD/EUR swap market spreads.

## Prerequisites

Fixed income, discount factors, calculus and interpolation, Python pandas/SciPy. No actual swap dealer quotes needed.

## Thesis outline

1. Fixed/floating contracts;

2. Curve construction and pricing;

3. Data and interpolation protocol;

4. Pricing and sensitivity results;

5. Modern multi-curve limitations.

## Milestones

W1-3: derive par rate and risk measures, acquire data; W4-6: parse zero yields and validate synthetic flat curves; W7-10: build panel of swap values and key-rate sensitivities; W11-13: stress tests and short-end conventions; W14-16: interpret and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
