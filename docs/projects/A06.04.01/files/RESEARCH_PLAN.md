# Research plan | A06.04.01

## Study design and independent work

Verify exact GKK/GSW grid 2/10y with dates and units, distinguish level regression from change regression, compare interaction coefficient with prespecified alternative maturity pairs and lagged IP growth. Resample joint date blocks, report recession episode counts and leave-one-episode sensitivity; no causal identification or real-time prediction.

## Prespecified implementation

GKK market and GSW same maturity/year units and exact monthly labels; join USREC and INDPRO without nearest-date matching; use lagged 12-month growth with conservative release lag unless vintage evidence. Fit sE=a+b*sB+c*rec+d*sB*rec; HAC and common calendar-block resample, report recession episodes and unstable subsample results. Distinguish levels vs changes, no contemporaneous recession prediction. Alternatives 5–2/10–5 predefined. Report model-implied GKK curves, no structural macro causality.

## Required tasks

1. Audit GKK definitions, GSW maturity units and common sample; compute slopes at identical maturities.

2. Plot levels, slopes and episode means; compare distributions in expansions and recessions.

3. Fit sE=a+b sB+c rec+d sB*rec+e using HAC and calendar-block bootstrap; report small number of recession clusters.

4. Replace rec by lagged 12-month industrial production growth and compare changes versus levels.

5. Test robustness to 5Y-2Y/10Y-5Y, crisis exclusion and subsamples without selecting the strongest result.

## Required exhibits

Matched-date yield and slope panels, business-cycle summary table, conditional correlations/regressions with intervals, maturity sensitivity.

## Robustness

GKK estimates are generated quantities; no inference of observed strip quotes, expected risk premium or causal macro shocks. Few recessions limit inference; distinguish retrospective macro descriptions from real-time predictors. Nominal yield spread does not isolate inflation risk.

## Minimum viable thesis

One common GKK/GSW grid, two slopes, recession/expansion summaries and one conditional regression with time-series uncertainty; permission and data match mandatory.

## Optional extension

Compare equity slopes with real Treasury slopes on shorter TIPS common support, only with compatible units and definitions.

## Prerequisites

Asset pricing, term structure, regression and macro data.

## Thesis outline

1. Equity and bond valuation;

2. Maturity slopes and cycle;

3. Data and matching;

4. Conditional evidence;

5. Interpretation.

## Milestones

W1-3: equity yield definitions and access; W4-6: match and validation; W7-9: descriptive/regression analysis; W10-12: robustness; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
