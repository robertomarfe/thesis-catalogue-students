# Research plan | D09.01.01

## Study design and independent work

Verify asset-value conservation, the upper bound on debt and probability intervals. Report simulation uncertainty in rare-default cases and physical-drift sensitivity separately from risk-neutral pricing. Keep all other parameters fixed in each comparative static.

## Required tasks

1. Derive prices, both default probabilities and equity elasticity; implement analytical and MC checks.

2. Map leverage-volatility grids for s, PD_P, PD_Q and sigma_E by maturity; quantify economic sensitivities in bp and percentage points.

3. Hold PD_P approximately constant across different asset drifts/volatilities using a prespecified grid or root solve; compare resulting spreads and equity volatility.

4. Discuss why terminal-only default, zero coupons and GBM limit the applicability of very short spreads and realistic credit term structures.

## Required exhibits

Credit spread and default-probability heatmaps; term structure plots by leverage; equity volatility table; analytical versus simulation check with confidence intervals; matched-PD comparison. Interpret deviations between risk-neutral and physical measures.

## Robustness

Check equity plus debt equals firm assets and debt price <= risk-free promised payoff, default probability in [0,1], monotonicities for fixed remaining parameters. Vary physical drift separately from pricing inputs; it should change PD_P but not Q debt price in the specified model. Do not calibrate historical PDs from spreads without assumptions on risk premia.

## Minimum viable thesis

Correct structural formulas and independent verification, comparative statics on leverage and volatility at several maturities, distinction between P and Q, and quantitative implications. No empirical validation claim is necessary.

## Optional extension

Compare first-passage default or introduce a small illustrative set of public firm filings, only after checking debt maturity, market capitalization and data consistency. Treat calibration of V and sigma_V from equity as optional and model-dependent.

## Prerequisites

BSM option pricing, probability measures, comparative statics, Python. Elementary corporate finance and credit spread interpretation.

## Thesis outline

1. Structural credit risk and capital structure;

2. Merton model and probability measures;

3. Numerical design and verification;

4. Comparative statics and credit risk;

5. Model limitations and conclusion.

## Milestones

W1-3: derive contingent-claim valuation; W4-6: implement analytic functions and MC validation; W7-10: grid, matched-PD and maturity analyses; W11-13: limiting cases and robustness; W14-16: write and reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
