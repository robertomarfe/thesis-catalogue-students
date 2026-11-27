# Data and model setup | A12.01.01

**Current data gate: conditional.** No actual external input bytes are supplied or validated.

## Original input contract and sample
OSAP October 2026 release, https://huggingface.co/datasets/OpenSourceAP/CrossSection, monthly original-paper long-short file PredictorLSretWide.parquet plus SignalDoc.csv; inspect Illiquidity, BidAskSpread, BetaLiquidityPS, DolVol and zerotrade12M (confirm definition, sign, units, availability); preselect first three core signals. FF3/5 and Mom from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; NFCI from https://fred.stlouisfed.org/series/NFCI. Target 1973-2025 or common intersection; use full-sample descriptive alphas and 2000-2025 temporal stability. One-month lag on NFCI; revised-vintage caveat.

## Inputs
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF5M — US FF5 monthly** (Core). Expected file: `F-F_Research_Data_5_Factors_2x3_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFMOM — US momentum monthly** (Core). Expected file: `F-F_Momentum_Factor_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Momentum_Factor_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **NFCI — NFCI** (Core). Expected file: `NFCI.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=NFCI); [provider page](https://fred.stlouisfed.org/series/NFCI). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Weekly; release lag and vintage.
- **OSAP_LS — October 2026 original-paper monthly long-short returns** (Core). Expected file: `PredictorLSretWide.parquet`. [Download or provider route](https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet); [provider page](https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet). Historical v13 inventory note (unverified in current release): Exact provider download URL displayed; binary not retrieved. 1.44 MB; file page SHA256 fc01df25d4383153cb3ae9e0dd730cc34b6d15a5207abeff09f34beda45bca58; main may change. Freeze 2026.10 release and revision; historical card license label unverified; check current terms; Illiquidity/BidAskSpread/BetaLiquidityPS; original-paper definitions.
- **OSAP_DOC — October 2026 signal documentation** (Core). Expected file: `SignalDoc.csv`. [Download or provider route](https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/SignalDoc.csv); [provider page](https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/SignalDoc.csv). Historical v13 inventory note (unverified in current release): Exact provider download URL displayed; web preview visible, file not acquired. Freeze same release/revision as portfolios; sign, weighting, quantile, construction, definitions and dates. Cite Chen-Zimmermann (2022), CFR 11(2), 207-264.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Pin OSAP original-paper long-short returns and matching SignalDoc same revision; original proposed October 2026 not verified, public website accessible but repository inaccessible. Verify Illiquidity, BidAskSpread and BetaLiquidityPS names, long-short orientation, holding period and units before data outcomes; do not switch to a different signal silently. FF3/5+Mom common monthly sample, one-month lagged NFCI subject to release, revised vintage label. HAC common dates, state interaction with both alpha and factor loadings, joint calendar-block uncertainty and multiple testing. No RF subtraction for zero-cost returns; no causal liquidity-price claim.

## Acceptance and first meeting
CONDITIONAL: actual matched OSAP revision, first three signal definitions, rights, FF/NFCI coverage. If inaccessible defer or explicitly approve a different design.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** conditional. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **FF3M — US FF3 monthly**: F-F_Research_Data_Factors_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed in provider page; bytes not inspected.
- **FF5M — US FF5 monthly**: F-F_Research_Data_5_Factors_2x3_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed in provider page; bytes not inspected.
- **FFMOM — US momentum monthly**: F-F_Momentum_Factor_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Momentum_Factor_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed in provider page; bytes not inspected.
- **NFCI — NFCI**: NFCI.csv. Route: https://fred.stlouisfed.org/graph/fredgraph.csv?id=NFCI. Provider: https://fred.stlouisfed.org/series/NFCI. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct CSV endpoint constructed from exact series ID; not fetched.
- **OSAP_DOC — October 2026 signal documentation**: SignalDoc.csv. Route: https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/SignalDoc.csv. Provider: https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/SignalDoc.csv. Inherited October 2026 migration hypothesis; verify actual release, migration and rights locally. Pin a shared commit with the return file; provider requests citation; no raw redistribution conclusion. Historical link note, not fresh verification: Exact provider download URL displayed; web preview visible, file not acquired.
- **OSAP_LS — October 2026 original-paper monthly long-short returns**: PredictorLSretWide.parquet. Route: https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet. Provider: https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet. Inherited candidate description of end-of-month portfolio returns; verify locally; pin same verified shared release with SignalDoc; exact columns, units and rights unverified. Historical link note, not fresh verification: Exact provider download URL displayed; binary not retrieved.

### Acceptance of the local input set

Pin same OSAP dictionary and return revision, exactly three named signals and direction; match factors/RF conventions and release-aware NFCI. Fit unconditional and interaction models on same dates; conditional alpha=a+c*z, conditional beta=b+d*z. Joint blocks and multiple-comparison sensitivity; defer if no authorized bytes.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

If three liquidity-related signals/dictionary unavailable, defer. An alternate liquidity proxy requires explicit redesign and must remain distinct from BAB.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

OSAP October 2026 release, https://huggingface.co/datasets/OpenSourceAP/CrossSection, monthly original-paper long-short file PredictorLSretWide.parquet plus SignalDoc.csv; inspect Illiquidity, BidAskSpread, BetaLiquidityPS, DolVol and zerotrade12M (confirm definition, sign, units, availability); preselect first three core signals. FF3/5 and Mom from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; NFCI from https://fred.stlouisfed.org/series/NFCI. Target 1973-2025 or common intersection; use full-sample descriptive alphas and 2000-2025 temporal stability. One-month lag on NFCI; revised-vintage caveat.

## Design-specific acceptance

Pin same OSAP dictionary and return revision, exactly three named signals and direction; match factors/RF conventions and release-aware NFCI. Fit unconditional and interaction models on same dates; conditional alpha=a+c*z, conditional beta=b+d*z. Joint blocks and multiple-comparison sensitivity; defer if no authorized bytes.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish funded wealth from zero-investment spreads, gross from net performance, allocation-time moments from realized risk, and actual turnover from hypothetical trading costs.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
