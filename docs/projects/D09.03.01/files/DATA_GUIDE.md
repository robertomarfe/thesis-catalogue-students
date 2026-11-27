# Data and model setup | D09.03.01

**Current data gate: blocked.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Monthly BAA, AAA (percent, long-maturity Moody's averages), INDPRO (seasonally adjusted index), USREC and VIXCLS (monthly mean of daily closes), FRED, https://fred.stlouisfed.org/. Target 1990-2025 common sample. Construct spread in basis points and annual industrial production growth. Respect Moody's source terms before retaining or sharing raw files. Recession chronology is retrospective; no claim of real-time prediction. Use pre-2007 versus later periods for stability, with crisis observations retained and flagged.

## Inputs
- **USREC — USREC** (Core / planned robustness). Expected file: `USREC.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=USREC); [provider page](https://fred.stlouisfed.org/series/USREC). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Monthly recession indicator; retrospective.
- **VIXCLS — VIXCLS** (Core / planned robustness). Expected file: `VIXCLS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS); [provider page](https://fred.stlouisfed.org/series/VIXCLS). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Daily closing index, monthly mean only for spread study.
- **BAA — BAA** (Rights review first). Expected file: `BAA.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAA); [provider page](https://fred.stlouisfed.org/series/BAA). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Moody's proprietary source: verify permitted use before obtaining/retaining; do NOT upload/redistribute without permission.
- **AAA — AAA** (Rights review first). Expected file: `AAA.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=AAA); [provider page](https://fred.stlouisfed.org/series/AAA). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Moody's proprietary source: verify permitted use before obtaining/retaining; do NOT upload/redistribute without permission.
- **INDPRO — INDPRO** (Core / planned robustness). Expected file: `INDPRO.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=INDPRO); [provider page](https://fred.stlouisfed.org/series/INDPRO). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Monthly seasonally adjusted index.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use approved monthly BAA and AAA, exact calendar IP growth, retrospective USREC and VIX monthly mean; use lagged regressors and contiguous dates, common complete sample, HAC and episode blocks. Explicit levels vs changes; no interpolation or replacing series silently.

## Acceptance and first meeting
BLOCKED until documented permission for Moody’s and other required inputs, actual schema and coverage. No raw files present; synthetic independent implementation checks units and monthly alignment only.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** blocked. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **AAA — AAA**: AAA.csv. Route: https://fred.stlouisfed.org/graph/fredgraph.csv?id=AAA. Provider: https://fred.stlouisfed.org/series/AAA. Inherited series route; check AAA-specific rights and metadata locally; do not infer authorization from BAA. Prior link status: Direct CSV endpoint constructed from exact series ID; not fetched.
- **BAA — BAA**: BAA.csv. Route: https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAA. Provider: https://fred.stlouisfed.org/series/BAA. Monthly percent; maturity 20 years or above; provider restricts reproduction, transfer and storage for redistribution. Obtain authorization. Prior link status: Direct CSV endpoint constructed from exact series ID; not fetched.
- **INDPRO — INDPRO**: INDPRO.csv. Route: https://fred.stlouisfed.org/graph/fredgraph.csv?id=INDPRO. Provider: https://fred.stlouisfed.org/series/INDPRO. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Prior link status: Direct CSV endpoint constructed from exact series ID; not fetched.
- **USREC — USREC**: USREC.csv. Route: https://fred.stlouisfed.org/graph/fredgraph.csv?id=USREC. Provider: https://fred.stlouisfed.org/series/USREC. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Prior link status: Direct CSV endpoint constructed from exact series ID; not fetched.
- **VIXCLS — VIXCLS**: VIXCLS.csv. Route: https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS. Provider: https://fred.stlouisfed.org/series/VIXCLS. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Prior link status: Direct CSV endpoint constructed from exact series ID; not fetched.

### Acceptance of the local input set

Obtain written permission or supervisor-approved licensed access, validate exact common monthly calendar and units; compare levels and changes with lagged controls, HAC and crisis/subperiod diagnostics. Do not substitute GZ or another spread without explicit approval.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

Do not substitute an ICE/OAS or Treasury spread for Moody AAA/BAA yield difference without new scope; use a separately approved authorized same-definition series or synthetic credit-cycle design.

## Design-specific acceptance

This design remains blocked until the supervisor verifies rights for both Moody series and actual input coverage. Record original filename, vintage and permitted retention separately for each series. No substitute index or simulation can satisfy the unchanged empirical MVT.

## Timing, accounting and units

Specify physical versus risk-neutral probability, discounted versus undiscounted cash flows, maturity and year fractions, and whether rates and spreads are decimals, percentages or basis points. Document default timing and recovery. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For finite-state models define the state support, probability mass and numerical tolerance before fitting.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
