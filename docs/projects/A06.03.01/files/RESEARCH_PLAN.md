# Research plan | A06.03.01

## Study design and independent work

Prespecify pooled asset-FE diagnostic separately from primary time-FE specification. In latter omit common dy and market main effects, interact market with portfolio indicators as appropriate, center lagged slopes within date and check rank; include slope main effect, joint month block inference and exact t-1 availability. Require >=4 exactly mapped styles and scale effects per 100bp. Do not silently treat helper output as the primary panel test.

## Prespecified implementation

Obtain GKK portfolio-specific yield and corresponding returns; exact return mapping requires provider code/metadata, not names alone. Compare at least four styles, require 1/10Y matched yield grid and actual exact month t-1 slope before return t; 10Y yield change t minus t-1 (decimal), no gaps compressed. Primary portfolio and date fixed effects with centered lagged slope, centered-slope-by-rate-change interaction and relative market loadings. The rate_interactions helper is a secondary pooled benchmark, using already lagged slopes. Do not include common market or rate main effects with date fixed effects. Bootstrap entire months jointly across portfolios with blocks; scale coefficient effects per 100bp. Describe GKK estimates as full-sample generated regressors, not live forecast. Rate beta reflects cash-flow revisions and discounting; compare theoretical duration separately.

## Required tasks

1. Validate GKK metadata and exact portfolio/return matching; document exclusions.

2. Plot slopes and synthetic PV-duration illustration holding cashflows fixed.

3. Estimate portfolio return-rate sensitivities, market-adjusted and rolling, with lagged slopes and common dates.

4. Estimate interacted panel and group contrasts; common month block bootstrap across all portfolios, report economic effect per 100 bp rate change.

5. Vary maturity pairs, real versus nominal changes where available and subperiods; disclose model-implied slopes generated on full sample. Use portfolio and date fixed effects as the primary specification. Include the within-date centered lagged equity-yield slope, its interaction with next-month yield changes, and portfolio-relative market loadings. Common market and rate main effects are absorbed by date effects. Check rank and relative portfolio-by-rate controls; resample complete months jointly. Pooled portfolio fixed effects are only a secondary benchmark.

## Required exhibits

Match table and definition audit; yield slopes by style; sensitivity and interaction table; joint intervals; robustness. Primary two-way fixed-effect interaction estimate, relative market loadings, rank check and joint month-block intervals.

## Robustness

Yield changes contain growth and risk-premium news; not pure exogenous discount shocks. GKK estimated curves are not observed dividend strip quotes or real-time predictors. No exact duration inference from slope alone. No assignment until matching confirmed; narrow to matched subset rather than fabricate returns.

## Minimum viable thesis

At least four matched style portfolios, 1/10Y slope, common sample return-rate interactions and joint inference plus theoretical duration example.

## Optional extension

Use monetary-policy event surprises with matched frequency and information-effect caveats, subject to separate return data gate.

## Prerequisites

Asset pricing, fixed income, panel econometrics, Python.

## Thesis outline

1. Equity strips and duration;

2. Identification of rate exposure;

3. Data and matching;

4. Panel evidence;

5. Interpretation.

## Milestones

W1-3: GKK definitions and gate; W4-6: exact merge and theory; W7-9: estimation; W10-12: joint inference; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
