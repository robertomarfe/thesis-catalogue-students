# Data and model setup | A06.02.01

**Current data gate: conditional.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Download GKK end-of-month aggregate equity yields n=1,...,15 via https://stefanogiglio.org/ (Data & Code, Equity Term Structures without Dividend Strips Data). Read the codebook and Eq. (32); inspect first/last dates, maturity columns, units and file version (do not assume all study dates equal release dates). Merge month-end GSW SVENY01-15 from https://www.federalreserve.gov/data/nominal-yield-curve.htm and FRED USREC https://fred.stlouisfed.org/series/USREC for ex post recession labels; use full common historical sample. Core data class B plus public controls; downloading the actual GKK file is an assignment gate.

## Inputs
- **USREC — USREC** (Core / planned robustness). Expected file: `USREC.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=USREC); [provider page](https://fred.stlouisfed.org/series/USREC). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Monthly recession indicator; retrospective.
- **GSW — GSW nominal fitted yield curve** (Core / planned robustness). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Historical v13 inventory note (unverified in current release): Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.
- **GKK — Equity yields synthetic strips** (Core / planned robustness). Expected file: `EqTS_synthetic_strip_yields-JF-2024-03-02.zip`. [Download or provider route](https://drive.google.com/file/d/1eycuEuxPbR5qeOwcbjisjy1B-kVZH9VL/view?usp=sharing); [provider page](https://stefanogiglio.org/). Historical v13 inventory note (unverified in current release): Exact file page observed; click Download. Keep ZIP intact and read codebook; model-implied yields.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
GKK Eq.32 equity yields in continuously compounded annual units after verifying archive scale and nominal convention. Require complete maturity grid 1–15, exact month-end convention and GSW SVENY01–15 common last valid date; no maturity interpolation unless explicit robustness. Use paired_curves and curve_summary; forward equity yield e-y_b is not forward rate between maturities. Descriptive PCA common dates, HAC/block intervals, USREC retrospective episode means and counts. If actual archive inaccessible, defer or supervisor-approved distinct synthetic exercise.

## Acceptance and first meeting
CONDITIONAL: official archive identified, browser sign-in gate; bytes, units, dates, rights, GSW and USREC sample open. Artificial exact alignment only.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** conditional. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **GKK — Equity yields synthetic strips**: EqTS_synthetic_strip_yields-JF-2024-03-02.zip. Route: https://drive.google.com/file/d/1eycuEuxPbR5qeOwcbjisjy1B-kVZH9VL/view?usp=sharing. Provider: https://stefanogiglio.org/. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Exact file page observed; click Download.
- **GSW — GSW nominal fitted yield curve**: feds200628.csv. Route: https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv. Provider: https://www.federalreserve.gov/data/nominal-yield-curve.htm. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed; file not inspected.
- **USREC — USREC**: USREC.csv. Route: https://fred.stlouisfed.org/graph/fredgraph.csv?id=USREC. Provider: https://fred.stlouisfed.org/series/USREC. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct CSV endpoint constructed from exact series ID; not fetched.

### Acceptance of the local input set

Verify archive/version and Eq.32/33, complete 1-15 annual maturity grid, positive dividend normalization and decimals, exact common month-end GSW SVENY, not par yields. Report common sample, model-implied caveat, slope and fixed curvature definition, centered PCA with sign convention and recession episode counts. Inference conditional on estimated curves; no independent validation of the underlying GKK estimator.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

Defer if aggregate strip-yield grid cannot be verified; retitled synthetic model-implied term structure is a different thesis, not measured GKK evidence.

## Frozen research design (original catalogue)

Download GKK end-of-month aggregate equity yields n=1,...,15 via https://stefanogiglio.org/ (Data & Code, Equity Term Structures without Dividend Strips Data). Read the codebook and Eq. (32); inspect first/last dates, maturity columns, units and file version (do not assume all study dates equal release dates). Merge month-end GSW SVENY01-15 from https://www.federalreserve.gov/data/nominal-yield-curve.htm and FRED USREC https://fred.stlouisfed.org/series/USREC for ex post recession labels; use full common historical sample. Core data class B plus public controls; downloading the actual GKK file is an assignment gate.

## Design-specific acceptance

Verify archive/version and Eq.32/33, complete 1-15 annual maturity grid, positive dividend normalization and decimals, exact common month-end GSW SVENY, not par yields. Report common sample, model-implied caveat, slope and fixed curvature definition, centered PCA with sign convention and recession episode counts. Inference conditional on estimated curves; no independent validation of the underlying GKK estimator.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Separate model-implied curves from traded prices, real safe payoffs from ex post real returns, and conditional from unconditional moments.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
