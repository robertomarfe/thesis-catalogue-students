# Research plan | A06.02.02

## Study design and independent work

Require positive-dividend portfolio IDs and validated exact high/low style crosswalk with common 1/5/10y dates; report both individual curves and paired differences/slope, joint calendar-block intervals and sensitivity across regimes. Keep matched weighting, units and vintage. If exact pair not verified, stop rather than substitute FF labels.

## Prespecified implementation

GKK 102 portfolios: choose exact high/low value characteristic labels from codebook, validate sign and weighting, do not equate anomaly long/short with asset-level dividend yield or French labels. Use exact paired same date/maturity 1/5/10 core, optional 2/15 and other styles only verified. Report difference high minus low and slope difference, block sample common across assets and maturities; GDP/recession labels descriptive only. No cash-flow versus discount-rate interpretation without decomposition inputs.

## Required tasks

1. Verify portfolio IDs, maturity units, yield normalization, missing codes and time coverage; reproduce an aggregate curve statistic.

2. Compute paired mean curves, standard deviations and short/long slopes; plot value-growth differences over time.

3. Estimate unconditional differences using time-block bootstrap jointly across portfolios and maturities.

4. Compare slopes in NBER recession versus expansion or predetermined lagged macro states; quantify limited recession count.

5. Explore whether differences come from cash-flow growth or discounting only if matching decomposition inputs exist; otherwise label interpretation as unresolved.

## Required exhibits

Portfolio crosswalk; mean term structures; slope time series and paired uncertainty; regime comparison; documentation of model dependence.

## Robustness

GKK curves are estimated from a shared model, not independent observed strip quotes. Common sample, same units and vintage are essential. Bootstrap treats curves as given and omits estimation uncertainty of the underlying GKK model; acknowledge. Do not equate equity yields with expected returns or pure duration.

## Minimum viable thesis

One verified value-growth pair, common 1/5/10y grid, paired curve/slope comparison, inference and clear model-implied caveat; conditional on archive. Distinct from aggregate A06.02.01 and theoretical duration A06.03.02.

## Optional extension

Compare multiple anomaly pairs with multiple-testing controls; add model-provided cash-flow/return decomposition only if available.

## Prerequisites

Asset pricing, term structures, time-series statistics and Python.

## Thesis outline

1. Dividend strip pricing;

2. Synthetic equity yields;

3. Dataset and crosswalk;

4. Style differences and regimes;

5. Interpretation.

## Milestones

W1-3: literature/archive gate; W4-6: crosswalk and baseline; W7-9: paired term structures; W10-12: regimes/robustness; W13-16: writing and replication.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
