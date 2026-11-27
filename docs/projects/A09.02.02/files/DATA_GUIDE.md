# Data and model setup | A09.02.02

**Current data gate: conditional.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Use Della Corte/Riddiough Currency Factors gross and net G10 carry series (provider files already in inventory; https://www.currencyfactors.com/), French FF3 monthly from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html, VIXCLS and NFCI from https://fred.stlouisfed.org/. Target 1990-2025 common sample, freeze carry methodology and units; if source ends earlier use actual overlap. Predefine risk-off as contemporaneous market bottom decile or VIX high state using training-only threshold, and predictive lagged VIX at prior month end. Net data only as documented transaction-cost adjustment.

## Inputs
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **CARRY_GROSS — Carry excess returns before transaction costs (G10 and other universes)** (Core conditional). Expected file: `Original XLSX (filename to verify)`. [Download or provider route](https://docs.google.com/spreadsheets/d/1mLb2pmU1QKFo2K2YU6xsUX41OGLTe33b/export?format=xlsx); [provider page](https://www.currencyfactors.com/currency-data). Historical v13 inventory note (unverified in current release): Exact provider Carry download link observed; redirected binary not accessible in web tool. Select Carry under before t-costs; provider describes academic use. Check sheet, units, definition and redistribution terms.
- **CARRY_NET — Carry excess returns after transaction costs (G10 and other universes)** (Optional gross/net sensitivity). Expected file: `Original XLSX (filename to verify)`. [Download or provider route](https://docs.google.com/spreadsheets/d/1BLHEQgcAaWISdkJtkpfkZmEWfuB9Eb5h/export?format=xlsx); [provider page](https://www.currencyfactors.com/currency-data). Historical v13 inventory note (unverified in current release): Exact provider Carry download link observed; redirected binary not accessible in web tool. Select Carry under after t-costs; published spread-cost assumption is not actual execution.
- **VIXCLS — VIXCLS** (Core). Expected file: `VIXCLS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS); [provider page](https://fred.stlouisfed.org/series/VIXCLS). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Daily closing index, monthly mean only for spread study.
- **NFCI — NFCI** (Core). Expected file: `NFCI.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=NFCI); [provider page](https://fred.stlouisfed.org/series/NFCI). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Weekly; release lag and vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
G10 gross H-L factor as published; optional net cost proxy. Align FF3M market, last valid VIX and publication-aware NFCI; no implicit compounding of zero-cost spreads. Freeze market bottom-decile and VIX high threshold on training data; 120-month initial window, expanding mean versus lagged predictors, no final sample threshold. Use HAC and paired date blocks; contemporaneous stress beta descriptive.

## Acceptance and first meeting
CONDITIONAL: carry gross file with G10 factor, VIX and NFCI permitted and available, actual date/lag/return units checked; no genuine real-time claim from revised NFCI.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** conditional. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **CARRY_GROSS — Carry excess returns before transaction costs (G10 and other universes)**: Original XLSX (filename to verify). Route: https://docs.google.com/spreadsheets/d/1mLb2pmU1QKFo2K2YU6xsUX41OGLTe33b/export?format=xlsx. Provider: https://www.currencyfactors.com/currency-data. Academic-use permission stated, cite paper; gross and net distinguished. Current page reports Jan 1976 to Sep 2026; actual workbook version/content and redistribution not checked. Historical link note, not fresh verification: Exact provider Carry download link observed; redirected binary not accessible in web tool.
- **FF3M — US FF3 monthly**: F-F_Research_Data_Factors_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed in provider page; bytes not inspected.
- **NFCI — NFCI**: NFCI.csv. Route: https://fred.stlouisfed.org/graph/fredgraph.csv?id=NFCI. Provider: https://fred.stlouisfed.org/series/NFCI. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct CSV endpoint constructed from exact series ID; not fetched.
- **VIXCLS — VIXCLS**: VIXCLS.csv. Route: https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS. Provider: https://fred.stlouisfed.org/series/VIXCLS. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct CSV endpoint constructed from exact series ID; not fetched.

### Acceptance of the local input set

Verify published gross H-L maturity dates, scale and units; prefit stress thresholds; compare matched expanding mean vs lagged VIX/NFCI with target maturation, same origins and block inference; keep zero-cost payoffs distinct from funded wealth.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

If G10 gross carry or aligned risk states unavailable, defer; net carry may be robustness only unless scope is expressly changed.

## Design-specific acceptance

Audit the G10 gross definition and dates before use. Report state counts, training thresholds, information lags and common forecast origins. Do not substitute other carry factors or claim causal effects.

## Timing, accounting and units

Fix currency quote orientation, base currency, return units, settlement dates, funding convention, measure and annualization. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For simulations distinguish expiry from delivery and quote rate from payoff currency.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
