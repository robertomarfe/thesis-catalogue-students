# Data and model setup | A09.02.01

**Current data gate: conditional.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Bank of England database end-month GBP/USD spot XUMLUSS and one-month forward XUMLDS1 via https://www.bankofengland.co.uk/boeapps/database/ ; request 1990-2021, actual common period to verify, forward discontinued after June 2021. Verify outright USD/GBP rates and identical fixing conventions, approximate next month-end settlement; exclude missing months. Currency Factors academic data https://www.currencyfactors.com/currency-data select named Carry gross and net returns files, G10 panel; restrict common sample for comparison, actual portfolio returns from provider. If files unavailable, use DEXUSEU and matched three-month OECD rate proxies with nonoverlapping quarters and explicit synthetic CIP label, subject to supervisor approval.

## Inputs
- **DEXUSEU — DEXUSEU** (Conditional synthetic CIP fallback only, supervisor approval). Expected file: `DEXUSEU.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DEXUSEU); [provider page](https://fred.stlouisfed.org/series/DEXUSEU). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. USD per EUR.
- **IR3TIB01USM156N — IR3TIB01USM156N** (Conditional synthetic CIP fallback only, supervisor approval). Expected file: `IR3TIB01USM156N.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=IR3TIB01USM156N); [provider page](https://fred.stlouisfed.org/series/IR3TIB01USM156N). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Monthly annual percentage rate proxy.
- **IR3TIB01EZM156N — IR3TIB01EZM156N** (Conditional synthetic CIP fallback only, supervisor approval). Expected file: `IR3TIB01EZM156N.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=IR3TIB01EZM156N); [provider page](https://fred.stlouisfed.org/series/IR3TIB01EZM156N). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. EA19 monthly annual rate proxy; verify coverage.
- **BOE_GBPUSD — End-month GBP/USD spot and one-month forward (XUMLUSS, XUMLDS1)** (Core conditional). Expected file: `CSV export (retain original filename)`. [Download or provider route](https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp?csv.x=yes&Datefrom=01/Jan/1990&Dateto=31/Jul/2021&SeriesCodes=XUMLUSS,XUMLDS1&CSVF=TT&UsingCodes=Y&VPD=N); [provider page](https://www.bankofengland.co.uk/boeapps/database/). Historical v13 inventory note (unverified in current release): CSV endpoint constructed from provider documented API and confirmed series IDs; bytes not inspected. Inherited endpoint hypothesis: XUMLDS1 through June 2021; confirm locally; spot through July for final outcome. Verify units, coverage and settlement. Select both IDs in database and export CSV if endpoint fails.
- **CARRY_GROSS — Carry excess returns before transaction costs (G10 and other universes)** (Core conditional). Expected file: `Original XLSX (filename to verify)`. [Download or provider route](https://docs.google.com/spreadsheets/d/1mLb2pmU1QKFo2K2YU6xsUX41OGLTe33b/export?format=xlsx); [provider page](https://www.currencyfactors.com/currency-data). Historical v13 inventory note (unverified in current release): Exact provider Carry download link observed; redirected binary not accessible in web tool. Select Carry under before t-costs; provider describes academic use. Check sheet, units, definition and redistribution terms.
- **CARRY_NET — Carry excess returns after transaction costs (G10 and other universes)** (Optional sensitivity). Expected file: `Original XLSX (filename to verify)`. [Download or provider route](https://docs.google.com/spreadsheets/d/1BLHEQgcAaWISdkJtkpfkZmEWfuB9Eb5h/export?format=xlsx); [provider page](https://www.currencyfactors.com/currency-data). Historical v13 inventory note (unverified in current release): Exact provider Carry download link observed; redirected binary not accessible in web tool. Select Carry under after t-costs; published spread-cost assumption is not actual execution.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
BoE XUMLUSS/XUMLDS1: verify USD per GBP and fixing; forward origins end Jun 2021, July spot required for final label. Exact calendar month maturity; missing outcomes stay missing and use contiguous segments or calendar-aware inference. OLS HAC on a common contiguous sample, slope 1 null; use 60/40 chronological split with matured training outcomes. Carry file G10 highest-minus-lowest gross return distinct from log bilateral proxy. No substitution of synthetic CIP without redesign approval.

## Acceptance and first meeting
CONDITIONAL: verify both BoE outright series, settlement approximation, data rights and G10 gross carry workbook; optional net. No observed forward price or portfolio file validated.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** conditional. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **BOE_GBPUSD — End-month GBP/USD spot and one-month forward (XUMLUSS, XUMLDS1)**: CSV export (retain original filename). Route: https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp?csv.x=yes&Datefrom=01/Jan/1990&Dateto=31/Jul/2021&SeriesCodes=XUMLUSS,XUMLDS1&CSVF=TT&UsingCodes=Y&VPD=N. Provider: https://www.bankofengland.co.uk/boeapps/database/. XUMLDS1 ends June 2021; no extrapolated forward history or CIP substitute. Historical link note, not fresh verification: CSV endpoint constructed from provider documented API and confirmed series IDs; bytes not inspected.
- **CARRY_GROSS — Carry excess returns before transaction costs (G10 and other universes)**: Original XLSX (filename to verify). Route: https://docs.google.com/spreadsheets/d/1mLb2pmU1QKFo2K2YU6xsUX41OGLTe33b/export?format=xlsx. Provider: https://www.currencyfactors.com/currency-data. Academic-use permission stated, cite paper; gross and net distinguished. Current page reports Jan 1976 to Sep 2026; actual workbook version/content and redistribution not checked. Historical link note, not fresh verification: Exact provider Carry download link observed; redirected binary not accessible in web tool.

### Acceptance of the local input set

Verify both outright quotes USD/GBP and fixing, July 2021 spot for final label; report exact settlement approximation and missing months. Test slope 1 with dependence-aware inference, keep G10 factor separate; no synthetic forward substitute without explicit redesign.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

Freeze observed forward sample ending June 2021, no post-2021 splice; if insufficient, shorten under approval or redesign as carry-only question without claiming UIP test.

## Design-specific acceptance

Before estimation verify outright versus points, quote orientation, fixing and outcome dates; audit rights and actual coverage. Do not splice observed and synthetic forwards or infer G10 carry from a bilateral regression.

## Timing, accounting and units

Fix currency quote orientation, base currency, return units, settlement dates, funding convention, measure and annualization. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For simulations distinguish expiry from delivery and quote rate from payoff currency.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
