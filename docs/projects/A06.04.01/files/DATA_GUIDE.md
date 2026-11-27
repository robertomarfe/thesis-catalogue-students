# Data and model setup | A06.04.01

**Current data gate: conditional.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Use GKK synthetic equity yields https://stefanogiglio.org/ (verify exact archive/maturity labels and rights), GSW nominal zeros https://www.federalreserve.gov/data/nominal-yield-curve.htm, FRED USREC and INDPRO. Month-end matching, proposed 1975-2019 or longest validated common sample, no nearest-date forward matching, percent to decimals and compounding documented. Recession dating is retrospective; for descriptive state dependence use USREC and lagged industrial production growth separately. For predictive extension use release-aware macro data, not final recession labels.

## Inputs
- **GKK — Equity yields synthetic strips** (Core). Expected file: `EqTS_synthetic_strip_yields-JF-2024-03-02.zip`. [Download or provider route](https://drive.google.com/file/d/1eycuEuxPbR5qeOwcbjisjy1B-kVZH9VL/view?usp=sharing); [provider page](https://stefanogiglio.org/). Historical v13 inventory note (unverified in current release): Exact file page observed; click Download. Keep ZIP intact and read codebook; model-implied yields.
- **GSW — GSW nominal fitted yield curve** (Core). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Historical v13 inventory note (unverified in current release): Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.
- **USREC — USREC** (Core). Expected file: `USREC.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=USREC); [provider page](https://fred.stlouisfed.org/series/USREC). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Monthly recession indicator; retrospective.
- **INDPRO — INDPRO** (Core). Expected file: `INDPRO.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=INDPRO); [provider page](https://fred.stlouisfed.org/series/INDPRO). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Monthly seasonally adjusted index.
- **GSW_TIPS — Fitted real TIPS zero yields and inflation compensation** (Optional extension). Expected file: `feds200805.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200805.csv); [provider page](https://www.federalreserve.gov/data/tips-yield-curve-and-inflation-compensation.htm). Historical v13 inventory note (unverified in current release): Direct CSV linked; binary unsupported by web fetch, not validated. 1999 onward per provider; verify valid maturity coverage, units and compounding; revisions documented.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
GKK market and GSW same maturity/year units and exact monthly labels; join USREC and INDPRO without nearest-date matching; use lagged 12-month growth with conservative release lag unless vintage evidence. Fit sE=a+b*sB+c*rec+d*sB*rec; HAC and common calendar-block resample, report recession episodes and unstable subsample results. Distinguish levels vs changes, no contemporaneous recession prediction. Alternatives 5–2/10–5 predefined. Report model-implied GKK curves, no structural macro causality.

## Acceptance and first meeting
CONDITIONAL: GKK archive, actual sample, rights, GSW, USREC, INDPRO all required; artificial interaction regression not empirical evidence.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** conditional. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **GKK — Equity yields synthetic strips**: EqTS_synthetic_strip_yields-JF-2024-03-02.zip. Route: https://drive.google.com/file/d/1eycuEuxPbR5qeOwcbjisjy1B-kVZH9VL/view?usp=sharing. Provider: https://stefanogiglio.org/. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Exact file page observed; click Download.
- **GSW — GSW nominal fitted yield curve**: feds200628.csv. Route: https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv. Provider: https://www.federalreserve.gov/data/nominal-yield-curve.htm. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed; file not inspected.
- **INDPRO — INDPRO**: INDPRO.csv. Route: https://fred.stlouisfed.org/graph/fredgraph.csv?id=INDPRO. Provider: https://fred.stlouisfed.org/series/INDPRO. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct CSV endpoint constructed from exact series ID; not fetched.
- **USREC — USREC**: USREC.csv. Route: https://fred.stlouisfed.org/graph/fredgraph.csv?id=USREC. Provider: https://fred.stlouisfed.org/series/USREC. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct CSV endpoint constructed from exact series ID; not fetched.

### Acceptance of the local input set

Verify exact GKK/GSW grid 2/10y with dates and units, distinguish level regression from change regression, compare interaction coefficient with prespecified alternative maturity pairs and lagged IP growth. Resample joint date blocks, report recession episode counts and leave-one-episode sensitivity; no causal identification or real-time prediction.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

Require common exact maturity/calendar grid, no nearest-date matching. If data fail, defer or redesign as synthetic equity-bond slope comparison, not empirical business-cycle evidence.

## Frozen research design (original catalogue)

Use GKK synthetic equity yields https://stefanogiglio.org/ (verify exact archive/maturity labels and rights), GSW nominal zeros https://www.federalreserve.gov/data/nominal-yield-curve.htm, FRED USREC and INDPRO. Month-end matching, proposed 1975-2019 or longest validated common sample, no nearest-date forward matching, percent to decimals and compounding documented. Recession dating is retrospective; for descriptive state dependence use USREC and lagged industrial production growth separately. For predictive extension use release-aware macro data, not final recession labels.

## Design-specific acceptance

Verify exact GKK/GSW grid 2/10y with dates and units, distinguish level regression from change regression, compare interaction coefficient with prespecified alternative maturity pairs and lagged IP growth. Resample joint date blocks, report recession episode counts and leave-one-episode sensitivity; no causal identification or real-time prediction.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Separate model-implied curves from traded prices, real safe payoffs from ex post real returns, and conditional from unconditional moments.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
