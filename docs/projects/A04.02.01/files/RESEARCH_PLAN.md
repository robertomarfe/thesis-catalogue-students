# Research plan | A04.02.01

## Study design and independent work

Hand-check one quarterly-average CPI realization and one forecast error from the prior vintage; compound market, portfolio and bill legs separately. Estimate nominal and real exposures on matched quarters and jointly bootstrap quarters, re-estimating both stages. Report common sample, rank, regime split and revised-CPI caveat.

## Prespecified implementation

Use previous-quarter SPF mean CPI forecast for target q, verify actual release and annualized quarterly-average SA CPI definition. Convert annualized published mean pp to quarterly simple rate via (1+f/100)^(1/4)-1; nonlinear transform of mean is not mean of individually converted forecasts. Compute realization from three monthly SA CPI levels in each adjacent quarter, forecast error on same convention. Compound French market, RF and portfolio returns separately; compute nominal excess and real excess after deflation, total real hedge returns separately. Estimate market-controlled inflation betas with HAC; jointly resample calendar quarters and re-estimate both beta and cross-sectional slopes (do not bootstrap assets independently). 1985-2025 target with actual coverage, industry baseline and characteristic portfolios robustness; fixed pre/post-2000 split. AR proxy only with approval and disclosed distinct design.

## Required tasks

1. Verify SPF target-quarter convention, annualization, CPI realization and release date; plot forecast errors.

2. Compound returns and RF separately to quarters, compute nominal and real total/excess returns.

3. Estimate inflation betas and market-controlled betas with HAC intervals; rank sectors and compare nominal versus real total-return hedge exposure.

4. Relate mean excess returns to market and inflation betas across portfolios; bootstrap quarters jointly with beta re-estimation.

5. Compare pre/post-2000 and inflation regimes; repeat using a lagged AR forecast and alternative CPI vintage if accessible.

## Required exhibits

Matched forecast/realization panel, innovation figure, portfolio beta and hedge tables, cross-sectional scatterplot and joint intervals, regime diagnostics.

## Robustness

Match CPI quarterly-average versus end-quarter and annualized-rate convention exactly; do not replace forecast errors with raw inflation. Revised realized CPI is retrospective; actual release dates define expectation timing. Portfolio exposures are not causal or a proof of priced inflation risk. Avoid independent-asset standard errors for correlated portfolio returns.

## Minimum viable thesis

One coherent quarterly CPI innovation measure, industry portfolio exposures with market control, nominal/real distinction, joint inference and regime robustness.

## Optional extension

Compare expected inflation and surprise effects separately or use PCE forecasts with matched realized PCE definition.

## Prerequisites

Asset pricing, macroeconomic data, regression, time-series inference and Python.

## Thesis outline

1. Inflation risk and real returns;

2. Expectations and factor exposures;

3. SPF/CPI and portfolio panel;

4. Heterogeneous exposures and pricing diagnostics;

5. Robustness and interpretation.

## Milestones

W1-3: inflation and risk pricing theory; W4-6: survey/CPI timing and quarterly returns; W7-9: exposure estimates; W10-12: cross-section and regimes; W13-16: inference and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
