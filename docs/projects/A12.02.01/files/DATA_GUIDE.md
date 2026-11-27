# Data and model setup | A12.02.01

**Current data gate: conditional.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Yale ICF US Stock Market Confidence Indices https://yale-icf.github.io/ShillerUSConfidence/ (Download Free Index Data; raw monthly since July 2001, earlier semiannual; select One-Year Confidence for both populations, standard errors if supplied). Do not splice legacy six-month moving average with raw monthly. Goyal workbook dp and French monthly market excess returns from https://sites.google.com/view/agoyal145/ and https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Target 2001-2025; lag survey at least one full month, audit publication dates; if absent describe conservative-lag pseudo-OOS not real-time. Yale terms require written permission for reproduction/distribution and permit publication of summaries only; do not upload raw file without authorization.

## Inputs
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **GOYAL2025 — Combined GW/GWZ full-sample workbook through 2025** (Core). Expected file: `Data2025.xlsx`. [Download or provider route](https://docs.google.com/spreadsheets/d/17mw_IpaiLFDrGnrPRQ2o1ugV5nJsZuD1/edit?ouid=113571510202500088860&rtpof=true&sd=true&usp=sharing); [provider page](https://sites.google.com/view/agoyal145/). Historical v13 inventory note (unverified in current release): Exact file page observed; download using Google Sheets File > Download > Excel. Freeze version, include definitions and verify timing; full-sample revised data.
- **YALE_CONF — US stock market confidence indices free data (raw monthly)** (Core conditional; rights gate). Expected file: `Original Free Index Data export (filename to verify)`. [Download or provider route](https://yale-icf.github.io/ShillerUSConfidence/); [provider page](https://yale-icf.github.io/ShillerUSConfidence/). Historical v13 inventory note (unverified in current release): Provider Download Free Index Data button confirmed; direct file URL not exposed. Select One-Year Confidence for individuals and institutions; monthly from July 2001, prior sparse surveys; old site six-month rolling mean. Terms prohibit reproduction/distribution without written permission; only summaries may be published. Do not upload raw data without authorization.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use raw One-Year Confidence for individuals and institutions, separate populations; monthly since July 2001, not legacy six-month moving average. Confirm actual publication date or lag at least full month and label pseudo-OOS; sample likely short, predeclare initial training (e.g. 120 months if supported), avoid post-hoc splits. Goyal dp preceding month and French market excess; confidence index percentage points not returns, standardize training only; historical mean, dp, confidence and joint, same origins with lagged predictors; report HAC and paired block uncertainty. No data reproduction/distribution without written Yale permission; publish only authorized summaries.

## Acceptance and first meeting
CONDITIONAL: obtain authorized Yale raw monthly series, exact population and release coverage, rights for local research and summaries; no raw distribution. Defer or supervisor-approved alternative if absent.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** conditional. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **FF3M — US FF3 monthly**: F-F_Research_Data_Factors_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed in provider page; bytes not inspected.
- **GOYAL2025 — Combined GW/GWZ full-sample workbook through 2025**: Data2025.xlsx. Route: https://docs.google.com/spreadsheets/d/17mw_IpaiLFDrGnrPRQ2o1ugV5nJsZuD1/edit?ouid=113571510202500088860&rtpof=true&sd=true&usp=sharing. Provider: https://sites.google.com/view/agoyal145/. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Exact file page observed; download using Google Sheets File > Download > Excel.
- **YALE_CONF — US stock market confidence indices free data (raw monthly)**: Original Free Index Data export (filename to verify). Route: https://yale-icf.github.io/ShillerUSConfidence/. Provider: https://yale-icf.github.io/ShillerUSConfidence/. Raw monthly rather than legacy six-month smoothed data; publication/distribution requires written permission; summaries only, not raw series. Contact Yale ICF before dissemination. Historical link note, not fresh verification: Provider Download Free Index Data button confirmed; direct file URL not exposed.

### Acceptance of the local input set

Obtain permission and exact monthly series/population/horizon; verify calendar and dates, predeclare lag and extra-lag sensitivity. One authorized series suffices for MVT; compare dp baseline and past-only historical mean on same origins, with paired blocks; defer if access or sample insufficient.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

Request written permission as applicable; if only summaries permitted, keep raw files local with authorization. Alternate sentiment proxy requires new approval; do not splice smoothed legacy series.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

Yale ICF US Stock Market Confidence Indices https://yale-icf.github.io/ShillerUSConfidence/ (Download Free Index Data; raw monthly since July 2001, earlier semiannual; select One-Year Confidence for both populations, standard errors if supplied). Do not splice legacy six-month moving average with raw monthly. Goyal workbook dp and French monthly market excess returns from https://sites.google.com/view/agoyal145/ and https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Target 2001-2025; lag survey at least one full month, audit publication dates; if absent describe conservative-lag pseudo-OOS not real-time. Yale terms require written permission for reproduction/distribution and permit publication of summaries only; do not upload raw file without authorization.

## Design-specific acceptance

Obtain permission and exact monthly series/population/horizon; verify calendar and dates, predeclare lag and extra-lag sensitivity. One authorized series suffices for MVT; compare dp baseline and past-only historical mean on same origins, with paired blocks; defer if access or sample insufficient.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish funded wealth from zero-investment spreads, gross from net performance, allocation-time moments from realized risk, and actual turnover from hypothetical trading costs.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
