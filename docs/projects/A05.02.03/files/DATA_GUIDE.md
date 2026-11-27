# Data and model setup | A05.02.03

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
GSW daily fitted nominal zeros https://www.federalreserve.gov/data/nominal-yield-curve.htm, monthly last available date, maturities 1,2,3,5,7,10y; target 1985-2025. Use lags 1,3,12 and slope/curvature; initial training 1985-2004, rolling-origin tuning 2005-2014, final 2015-2025 with expanding estimation; 1,3,12 month direct horizons. Shift dates if missing but lock before test. Optional ECB curves only after common-period gate.

## Inputs
- **GSW — GSW nominal fitted yield curve** (Core). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Link status from v13 inventory: Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.
- **ECB_AAA_1_10 — AAA euro area fitted spot curve 1-10 years daily** (Optional external evaluation). Expected file: `CSV export (retain original filename)`. [Download or provider route](https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_1Y+SR_2Y+SR_3Y+SR_4Y+SR_5Y+SR_6Y+SR_7Y+SR_8Y+SR_9Y+SR_10Y?startPeriod=2004-09-06&endPeriod=2025-12-31&format=csvdata); [provider page](https://data.ecb.europa.eu/data/datasets/YC). Link status from v13 inventory: Constructed CSV endpoint from documented API and series-key pattern; 1/2/5/10Y metadata checked, full query untested. Continuous-compounded percent p.a.; AAA sample, Svensson fit, changing composition. Check all ten keys and date coverage; if failure download named series individually.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Construct month-dated predictors from available current and exact lag 1/3/12 yields, slope/curvature; target direct h-month future yields, no row shifts across missing months. Fit historical no-change, DNS/AR and ridge or shallow trees; select hyperparameters on 2005–2014 rolling origins only with matured labels. Freeze design for 2015–2025. Estimate standardization in each training window only.

## Acceptance and first meeting
Actual GSW sample, features and publication assumptions open. Verify target maturity dates and no pre-test tuning on holdout. If missing months, use exact calendar lookup, not deletion then shift.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Implement a strong DNS baseline independently before ML. Lock temporal validation and data features, log all tuning choices and missing outcomes, and never select the final model using the final test loss.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
