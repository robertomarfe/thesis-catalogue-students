# Data and model setup | D04.02.02

**Current data gate: blocked.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Use daily S&P 500 price index SP500 from https://fred.stlouisfed.org/series/SP500 (rolling ten-year coverage; freeze available snapshot). Choose all nonoverlapping 63-trading-day windows after a 252-day volatility warmup, label stress by realized drawdown only for ex post evaluation. Rebase each path to 100; strikes 90,100,110; r=2%, q=0 illustrative; fixed historical volatility estimated before inception and rolling lagged alternative. Synthetic GBM controls match inception volatility, horizon, observation grid and drift scenario. Seed 2027, 5,000 paths per representative parameter set. If price history unavailable, use jump and high-variance stress DGP only as explicitly retitled fallback.

## Inputs
- **SP500 — SP500** (Core hybrid S; historical replay). Expected file: `SP500.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500); [provider page](https://fred.stlouisfed.org/series/SP500). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. FRED limited rolling history; price index only.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Acquire permitted SP500 price closes and actual session calendar; form nonoverlapping 63-session paths with 252 prior returns. Use fixed inception vol and rolling lagged vol. Compare same rebase, strikes, funding and pricing convention with GBM; stress labels only ex post.

## Acceptance and first meeting
BLOCKED until permitted SP500 and adequate complete windows verified, or explicitly approved retitled synthetic fallback. Check warm-up and missing sessions.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** blocked. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **SP500 — SP500**: SP500.csv. Route: https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500. Provider: https://fred.stlouisfed.org/series/SP500. Rolling ten years of daily price-index history, not total return. Reproduction requires S&P permission; no permission established. Prior link status: Direct CSV endpoint constructed from exact series ID; not fetched.

### Acceptance of the local input set

Acquire authorized exact price history with session calendar and warm-up; freeze stress rules before measuring error, compare same synthetic rules with matched GBM. If unavailable, require explicit retitled simulation approval.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

Retitle to simulated jump/high-variance stress hedge experiments if historical replay impossible; distinguish from D01.03.03 by predeclared stress-window and hedge frequency design.

## Timing, accounting and units

Define the pricing measure, path measure, position and loss signs, trading dates, initial funding and terminal liquidation. Freeze the provider vintage for empirical designs, retain common dates and distinguish price indices from total-return indices. A historical replay of synthetic option quotes is not a realized traded-option backtest.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
