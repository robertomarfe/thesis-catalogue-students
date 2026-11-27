# Data and model setup | A10.03.02

**Current data gate: conditional.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Pinned OSAP long-short returns and metadata https://www.openassetpricing.com/; French industries and size/BM portfolios and FF3/5 https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Preselect 30-60 signals by metadata and coverage, not performance; candidate 1975-2025 common sample. Train on industries, tune lambda using blocked chronological industry validation; test on size/BM portfolios and untouched final decade 2016-2025. Also evaluate same assets future dates to separate time and cross-asset transfer. No test-asset input to selection.

## Inputs
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF5M — US FF5 monthly** (Robustness). Expected file: `F-F_Research_Data_5_Factors_2x3_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **OSAP_LS — October 2026 original-paper monthly long-short returns** (Core). Expected file: `PredictorLSretWide.parquet`. [Download or provider route](https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet); [provider page](https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet). Historical v13 inventory note (unverified in current release): Exact provider download URL displayed; binary not retrieved. 1.44 MB; file page SHA256 fc01df25d4383153cb3ae9e0dd730cc34b6d15a5207abeff09f34beda45bca58; main may change. Freeze 2026.10 release and revision; historical card license label unverified; check current terms; Illiquidity/BidAskSpread/BetaLiquidityPS; original-paper definitions.
- **OSAP_DOC — October 2026 signal documentation** (Core). Expected file: `SignalDoc.csv`. [Download or provider route](https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/SignalDoc.csv); [provider page](https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/SignalDoc.csv). Historical v13 inventory note (unverified in current release): Exact provider download URL displayed; web preview visible, file not acquired. Freeze same release/revision as portfolios; sign, weighting, quantile, construction, definitions and dates. Cite Chen-Zimmermann (2022), CFR 11(2), 207-264.
- **FF30M — US 30 industries monthly** (Core). Expected file: `30_Industry_Portfolios_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/30_Industry_Portfolios_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF25M — US 25 size/BM monthly** (Core). Expected file: `25_Portfolios_5x5_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_5x5_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Pin OSAP long-short file and metadata in shared revision; choose 30–60 signals from metadata/availability without performance. Fit normalized SDF using training industry moment covariance; FF3 unpenalized, ridge/L1 on added factors. Tune common positive definite W and lambda using training industries only. Freeze centering, scale and b; evaluate industries later and separate size/BM portfolios later, no held-out asset input. Negative SDF allowed as diagnostic, not positive feasibility.

## Acceptance and first meeting
CONDITIONAL: OSAP revision, rights, file schema and coverage unverified. Do not assign unconditionally or substitute factors silently. Check sparse KKT and an independently constructed artificial known-coefficient check.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** conditional. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **FF25M — US 25 size/BM monthly**: 25_Portfolios_5x5_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_5x5_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed in provider page; bytes not inspected.
- **FF30M — US 30 industries monthly**: 30_Industry_Portfolios_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/30_Industry_Portfolios_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed in provider page; bytes not inspected.
- **FF3M — US FF3 monthly**: F-F_Research_Data_Factors_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed in provider page; bytes not inspected.
- **OSAP_DOC — October 2026 signal documentation**: SignalDoc.csv. Route: https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/SignalDoc.csv. Provider: https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/SignalDoc.csv. Inherited October 2026 migration hypothesis; verify actual release, migration and rights locally. Pin a shared commit with the return file; provider requests citation; no raw redistribution conclusion. Historical link note, not fresh verification: Exact provider download URL displayed; web preview visible, file not acquired.
- **OSAP_LS — October 2026 original-paper monthly long-short returns**: PredictorLSretWide.parquet. Route: https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet. Provider: https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet. Inherited candidate description of end-of-month portfolio returns; verify locally; pin same verified shared release with SignalDoc; exact columns, units and rights unverified. Historical link note, not fresh verification: Exact provider download URL displayed; binary not retrieved.

### Acceptance of the local input set

Pin shared dictionary/return revision and rights; freeze candidate selection and common SPD weight from training only. Check KKT, scale and unpenalized FF3 terms; compare same assets future versus different assets future, fixed b/mu/sd and identical metric. No post-selection p-values.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

Defer if OSAP and test assets fail. A smaller factor dictionary is a different sparsity exercise; approve it separately and preserve disjoint test assets and dates.
Use one shared, actually retrieved OSAP commit; record a separate SHA-256 for dictionary and returns. Verify coverage and rights. The v61 source evidence erratum supersedes historical fresh-verification labels. Include the original FF5 benchmark with a separately verified monthly five-factor file. No substitute without approval.


## Frozen research design (original catalogue)

Pinned OSAP long-short returns and metadata https://www.openassetpricing.com/; French industries and size/BM portfolios and FF3/5 https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Preselect 30-60 signals by metadata and coverage, not performance; candidate 1975-2025 common sample. Train on industries, tune lambda using blocked chronological industry validation; test on size/BM portfolios and untouched final decade 2016-2025. Also evaluate same assets future dates to separate time and cross-asset transfer. No test-asset input to selection.

## Design-specific acceptance

Use one shared OSAP revision and distinct file hashes; freeze candidate selection and common SPD weight on training only. Check KKT, scale and unpenalized FF3. Compare same assets future and different assets future, fixed kernel, mean and scale, common metric. No post-selection p-values. Conditional access; no silent substitution.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
