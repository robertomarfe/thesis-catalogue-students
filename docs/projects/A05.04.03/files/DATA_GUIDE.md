# Data and model setup | A05.04.03

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
GSW nominal Treasury curve, ECB AAA fitted spot curve https://data.ecb.europa.eu/data/datasets/YC, FRED INDPRO and Eurostat euro-area industrial production volume index (monthly seasonally adjusted, documented fixed area definition) https://ec.europa.eu/eurostat/databrowser/view/sts_inpr_m/default/table?lang=en. ECB daily starts Sep 2004; proposed 2005-2025 common month-end observations on last common trading day; exact keys and quote types checked. Align local activity series by reference month for descriptive analysis; lag for predictive extension with release dates. Do not mix all-rated and AAA curves or par yields. Normalize per market only for PCA loadings, retain bp for risk comparisons.

## Inputs
- **GSW — GSW nominal fitted yield curve** (Core). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Link status from v13 inventory: Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.
- **INDPRO — INDPRO** (Core). Expected file: `INDPRO.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=INDPRO); [provider page](https://fred.stlouisfed.org/series/INDPRO). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Monthly seasonally adjusted index.
- **ECB_AAA_1_10 — AAA euro area fitted spot curve 1-10 years daily** (Core). Expected file: `CSV export (retain original filename)`. [Download or provider route](https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_1Y+SR_2Y+SR_3Y+SR_4Y+SR_5Y+SR_6Y+SR_7Y+SR_8Y+SR_9Y+SR_10Y?startPeriod=2004-09-06&endPeriod=2025-12-31&format=csvdata); [provider page](https://data.ecb.europa.eu/data/datasets/YC). Link status from v13 inventory: Constructed CSV endpoint from documented API and series-key pattern; 1/2/5/10Y metadata checked, full query untested. Continuous-compounded percent p.a.; AAA sample, Svensson fit, changing composition. Check all ten keys and date coverage; if failure download named series individually.
- **EUROSTAT_IP — Monthly industrial production, fixed euro area** (Core). Expected file: `sts_inpr_m filtered CSV/TSV (retain original name)`. [Download or provider route](https://ec.europa.eu/eurostat/databrowser/view/sts_inpr_m/default/table?lang=en); [provider page](https://ec.europa.eu/eurostat/databrowser/view/sts_inpr_m/default/table?lang=en). Link status from v13 inventory: Dataset code and dimensions observed; filtered export not tested. Choose M, production volume, total industry excluding construction, seasonally/calendar adjusted index, fixed EA composition, 2005-2025; verify available keys/flags and revisions.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Join US and euro AAA daily curves on exact common dates; choose last common day each month, 1/2/5/10Y. Use level y10, slope y10-y2, curvature 2y5-y2-y10; compute adjacent changes. Filter Eurostat sts_inpr_m production volume, seasonally/calendar adjusted, fixed geography (e.g. EA20 as documented), total industry excluding construction, one index base; FRED INDPRO. Align reference month for descriptive co-movement; use release date for predictive extension, not future revisions.

## Acceptance and first meeting
Verify ECB changing composition and Eurostat fixed-area selection; actual coverage and rights pending; do not treat descriptive regression as causal or live strategy.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Unlike A05.02.02, the primary target is economic conditioning of co-movement, not eigenspace stability. Report bin counts, uncertainty and any stale-date exclusions.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
