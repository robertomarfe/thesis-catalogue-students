# Data and model setup | A05.01.03

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Daily DTB3 https://fred.stlouisfed.org/series/DTB3 convert discount-basis quote to approximate continuously compounded bill yield using 91-day face discount and actual convention check; GSW daily zero yields https://www.federalreserve.gov/data/nominal-yield-curve.htm at 1,2,5,10 years. Weekly last common trading day; train 1971-1999, validation 2000-2009, test 2010-2025 subject to coverage. CIR use strictly positive contiguous episodes only; report excluded dates and same-sample Vasicek comparison, full-sample Vasicek separately. Fit exact transitions with irregular elapsed year fractions; include GARCH or rolling variance benchmark.

## Inputs
- **GSW — GSW nominal fitted yield curve** (Core). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Link status from v13 inventory: Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.
- **DTB3 — DTB3** (Core). Expected file: `DTB3.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DTB3); [provider page](https://fred.stlouisfed.org/series/DTB3). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Daily discount basis bill yield.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Intersect daily GSW and DTB3 before selecting weekly last common date; retain elapsed ACT/365 years. Form only consecutive calendar-week pairs; for CIR require positive adjacent observations, no bridge across omitted weeks. Estimate OU/CIR on same positive training dates; add rolling variance scaled to actual interval. Report conditional forecast error by short-rate bin and changes in affine yields B(T)/T times innovations, with separate stress OU.

## Acceptance and first meeting
Verify bill conversion and rate support, same weekly intervals and common-positive sample; test exact transition variance against distribution moments. Held-out yield-volatility comparison uses aligned maturities and interval; P estimates do not identify Q loadings.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Use identical dates for comparisons, rate-bin diagnostics and a predeclared mean/variance scoring convention. Distinguish this variance-target experiment from A05.01.01 density forecasting.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
