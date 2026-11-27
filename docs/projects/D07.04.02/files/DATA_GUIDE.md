# Data and model setup | D07.04.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
GSW nominal Treasury zero yields SVENY01-10 and SVENY15,20 where available: https://www.federalreserve.gov/data/nominal-yield-curve.htm. Month-end observations 1990-2025 target; use 1,2,3,5,7,10 years common across baseline. Target a fixed 7/10-year zero portfolio of equal market values, hedged with 2-year alone or 2- and 5-year zeros. Train PCA in rolling 120-month windows; hedge shocks from 2005 onward with identical timestamps. Instantaneous repricing at fixed maturities, not holding-period returns. Scale to $1m initial target value; report hedge notional limits as sensitivity.

## Inputs
- **GSW — GSW nominal fitted yield curve** (Core). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Link status from v13 inventory: Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use common monthly 1,2,3,5,7,10Y GSW changes, rolling 120 calendar months before each shock. Price 7/10Y zero portfolio at $1m market value, hedge with 2Y alone or 2/5Y. Compute factor exposure via yield-key sensitivity dotted with frozen loadings, solve signed quantities; compare gross notional, condition numbers and exact fixed-maturity shock repricing. Use same shock dates; no aging-return claim.

## Acceptance and first meeting
Actual GSW common sample, chronology and rights open. Verify artificial two-factor exposures exactly neutralized when full rank, report ill-conditioning and notional caps rather than silently clipping.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Do not treat physical PCA loadings as risk-neutral parameters. Unlike D07.01.02, compare statistical factor spanning with zero-bond hedges rather than single-curve swap DV01.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
