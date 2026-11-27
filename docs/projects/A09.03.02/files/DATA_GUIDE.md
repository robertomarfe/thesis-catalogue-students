# Data and model setup | A09.03.02

**Current data gate: conditional.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Original Koijen-Moskowitz-Pedersen-Vrugt strategy returns from https://koijen.net/uploads/3/4/4/7/34470013/strategy_returns.xlsx; optional updated international/commodity file through July 2021 https://koijen.net/uploads/3/4/4/7/34470013/strategy_returns_-_global.xlsx. Provider https://www.koijen.net/research.html. Target native monthly common sample, verify exact dates, return units, sleeves and leverage convention. USREC, VIXCLS or NFCI as stress proxies; optional AQR century factor dataset only if carry sleeves documented.

## Inputs
- **NFCI — NFCI** (Robustness). Expected file: `NFCI.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=NFCI); [provider page](https://fred.stlouisfed.org/series/NFCI). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Weekly; release lag and vintage.
- **USREC — USREC** (Regime analysis). Expected file: `USREC.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=USREC); [provider page](https://fred.stlouisfed.org/series/USREC). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Monthly recession indicator; retrospective.
- **VIXCLS — VIXCLS** (Optional regime analysis). Expected file: `VIXCLS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS); [provider page](https://fred.stlouisfed.org/series/VIXCLS). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Daily closing index, monthly mean only for spread study.
- **KMPV_CARRY — Carry original strategy returns** (Core). Expected file: `strategy_returns.xlsx`. [Download or provider route](https://koijen.net/uploads/3/4/4/7/34470013/strategy_returns.xlsx); [provider page](https://www.koijen.net/research.html). Historical v13 inventory note (unverified in current release): Exact author-linked workbook; web click reports unsupported ZIP content type; bytes unvalidated. Select original paper return workbook, confirm at least three asset-class sleeves, units and common sample, leverage and terms. Do not assume raw quotes.
- **KMPV_CARRY_UPDATE — Updated international and commodity carry factors through July 2021** (Optional extension). Expected file: `strategy_returns_-_global.xlsx`. [Download or provider route](https://koijen.net/uploads/3/4/4/7/34470013/strategy_returns_-_global.xlsx); [provider page](https://www.koijen.net/research.html). Historical v13 inventory note (unverified in current release): Exact author-linked workbook; web click reports unsupported ZIP content type; bytes unvalidated. Optional update; confirm actual coverage and construction before combining with original.
- **AQR_CENTURY — How Do Factor Premia Vary Over Time? A Century of Evidence, Factor Data Monthly** (Optional extension). Expected file: `Original workbook (filename to verify)`. [Download or provider route](https://www.aqr.com/Insights/Datasets/Century-of-Factor-Premia-Monthly); [provider page](https://www.aqr.com/Insights/Datasets/Century-of-Factor-Premia-Monthly). Historical v13 inventory note (unverified in current release): Provider dataset page verified; binary URL unresolved. Optional independent evidence; check whether carry sleeves are available separately and confirm methodology and rights.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use original KMPV workbook, at least three distinct sleeves; inspect leverage, unit and frequency. Preserve sample vintage; optional 2021 update separate, no unverified splice. Compare equal-weight and lagged inverse-vol (60 months, shrink weights toward equal if cap binds); distinguish payoff aggregation from funded wealth. Joint date block comparisons; retrospective recession classification and lagged NFCI sensitivity only after release audit.

## Acceptance and first meeting
CONDITIONAL: actual original strategy_returns.xlsx, permitted use, sleeve labels and common sample must pass; defer if unavailable, not spot substitute.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** conditional. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **KMPV_CARRY — Carry original strategy returns**: strategy_returns.xlsx. Route: https://koijen.net/uploads/3/4/4/7/34470013/strategy_returns.xlsx. Provider: https://www.koijen.net/research.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Exact author-linked workbook; web click reports unsupported ZIP content type; bytes unvalidated.

### Acceptance of the local input set

Verify original KMPV file, three distinct sleeves, funding/units and common dates. Report unscaled and trailing inverse-vol composites, cap and notional, paired stress comparisons; no splicing or executable wealth claim.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

Require original multi-asset strategy returns and documented sleeve units; if unavailable, restrict to verified sleeves only after approval. Do not reconstruct carry from spot returns.

## Design-specific acceptance

Confirm original workbook, documented units, at least three distinct sleeves, no composites or silent splicing. If the core is unavailable, defer. Record stress proxy timing, notional and common dates.

## Timing, accounting and units

Fix currency quote orientation, base currency, return units, settlement dates, funding convention, measure and annualization. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For simulations distinguish expiry from delivery and quote rate from payoff currency.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
