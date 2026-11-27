# Data and model setup | D07.01.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Use Fed GSW nominal zero yields SVENY01,...,SVENY10 (annual maturities, continuously compounded, percent; divide by 100). Source https://www.federalreserve.gov/data/nominal-yield-curve.htm ; ECB zero curves optional https://data.ecb.europa.eu/methodology/yield-curves. Baseline month-end dates 2000-2025 subject to coverage; sample six curves spanning steep/flat/inverted states using a rule fixed before results. Hypothetical annual and semiannual fixed payments with alpha=1 or 0.5, maturity 2,5,10 years, notional USD 1m. For t<1 use flat y(1) extrapolation as explicit approximation, test alternate short-end anchor only as sensitivity.

## Inputs
- **GSW — GSW nominal fitted yield curve** (Core / planned robustness). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Link status from v13 inventory: Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use GSW 1–10Y zero yields, compare linear zero and log-discount interpolation at annual and semiannual schedules; both reproduce nodes and use flat first zero yield below year 1. Choose six curves by ex ante slope ranking/thresholds. Price par swap and central signed PV changes for parallel/key-rate +/-1bp; fixed USD 1m. No OIS, collateral or executable swap quote claim.

## Acceptance and first meeting
GSW actual sample open; synthetic fallback only with approved amended empirical claim. Check par PV=0 for each schedule and positive discount factors. Negative forwards not automatically arbitrage with negative-rate environment.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Verify node reproduction, discount positivity, zero PV at par and bump convergence. Separate interpolation and short-end extrapolation; synthetic fallback requires an explicit approved redesign.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
