# Data and model setup | A06.03.01

**Current data gate: conditional.** No actual external input bytes are supplied or validated.

## Original input contract and sample
GKK public equity yield archive https://stefanogiglio.org/ (equation 32); inspect the author or publisher replication archive https://onlinelibrary.wiley.com/doi/10.1111/jofi.13394 for exact matched returns; confirm exact portfolio labels, 1/10Y maturities, sample and normalization. GSW nominal yields https://www.federalreserve.gov/data/nominal-yield-curve.htm, French style portfolio returns and FF3 https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Use only verifiably matched GKK and French portfolio definitions or provider's corresponding returns; proposed 1975-2020 common monthly sample, no invented correspondence. Benchmark 10Y monthly yield change in decimal; controls 2Y, market; optional USMPD high-frequency extension separately.

## Inputs
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **GSW — GSW nominal fitted yield curve** (Core). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Historical v13 inventory note (unverified in current release): Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.
- **GKK — Equity yields synthetic strips** (Core conditional). Expected file: `EqTS_synthetic_strip_yields-JF-2024-03-02.zip`. [Download or provider route](https://drive.google.com/file/d/1eycuEuxPbR5qeOwcbjisjy1B-kVZH9VL/view?usp=sharing); [provider page](https://stefanogiglio.org/). Historical v13 inventory note (unverified in current release): Exact file page observed; click Download. Keep ZIP intact and read codebook; model-implied yields.
- **FF25M — US 25 size/BM monthly** (Conditional exact match only; not automatic). Expected file: `25_Portfolios_5x5_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_5x5_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **USMPD — Full USMPD** (Optional event extension). Expected file: `USMPD.xlsx`. [Download or provider route](https://www.frbsf.org/wp-content/uploads/USMPD.xlsx?2026-11-24=); [provider page](https://www.frbsf.org/research-and-insights/data-and-indicators/us-monetary-policy-event-study-database/). Historical v13 inventory note (unverified in current release): Direct link observed; file not inspected. Use full workbook, not chart data; query suffix may rotate.
- **GKK_REPL — Equity Term Structures without Dividend Strips Data replication code** (Core conditional; exact return match gate). Expected file: `jofi13394-sup-0002-ReplicationCode.zip`. [Download or provider route](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1111%2Fjofi.13394&file=jofi13394-sup-0002-ReplicationCode.zip); [provider page](https://onlinelibrary.wiley.com/doi/10.1111/jofi.13394). Historical v13 inventory note (unverified in current release): Publisher supporting-information link observed; fetch returned 403; contents and rights unknown. Inspect package for exact matched P1/P3 portfolio return series; do not assume code includes returns. If unavailable, resolve via authors or only verifiably matched public definitions.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Obtain GKK portfolio-specific yield and corresponding returns; exact return mapping requires provider code/metadata, not names alone. Compare at least four styles, require 1/10Y matched yield grid and actual exact month t-1 slope before return t; 10Y yield change t minus t-1 (decimal), no gaps compressed. Primary portfolio and date fixed effects with centered lagged slope, centered-slope-by-rate-change interaction and relative market loadings. The rate_interactions helper is a secondary pooled benchmark, using already lagged slopes. Do not include common market or rate main effects with date fixed effects. Bootstrap entire months jointly across portfolios with blocks; scale coefficient effects per 100bp. Describe GKK estimates as full-sample generated regressors, not live forecast. Rate beta reflects cash-flow revisions and discounting; compare theoretical duration separately.

## Acceptance and first meeting
CONDITIONAL: exact GKK yield/return mapping (replication archive or provider), >=4 styles, rights, actual matched data and GSW/FF3 required. Do not use FF25M unless exact match established. Artificial interaction recovery only.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** conditional. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **FF3M — US FF3 monthly**: F-F_Research_Data_Factors_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed in provider page; bytes not inspected.
- **GKK — Equity yields synthetic strips**: EqTS_synthetic_strip_yields-JF-2024-03-02.zip. Route: https://drive.google.com/file/d/1eycuEuxPbR5qeOwcbjisjy1B-kVZH9VL/view?usp=sharing. Provider: https://stefanogiglio.org/. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Exact file page observed; click Download.
- **GKK_REPL — Equity Term Structures without Dividend Strips Data replication code**: jofi13394-sup-0002-ReplicationCode.zip. Route: https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1111%2Fjofi.13394&file=jofi13394-sup-0002-ReplicationCode.zip. Provider: https://onlinelibrary.wiley.com/doi/10.1111/jofi.13394. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Publisher supporting-information link observed; fetch returned 403; contents and rights unknown.
- **GSW — GSW nominal fitted yield curve**: feds200628.csv. Route: https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv. Provider: https://www.federalreserve.gov/data/nominal-yield-curve.htm. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed; file not inspected.

### Acceptance of the local input set

Prespecify pooled asset-FE diagnostic separately from primary time-FE specification. In latter omit common dy and market main effects, interact market with portfolio indicators as appropriate, center lagged slopes within date and check rank; include slope main effect, joint month block inference and exact t-1 availability. Require >=4 exactly mapped styles and scale effects per 100bp. Do not silently treat helper output as the primary panel test.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

Defer unless at least four exact GKK yield/return crosswalks can be documented; narrower subset requires new approval. Keep theoretical duration illustration only as feasibility, not empirical result.

## Frozen research design (original catalogue)

GKK public equity yield archive https://stefanogiglio.org/ (equation 32); inspect the author or publisher replication archive https://onlinelibrary.wiley.com/doi/10.1111/jofi.13394 for exact matched returns; confirm exact portfolio labels, 1/10Y maturities, sample and normalization. GSW nominal yields https://www.federalreserve.gov/data/nominal-yield-curve.htm, French style portfolio returns and FF3 https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Use only verifiably matched GKK and French portfolio definitions or provider's corresponding returns; proposed 1975-2020 common monthly sample, no invented correspondence. Benchmark 10Y monthly yield change in decimal; controls 2Y, market; optional USMPD high-frequency extension separately.

## Design-specific acceptance

Prespecify pooled asset-FE diagnostic separately from primary time-FE specification. In latter omit common dy and market main effects, interact market with portfolio indicators as appropriate, center lagged slopes within date and check rank; include slope main effect, joint month block inference and exact t-1 availability. Require >=4 exactly mapped styles and scale effects per 100bp. Do not silently treat helper output as the primary panel test.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Separate model-implied curves from traded prices, real safe payoffs from ex post real returns, and conditional from unconditional moments.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
