# Data and model setup | A09.04.02

**Current data gate: blocked.** No actual external input bytes are supplied or validated.

No provider observations are bundled. **Permission gate first:** [CBBTCUSD](https://fred.stlouisfed.org/series/CBBTCUSD) says prior written Coinbase permission is required for reproduction. Do not download, copy, upload or distribute for this thesis before confirming authorized use and permitted output with the provider/institution. A public page is not a license. VIXCLS is copyrighted Cboe material reprinted by FRED with permission; verify your own permitted use. French data public access does not establish unrestricted redistribution. If an alternate Bitcoin provider is proposed, obtain explicit supervisor approval for coverage, timestamp, definition, rights and comparison design.

| Input | Official source / exact local filename | Role |
|---|---|---|
| BTC USD daily, 7-day | [CBBTCUSD](https://fred.stlouisfed.org/series/CBBTCUSD); after authorization, Download CSV; standard endpoint `https://fred.stlouisfed.org/graph/fredgraph.csv?id=CBBTCUSD` (not fetched). `CBBTCUSD.csv` | Core conditional |
| FF3 monthly | [French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html), [CSV ZIP](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip), `F-F_Research_Data_Factors_CSV.zip` | Core |
| VIX daily close | [VIXCLS](https://fred.stlouisfed.org/series/VIXCLS), standard CSV endpoint `https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS` (not fetched), `VIXCLS.csv` | Stress analysis and calendar proxy subject to audit |
| FF5 and momentum | Library monthly FF5 CSV ZIP and monthly Momentum CSV ZIP; candidate files `F-F_Research_Data_5_Factors_2x3_CSV.zip` and `F-F_Momentum_Factor_CSV.zip`; verify provider metadata and rights | Robustness |

## Local construction
- Record provider permission evidence privately, retrieval date, filename, SHA-256, schema, timestamp, units, coverage. FRED CSV requires ISO dates and named series, one row/date; '.'/blank missing; no carry-forward. Inspect actual provider bytes locally. French main monthly block only, percent/100; preserve CIZ/FIZ vintage, don't append histories silently. Verify endpoint date before every ratio. Need December 2014 through December 2025 endpoints for January 2015 through December 2025 returns.
- Baseline calendar month-end BTC USD price ratio minus 1, not log difference. Alternative last US trading day requires independently audited calendar for each month, including previous endpoint. VIX close dates can be a cross-check but not proof of exchange calendar completeness. Document asynchronously timed equity and crypto endpoints. Missing exact prices require sample redesign or authorized replacement; no interpolation. Use lagged VIX level in index points; no division by 100 unless changing the explicitly declared scaling. Join by monthly PeriodIndex, one row per month; no repeated annual table. Compare RF if combining FF5/Momentum.
- Independently verify exact baseline coverage, prior endpoint, continuous dates, lagged stress and independently audited exchange calendar. Record actual timezone and written permission separately; no raw observations may be redistributed without authorization. If VIX is missing, the stress gate remains pending.

## Acceptance
Baseline full common calendar coverage or approved contiguous sample redesign before regressions. At least 72 months baseline and 36 per approved split, positive BTC levels, finite factors/RF, exact endpoints; one timing robustness with verified calendar. Check dates, missing daily counts and permission. Treat unusually large but valid returns as data audit items, not automatic exclusions. Return the local report to supervisor only if permitted. Optional robustness files require individual validation; no promise of full coverage or free reuse.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** blocked. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **CBBTCUSD — Coinbase Bitcoin USD daily seven-day price**: CBBTCUSD.csv. Route: https://fred.stlouisfed.org/graph/fredgraph.csv?id=CBBTCUSD. Provider: https://fred.stlouisfed.org/series/CBBTCUSD. Inherited route note describes seven-day observations at 5 PM PST and a written-permission requirement; independently verify timestamp and terms before use. Historical link note, not fresh verification: Series metadata observed; standard CSV candidate not fetched; rights conditional.
- **FF3M — US FF3 monthly**: F-F_Research_Data_Factors_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed in provider page; bytes not inspected.
- **VIXCLS — VIXCLS**: VIXCLS.csv. Route: https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS. Provider: https://fred.stlouisfed.org/series/VIXCLS. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct CSV endpoint constructed from exact series ID; not fetched.

### Acceptance of the local input set

Retain the input acceptance gate and previously specified sample thresholds. Written permission or authorized supervisor-approved alternate; validate prior endpoint, timezone and last US trading-day robustness; lag stress, matched dates and contiguous HAC. No alternative without approval.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

Obtain a permitted alternative Bitcoin source only after checking exchange, timestamp, weekend and currency definitions; otherwise defer. No fabricated crypto returns or silent substitution.

## Design-specific acceptance

Blocked until permission, actual coverage and timestamp are validated. Retain the baseline 72-month and split 36-month thresholds from the input protocol; require exact prior endpoints and documented timing robustness. No unapproved substitute or raw redistribution.

## Timing, accounting and units

Fix currency quote orientation, base currency, return units, settlement dates, funding convention, measure and annualization. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For simulations distinguish expiry from delivery and quote rate from payoff currency.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
