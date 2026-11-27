# Research plan | A12.01.02

## Study design and independent work

Validate BAB workbook version, long-short orientation/units and common FF/Mom panel; separate contemporaneous versus lagged standardized states with past-only scaling. Joint date blocks, fixed crisis windows and optional ANFCI/NFCICREDIT; report no causality and vintage caveat. No OOS claim from contemporaneous controls.

## Prespecified implementation

Use AQR monthly US BAB zero-cost long/short, not a total-return index; no RF subtraction or assumption of gross/net treatment until workbook inspected. NFCI weekly covers Friday, normally published Wednesday 8:30 ET, holidays Thursday; use actual release if supplied and additional one-week buffer for lagged predictor; revised data label. Aggregate month-end last available release, distinguish change during month (association) versus lagged level/change (predictive). Standardize using training scale; factor regression and HAC, fixed 2008-09/2020 windows and ANFCI/NFCICREDIT sensitivity, OOS historical mean optional if enough data. No causal identification of borrowing constraints.

## Required tasks

1. Inspect BAB metadata, NFCI direction and timestamps; construct monthly level/change and lagged predictors, verify no RF subtraction from published long-short BAB.

2. Estimate unconditional mean and factor alpha; report contemporaneous stress regressions with HAC inference and economic effects per one-SD tightening.

3. Run separate predictive regressions using only lagged/release-safe proxies; compare with historical mean OOS if sample sufficient.

4. Compare high/low stress regime returns using thresholds fixed in training period, and test adjusted NFCI/credit subindex sensitivity and crisis influence.

## Required exhibits

BAB and financial-conditions plots, conditional return and regression table, contemporaneous versus predictive results, crisis and proxy sensitivity, timestamp and vintage log. Include factor exposure and uncertainty rather than equating BAB return with funding cost.

## Robustness

NFCI combines financial markets including equities, so simultaneity and shared shocks are material. Adjusted index does not isolate funding constraints; predictive results on latest revised data remain pseudo-real-time. Report lagged availability assumptions, HAC/block bootstrap, multiple proxy results and subsample sensitivity. No executable leveraged strategy claim.

## Minimum viable thesis

Verified US BAB and NFCI monthly alignment, unconditional factor analysis, contemporaneous and lagged regressions with uncertainty, crisis and alternate proxy sensitivity, explicit noncausal interpretation. OOS prediction optional if sample too short.

## Optional extension

Compare international BAB factors with local stress proxies only after checking currencies, units and comparable measures; a causal funding-shock design requires separate identification.

## Prerequisites

CAPM, multifactor regressions, funding liquidity economics, time-series HAC and Python.

## Thesis outline

1. Leverage constraints and low-beta anomaly;

2. BAB construction and predictions;

3. Public factors and funding proxies;

4. Conditional returns and predictive tests;

5. Endogeneity and interpretation.

## Milestones

W1-3: model theory and source gate; W4-6: align BAB and stress measures; W7-10: estimate factor/stress regressions; W11-13: timing, regimes and proxy robustness; W14-16: write and reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
