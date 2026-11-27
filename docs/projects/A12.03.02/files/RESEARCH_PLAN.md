# Research plan | A12.03.02

## Study design and independent work

Check monotone market clearing, nonnegative holdings and exact inventory accounting; reproduce purchase-weighted reference update and no-reference/symmetric/asymmetric controls with identical shocks. Add explicit matched-turnover calibration on development paths only, report unmatched paths and paired simulation intervals; use strictly lagged predictive variables. No claim on actual investor data.

## Prespecified implementation

Positive log-random-walk F, N=100, initial shares/reference dispersion. Signed investor trades max[a_i(F-P)/P_prev-s_i h_i,-h_i]; liquidity-provider order mm(F-P)/P_prev, strictly monotone clearing in P; cap investor selling by holdings, investor cash unconstrained and provider may short (explicit stylized baseline). Update purchase reference using weighted costs for positive buys, unchanged for sales, reset at zero. Propensity s_i=base+strength*(I(P_prev>A_i)-cross-sectional mean I) matches average propensity, not realized turnover; no-reference control match realized turnover only using independent calibration paths. Reject nonpositive price, record all failures. Common 200 paths, 500 dates/burn 100; news response, gap, return continuation/reversal, lagged overhang; no empirical mechanism claim.

## Required tasks

1. Write exact order, clearing, holdings and purchase-reference updates; test one period by hand and verify aggregate shares.

2. Freeze symmetric and asymmetric parameter scenarios, check positive prices and turnover; report infeasible paths rather than deleting them.

3. Compare price-fundamental gaps, signed news responses, autocorrelation and momentum/reversal regressions with lagged aggregate capital-gain overhang.

4. Vary strength of disposition, liquidity elasticity and fundamental volatility independently using matched seeds.

5. Add a no-reference-price control with matched average turnover to distinguish generic trading pressure from reference dependence.

## Required exhibits

Documented simulation rules, accounting and clearing tests, price-gap trajectories, return autocorrelation and predictability distributions, turnover and sensitivity plots.

## Robustness

No empirical causal inference or claim that stylized demand is structurally estimated. Avoid interpreting price pressure as risk premium without an SDF. Keep fundamental shocks identical across treatments and define reference updates for new/zero holdings. Report sensitivity to market-maker and positivity rules.

## Minimum viable thesis

Audited market clearing and share accounting, symmetric/asymmetric/no-reference controls, replicated paths, news response and predictability metrics with uncertainty.

## Optional extension

Add heterogeneous beliefs or endogenous participation as a separate mechanism; compare price pressure and return predictability holding disposition parameters fixed.

## Prerequisites

Behavioral finance, probability, numerical root finding, simulation and basic regression.

## Thesis outline

1. Behavioral trading and the disposition effect;

2. Reference-dependent market design;

3. Simulation and validation;

4. Return dynamics and controlled comparisons;

5. Interpretation and limitations.

## Milestones

W1-3: literature and model rules; W4-6: clearing and reference accounting; W7-9: matched simulation; W10-12: counterfactual and sensitivity; W13-16: interpretation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
