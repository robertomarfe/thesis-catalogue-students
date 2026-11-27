# Data and model setup | A05.02.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
US nominal GSW fitted zero yields https://www.federalreserve.gov/data/nominal-yield-curve.htm; euro-area AAA fitted Svensson spot rates https://data.ecb.europa.eu/data/datasets/YC, series YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_1Y,...,SR_10Y. Continuous nominal zeros in percent p.a., convert to bp. Common 1-10 year annual grid; monthly last common trading observation, 2004-09 to 2025-12 target. For changes use adjacent months only. Separate PCA per region; train 2004-2014, test 2015-2025, rolling 60-month windows for stability.

## Inputs
- **GSW — GSW nominal fitted yield curve** (Core). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Link status from v13 inventory: Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.
- **ECB_AAA_1_10 — AAA euro area fitted spot curve 1-10 years daily** (Core). Expected file: `CSV export (retain original filename)`. [Download or provider route](https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_1Y+SR_2Y+SR_3Y+SR_4Y+SR_5Y+SR_6Y+SR_7Y+SR_8Y+SR_9Y+SR_10Y?startPeriod=2004-09-06&endPeriod=2025-12-31&format=csvdata); [provider page](https://data.ecb.europa.eu/data/datasets/YC). Link status from v13 inventory: Constructed CSV endpoint from documented API and series-key pattern; 1/2/5/10Y metadata checked, full query untested. Continuous-compounded percent p.a.; AAA sample, Svensson fit, changing composition. Check all ten keys and date coverage; if failure download named series individually.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Join daily panels on exact shared valid observation dates before month-end selection, 1–10Y. Compute adjacent-month differences without bridging missing months. Estimate PCA separately by region on levels and changes; hold training centering/loadings fixed for test. For rolling 60-month fit compare subspace principal angles/projectors (sign and rotation invariant). Report maturity errors in bp and note AAA changing issuer composition.

## Acceptance and first meeting
Verify ECB series key/rating/continuous compounding for every maturity and GSW sample. No substitution of all-rated or par yields. Actual common sample open.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Separate reconstruction from forecasting. Near tied eigenvalues, use subspace comparisons rather than interpreting a particular eigenvector as an economic structural shock.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
