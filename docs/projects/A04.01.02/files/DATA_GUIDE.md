# Data and model setup | A04.01.02

**Current data gate: conditional.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Philadelphia Fed SPF dispersion measure D2 (Q/Q growth, annualized percentage points) https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/dispersion-forecasts; RGDP mean growth/forecasts https://www.philadelphiafed.org/surveys-and-data/rgdp and release dates. French daily market+RF https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; optional VIXCLS. Sample proposed 1968Q4-2025Q4 after coverage gate, initial 80 quarters; use same survey vintage and horizon T+1. Target next complete calendar quarter after survey, nonoverlapping squared daily log returns. Lagged RV observed through previous completed quarter; forecasts no earlier than actual release.

## Inputs
- **FF3D — US FF3 daily** (Core). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **SPFLEVEL — SPF mean forecast levels** (Core). Expected file: `meanLevel.xlsx`. [Download or provider route](https://www.philadelphiafed.org/-/media/FRBP/Assets/Surveys-And-Data/survey-of-professional-forecasters/historical-data/meanLevel.xlsx?hash=A51C49A6FCF80FE18F2CE81D903F4970&sc_lang=en); [provider page](https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/mean-forecasts). Historical v13 inventory note (unverified in current release): Direct link observed; file not inspected. RGDP level forecasts; same-vintage ratios; preserve documentation.
- **SPFDATES — SPF release dates** (Core). Expected file: `spf-release-dates.txt`. [Download or provider route](https://www.philadelphiafed.org/-/media/frbp/assets/surveys-and-data/survey-of-professional-forecasters/spf-release-dates.txt); [provider page](https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/mean-forecasts). Historical v13 inventory note (unverified in current release): Exact link listed in provider documentation; file not inspected. Verify actual coverage and date conventions; do not guess release days.
- **VIXCLS — VIXCLS** (Optional control). Expected file: `VIXCLS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS); [provider page](https://fred.stlouisfed.org/series/VIXCLS). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Daily closing index, monthly mean only for spread study.
- **USREC — USREC** (Robustness). Expected file: `USREC.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=USREC); [provider page](https://fred.stlouisfed.org/series/USREC). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Monthly recession indicator; retrospective.
- **SPF_D2 — SPF D2 forecast dispersion of Q/Q growth** (Core). Expected file: `Dispersion_2.xlsx`. [Download or provider route](https://www.philadelphiafed.org/-/media/FRBP/Assets/Surveys-And-Data/survey-of-professional-forecasters/historical-data/Dispersion_2.xlsx?hash=E0A0D114F37EC56209ECB512CA07FA84&sc_lang=en); [provider page](https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/dispersion-forecasts). Historical v13 inventory note (unverified in current release): Exact provider-linked workbook observed 2026-11-25; unsupported binary content in web fetch. D2=75th minus 25th percentile of individual annualized Q/Q growth forecasts in percentage points, not volatility of expected growth; use RGDP horizon T+1, check release dates and coverage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use SPF D2 RGDP for q+1 in annualized pp, not D1 or D3; mean forecast from same vintage/horizon ratio of levels. Pre-1992 RGNP not RGDP: document and separate full-history GNP/GDP splice as original design; GDP-only robustness. Actual survey release determines next complete calendar quarter; if delayed outside vintage q stop and resolve. Construct total daily market log returns, sum squares on full independently audited US session calendar (a coverage check only tests the supplied calendar), lag previous completed quarter RV. Compare log OLS with training-only smearing or Gamma log-link; fit D2/EG incremental coefficients on same sample, strict label maturation at origin. 80-quarter initial sample, HAC and joint block inference. Optional VIX control on common authorized shorter sample; USREC ex post.

## Acceptance and first meeting
Actual SPF D2 and mean RGDP same horizon, vintage dates, full FF3D calendar and rights required; initial 80 quarters feasible only after coverage check. No substitution of forecast disagreement by volatility.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** conditional. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **FF3D — US FF3 daily**: F-F_Research_Data_Factors_daily_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed in provider page; bytes not inspected.
- **SPFDATES — SPF release dates**: spf-release-dates.txt. Route: https://www.philadelphiafed.org/-/media/frbp/assets/surveys-and-data/survey-of-professional-forecasters/spf-release-dates.txt. Provider: https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/mean-forecasts. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Exact link listed in provider documentation; file not inspected.
- **SPFLEVEL — SPF mean forecast levels**: meanLevel.xlsx. Route: https://www.philadelphiafed.org/-/media/FRBP/Assets/Surveys-And-Data/survey-of-professional-forecasters/historical-data/meanLevel.xlsx?hash=A51C49A6FCF80FE18F2CE81D903F4970&sc_lang=en. Provider: https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/mean-forecasts. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed; file not inspected.
- **SPF_D2 — SPF D2 forecast dispersion of Q/Q growth**: Dispersion_2.xlsx. Route: https://www.philadelphiafed.org/-/media/FRBP/Assets/Surveys-And-Data/survey-of-professional-forecasters/historical-data/Dispersion_2.xlsx?hash=E0A0D114F37EC56209ECB512CA07FA84&sc_lang=en. Provider: https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/dispersion-forecasts. D2 = interquartile spread of Q/Q growth forecasts in annualized percentage points; excludes CPI and PCE. Actual RGDP tab and horizon unverified. Historical link note, not fresh verification: Exact provider-linked workbook observed 2026-11-25; unsupported binary content in web fetch.

### Acceptance of the local input set

Match D2 and mean RGDP at the same vintage and q+1 horizon. Audit exchange calendar independently; mark a missing daily return as missing quarterly RV. Show an 80-quarter warmup and only matured next-quarter RV; use training-only log smearing, matched QLIKE and log-MSE with paired blocks; GDP-only robustness.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

If RGDP D2 and matching mean horizon cannot be established, defer. A GDP-only expectation study is a distinct question, not a substitute for disagreement.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

Philadelphia Fed SPF dispersion measure D2 (Q/Q growth, annualized percentage points) https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/dispersion-forecasts; RGDP mean growth/forecasts https://www.philadelphiafed.org/surveys-and-data/rgdp and release dates. French daily market+RF https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; optional VIXCLS. Sample proposed 1968Q4-2025Q4 after coverage gate, initial 80 quarters; use same survey vintage and horizon T+1. Target next complete calendar quarter after survey, nonoverlapping squared daily log returns. Lagged RV observed through previous completed quarter; forecasts no earlier than actual release.

## Design-specific acceptance

Match D2 and mean RGDP at the same vintage and q+1 horizon. Audit exchange calendar independently; mark a missing daily return as missing quarterly RV. Show an 80-quarter warmup and only matured next-quarter RV; use training-only log smearing, matched QLIKE and log-MSE with paired blocks; GDP-only robustness.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish observation and release dates, gross and log returns, physical variance and implied variance, yield changes and holding returns, and nominal-real matching on identical dates.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
