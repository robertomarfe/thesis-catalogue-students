# Data and model setup | A01.03.02

**Current data gate: conditional.** No actual external input bytes are supplied or validated.

## Original input contract and sample
OSAP PredictorLSretWide and SignalDoc https://huggingface.co/datasets/OpenSourceAP/CrossSection, French FF3/FF5/momentum https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Freeze same OSAP revision; choose 20-40 predictors with verified original sample end and journal publication year/month from SignalDoc and original papers. Predeclare availability criteria (at least 24 months in each feasible window), equal 36-month before/after publication as complementary sample; publication year only implies start post period January of following year; ambiguous dates excluded, not inferred.

## Inputs
- **OSAP_LS — October 2026 original-paper monthly long-short returns** (Core). Expected file: `PredictorLSretWide.parquet`. [Download or provider route](https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet); [provider page](https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet). Historical v13 inventory note (unverified in current release): Exact provider download URL displayed; binary not retrieved. 1.44 MB; file page SHA256 fc01df25d4383153cb3ae9e0dd730cc34b6d15a5207abeff09f34beda45bca58; main may change. Freeze 2026.10 release and revision; historical card license label unverified; check current terms; Illiquidity/BidAskSpread/BetaLiquidityPS; original-paper definitions.
- **OSAP_DOC — October 2026 signal documentation** (Core). Expected file: `SignalDoc.csv`. [Download or provider route](https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/SignalDoc.csv); [provider page](https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/SignalDoc.csv). Historical v13 inventory note (unverified in current release): Exact provider download URL displayed; web preview visible, file not acquired. Freeze same release/revision as portfolios; sign, weighting, quantile, construction, definitions and dates. Cite Chen-Zimmermann (2022), CFR 11(2), 207-264.
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF5M — US FF5 monthly** (Robustness). Expected file: `F-F_Research_Data_5_Factors_2x3_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFMOM — US momentum monthly** (Core). Expected file: `F-F_Momentum_Factor_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Momentum_Factor_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use same pinned OSAP release; verify original sample end and publication date from SignalDoc plus original articles, 20–40 signals and ≥24 months per feasible window. Exclude ambiguous or overlapping windows before inspecting results; year-only publication starts post January following year. Freeze sign. Estimate signal FE on raw and benchmark-adjusted outcomes, and calendar FE on common support with staggered timing; retain identification rank check. Joint month-block resampling on signal-level outcomes and date labels, signal sensitivity, fixed 36-month windows and ex ante placebo. Calendar FE can absorb common timing; no causal publication effect.

## Acceptance and first meeting
CONDITIONAL: actual OSAP files/revision and verified publication dates for ≥20 predictors required; no inferred dates. Actual source rights, bytes, dates, decimal units, common sample and covariance rank pending; 

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** conditional. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **FF3M — US FF3 monthly**: F-F_Research_Data_Factors_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed in provider page; bytes not inspected.
- **FFMOM — US momentum monthly**: F-F_Momentum_Factor_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Momentum_Factor_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed in provider page; bytes not inspected.
- **OSAP_DOC — October 2026 signal documentation**: SignalDoc.csv. Route: https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/SignalDoc.csv. Provider: https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/SignalDoc.csv. Inherited October 2026 migration hypothesis; verify actual release, migration and rights locally. Pin a shared commit with the return file; provider requests citation; no raw redistribution conclusion. Historical link note, not fresh verification: Exact provider download URL displayed; web preview visible, file not acquired.
- **OSAP_LS — October 2026 original-paper monthly long-short returns**: PredictorLSretWide.parquet. Route: https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet. Provider: https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet. Inherited candidate description of end-of-month portfolio returns; verify locally; pin same October 2026 or specified release with SignalDoc; exact columns, units and rights unverified. Historical link note, not fresh verification: Exact provider download URL displayed; binary not retrieved.

### Acceptance of the local input set

Document date sources and year-only convention (next January), enforce ordered windows, minimum sample and fixed paired predictors; calendar-block or two-way dependence diagnostic and signal/calendar FE rank. If only two windows feasible, use explicitly permitted two-window subset. Do not claim publication causes attenuation.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

If publication dates or sample ends unverifiable, exclude ambiguous signals and reassess minimum 20. If below minimum, defer or approve a narrower dated subset.

## Design-specific acceptance

Retain the minimum 20 dated predictors and original minimum coverage; distinguish a permitted two-window subset from a three-window design. Log every date source and exclusion; do not equate journal publication with first dissemination or the OSAP migration with verified access.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
