# Data and model setup | A06.02.02

**Current data gate: conditional.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Giglio-Kelly-Kozak public model-implied curves from https://stefanogiglio.org/ and article https://doi.org/10.1111/jofi.13394; 102 characteristic-sorted portfolios, monthly or provided frequency, original model estimates through 2020. Select value/growth high/low, then size and profitability if labels verified. Use common years and maturities 1,2,5,10,15 if available; optional USREC, GSW nominal yields only after checking units/price convention. Gate archive contents, mapping and rights.

## Inputs
- **USREC — USREC** (Regime analysis). Expected file: `USREC.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=USREC); [provider page](https://fred.stlouisfed.org/series/USREC). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Monthly recession indicator; retrospective.
- **GKK — Equity yields synthetic strips** (Core conditional). Expected file: `EqTS_synthetic_strip_yields-JF-2024-03-02.zip`. [Download or provider route](https://drive.google.com/file/d/1eycuEuxPbR5qeOwcbjisjy1B-kVZH9VL/view?usp=sharing); [provider page](https://stefanogiglio.org/). Historical v13 inventory note (unverified in current release): Exact file page observed; click Download. Keep ZIP intact and read codebook; model-implied yields.
- **GSW — GSW nominal fitted yield curve** (Optional illustration). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Historical v13 inventory note (unverified in current release): Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
GKK 102 portfolios: choose exact high/low value characteristic labels from codebook, validate sign and weighting, do not equate anomaly long/short with asset-level dividend yield or French labels. Use exact paired same date/maturity 1/5/10 core, optional 2/15 and other styles only verified. Report difference high minus low and slope difference, block sample common across assets and maturities; GDP/recession labels descriptive only. No cash-flow versus discount-rate interpretation without decomposition inputs.

## Acceptance and first meeting
CONDITIONAL: GKK archive/rights/labels and exact style pair required. Synthetic paired curve difference only; no claim actual value-growth ranking.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** conditional. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **GKK — Equity yields synthetic strips**: EqTS_synthetic_strip_yields-JF-2024-03-02.zip. Route: https://drive.google.com/file/d/1eycuEuxPbR5qeOwcbjisjy1B-kVZH9VL/view?usp=sharing. Provider: https://stefanogiglio.org/. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Exact file page observed; click Download.

### Acceptance of the local input set

Require positive-dividend portfolio IDs and validated exact high/low style crosswalk with common 1/5/10y dates; report both individual curves and paired differences/slope, joint calendar-block intervals and sensitivity across regimes. Keep matched weighting, units and vintage. If exact pair not verified, stop rather than substitute FF labels.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

If exact value-growth style pair not verified, stop; alternate pair or synthetic duration exercise requires approval. Do not infer labels from similar French portfolios.

## Frozen research design (original catalogue)

Giglio-Kelly-Kozak public model-implied curves from https://stefanogiglio.org/ and article https://doi.org/10.1111/jofi.13394; 102 characteristic-sorted portfolios, monthly or provided frequency, original model estimates through 2020. Select value/growth high/low, then size and profitability if labels verified. Use common years and maturities 1,2,5,10,15 if available; optional USREC, GSW nominal yields only after checking units/price convention. Gate archive contents, mapping and rights.

## Design-specific acceptance

Require positive-dividend portfolio IDs and validated exact high/low style crosswalk with common 1/5/10y dates; report both individual curves and paired differences/slope, joint calendar-block intervals and sensitivity across regimes. Keep matched weighting, units and vintage. If exact pair not verified, stop rather than substitute FF labels.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Separate model-implied curves from traded prices, real safe payoffs from ex post real returns, and conditional from unconditional moments.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
