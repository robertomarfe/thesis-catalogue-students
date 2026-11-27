# Data and model setup | D10.03.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Use FRED DEXUSEU daily USD/EUR and OECD monthly three-month interbank rate proxies IR3TIB01USM156N and IR3TIB01EZM156N, percent p.a. Source https://fred.stlouisfed.org/series/DEXUSEU ; https://fred.stlouisfed.org/series/IR3TIB01USM156N ; https://fred.stlouisfed.org/series/IR3TIB01EZM156N . Baseline 1999-2025 common dates, month-end last valid spot with latest published prior-month rate averages (use two-month lag if release timing is unknown) as deliberately stale proxies (same-month averages descriptive sensitivity only); tau=0.25, simple accrual. Verify series definition changes and EA19 end coverage. Compute 3m points in pips (0.0001 USD/EUR). Compare with alternative rate-proxy pair only if definitions and overlap verified.

## Inputs
- **DEXUSEU — DEXUSEU** (Core / planned robustness). Expected file: `DEXUSEU.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DEXUSEU); [provider page](https://fred.stlouisfed.org/series/DEXUSEU). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. USD per EUR.
- **IR3TIB01USM156N — IR3TIB01USM156N** (Core / planned robustness). Expected file: `IR3TIB01USM156N.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=IR3TIB01USM156N); [provider page](https://fred.stlouisfed.org/series/IR3TIB01USM156N). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Monthly annual percentage rate proxy.
- **IR3TIB01EZM156N — IR3TIB01EZM156N** (Core / planned robustness). Expected file: `IR3TIB01EZM156N.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=IR3TIB01EZM156N); [provider page](https://fred.stlouisfed.org/series/IR3TIB01EZM156N). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. EA19 monthly annual rate proxy; verify coverage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
DEXUSEU USD/EUR month-end fixing and monthly US/EA19 OECD rate proxies percent p.a.; exact prior-month rate, default two-month lag if release unknown. Convert percent once; simple tau=.25, positive accrual; points (F-S)/.0001. Invert quote and swap domestic/foreign rates; legacy value with fixed contractual K and remaining tenor. Hypothetical basis shift in domestic accrual, not empirical basis.

## Acceptance and first meeting
Verify actual overlap, units, rate definitions, dates and permission; no actual forward quotes. Synthetic parity, inversion and MTM identities passed; any missing-source redesign requires approval.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Verify quote orientation, rate units, positive accrual, zero initial PV and reciprocal identity. Record availability and exact overlap. No observed basis or executable trade claim.

## Timing, accounting and units

Fix currency quote orientation, base currency, return units, settlement dates, funding convention, measure and annualization. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For simulations distinguish expiry from delivery and quote rate from payoff currency.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
