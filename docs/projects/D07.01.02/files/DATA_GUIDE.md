# Data and model setup | D07.01.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Fed GSW fitted nominal Treasury curves https://www.federalreserve.gov/data/nominal-yield-curve.htm, proposed 2000-2025 daily sample. Use continuously compounded zero yields or calculate from published parameters; avoid unsupported extrapolation. On each historical date independently construct synthetic 5y/10y annual coupon par bonds and par payer swaps with annual payment dates. Freeze original cash-flow schedules and coupon rates; apply next day's curve as an instantaneous shock at fixed maturities, not a realized holding-period return. Compare 5y single swap hedge with 2y/10y key-rate hedge.

## Inputs
- **GSW — GSW nominal fitted yield curve** (Core / planned robustness). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Link status from v13 inventory: Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Construct par coupon bonds and swaps at each origin; freeze cash flows/coupons. Compute signed parallel DV01 and key-node sensitivities by central reprice; solve target plus hedge exposure=0. Compare 5Y payer vs 2Y/10Y hedge with equal target notional and report gross notional. Reprice all fixed schedules under next observed curve, only consecutive verified sessions.

## Acceptance and first meeting
GSW rights/schema/calendar pending. Check payer sign against bond, par identities and conditioning; distinguish instantaneous fixed-maturity shock from aging returns.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Report initial zero PV for swaps, matched shocks and risk reduction net of exposure sign mistakes. Distinct from D07.04.02: swap DV01/key-rate hedging rather than PCA zero-bond spanning.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
