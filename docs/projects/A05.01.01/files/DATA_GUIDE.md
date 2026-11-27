# Data and model setup | A05.01.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Use monthly last valid daily 3-month Treasury bill discount quote DTB3 https://fred.stlouisfed.org/series/DTB3; transform d in decimal to approximate continuous yield -log(1-d*91/360)/(91/365), fixed 91-day proxy explicitly labeled. Proposed 1960-2007 positive-rate baseline; 1960-1994 train, 1995-2007 test. Use monthly time step 1/12 and verify missing months. 2008-2025 stress sample: if zero/negative rates appear, report CIR support limitation; do not silently floor rates. All models share same observed proxy and training sample.

## Inputs
- **DTB3 — DTB3** (Core / planned robustness). Expected file: `DTB3.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DTB3); [provider page](https://fred.stlouisfed.org/series/DTB3). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Daily discount basis bill yield.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Convert observed DTB3 percent to decimal before bill_yield; use last valid monthly observation and exact adjacent-month pairs, no forward fill. Estimate P OU and CIR by exact likelihood on the same positive baseline, check optimizer boundary and multiple starts, freeze parameters for test. Report average log score, PIT histogram and conditional mean/variance. In the stress period exclude no negative rates silently; CIR score unavailable on unsupported observations. Show illustrative Q curves only with separately declared Q parameters.

## Acceptance and first meeting
Verify the original 91-day approximation and actual local DTB3 history/rights. CIR strictly positive sample; report support failures and sensitivity to 90/92 days. Check transition densities and finite likelihood; actual fits pending.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Compare held-out log scores, PIT calibration and parameter uncertainty on identical positive observations. Record optimizer failures and missing months. Distinct from A05.01.03: primary target is the whole conditional density, not conditional variance alone.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
