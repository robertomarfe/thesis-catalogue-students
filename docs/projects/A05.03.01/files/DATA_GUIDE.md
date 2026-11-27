# Data and model setup | A05.03.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Federal Reserve GSW nominal zero yields https://www.federalreserve.gov/data/nominal-yield-curve.htm; daily estimates sampled last available trading day each month, maturities 1-5 years; verify percent/continuous compounding and no extrapolation flags. Proposed 1972-2025; initial 20 years, expanding estimates with only matured 12-month outcomes used. Monthly overlapping baseline with HAC bandwidth at least 11, annual nonoverlap robustness.

## Inputs
- **GSW — GSW nominal fitted yield curve** (Core). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Link status from v13 inventory: Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use GSW 1–5Y monthly common zero yields; construct synthetic log excess returns of 2–5Y zeros over 12 months, aging remaining maturity. Fit historical mean, slope and common forward factor (reuse forward_factor) using only matured outcomes. Compare expanding forecasts and annual nonoverlap robustness, use HAC with >=11 lags for monthly overlaps.

## Acceptance and first meeting
Actual GSW coverage/revision gate open. Verify constant flat curve produces zero log excess returns and unavailable labels remain missing. No executable return claim.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Focus on predictive gains of forward information rather than the common-factor restriction in A05.03.02. Report overlap and latest-vintage pseudo-OOS limitations explicitly.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
