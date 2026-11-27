# Data and model setup | A12.02.02

**Current data gate: conditional.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Baker-Wurgler monthly sentiment https://pages.stern.nyu.edu/~jwurgler/data/SENTIMENT.xlsx (author page https://pages.stern.nyu.edu/~jwurgler/main.htm; listed July 1965-Dec 2025); OSAP long-short parquet and SignalDoc https://huggingface.co/datasets/OpenSourceAP/CrossSection; monthly French FF3/FF5/momentum https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Preselect 8-12 signals across valuation, profitability, issuance and investment by metadata before viewing results; common sample proposed 1970-2025 subject to coverage. Lag sentiment at least two months, standardize using expanding historical moments, acknowledge revised index; no point-in-time claim.

## Inputs
- **OSAP_LS — October 2026 original-paper monthly long-short returns** (Core). Expected file: `PredictorLSretWide.parquet`. [Download or provider route](https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet); [provider page](https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet). Historical v13 inventory note (unverified in current release): Exact provider download URL displayed; binary not retrieved. 1.44 MB; file page SHA256 fc01df25d4383153cb3ae9e0dd730cc34b6d15a5207abeff09f34beda45bca58; main may change. Freeze 2026.10 release and revision; historical card license label unverified; check current terms; Illiquidity/BidAskSpread/BetaLiquidityPS; original-paper definitions.
- **OSAP_DOC — October 2026 signal documentation** (Core). Expected file: `SignalDoc.csv`. [Download or provider route](https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/SignalDoc.csv); [provider page](https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/SignalDoc.csv). Historical v13 inventory note (unverified in current release): Exact provider download URL displayed; web preview visible, file not acquired. Freeze same release/revision as portfolios; sign, weighting, quantile, construction, definitions and dates. Cite Chen-Zimmermann (2022), CFR 11(2), 207-264.
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF5M — US FF5 monthly** (Robustness). Expected file: `F-F_Research_Data_5_Factors_2x3_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFMOM — US momentum monthly** (Core). Expected file: `F-F_Momentum_Factor_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Momentum_Factor_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **BW_SENT — Baker-Wurgler investor sentiment monthly workbook** (Core). Expected file: `SENTIMENT.xlsx`. [Download or provider route](https://pages.stern.nyu.edu/~jwurgler/data/SENTIMENT.xlsx); [provider page](https://pages.stern.nyu.edu/~jwurgler/main.htm). Historical v13 inventory note (unverified in current release): Author-linked workbook verified; web click unsupported content type, runtime DNS failure. Author lists July 1965-Dec 2025. Inspect raw/orthogonalized columns, construction/revision notes, rights and availability lag; no point-in-time claim.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Pin OSAP long-short and SignalDoc revision, preselect 8-12 signals by valuation/profitability/issuance/investment metadata before viewing outcomes. Baker–Wurgler SENTIMENT.xlsx author-linked; page snapshot here lists 196507-202312, frozen proposal says through Dec 2025: pin actual downloaded version and report shortened coverage, not infer missing 2024-25. Choose raw or orthogonalized series before results; minimum two-month lag and expanding past-only standardization, revised not real-time. FF3/5+Mom common sample, interactions in alpha and betas, joint calendar inference with multiplicity; no RF subtraction for long-short. No stock-level sorting from published factor series.

## Acceptance and first meeting
CONDITIONAL: actual same-release OSAP and sentiment workbook, exact columns, coverage and rights. Require eight preselected signals; no substitution without approval.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** conditional. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **BW_SENT — Baker-Wurgler investor sentiment monthly workbook**: SENTIMENT.xlsx. Route: https://pages.stern.nyu.edu/~jwurgler/data/SENTIMENT.xlsx. Provider: https://pages.stern.nyu.edu/~jwurgler/main.htm. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Author-linked workbook verified; web click unsupported content type, runtime DNS failure.
- **FF3M — US FF3 monthly**: F-F_Research_Data_Factors_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed in provider page; bytes not inspected.
- **FFMOM — US momentum monthly**: F-F_Momentum_Factor_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Momentum_Factor_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Historical link note, not fresh verification: Direct link observed in provider page; bytes not inspected.
- **OSAP_DOC — October 2026 signal documentation**: SignalDoc.csv. Route: https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/SignalDoc.csv. Provider: https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/SignalDoc.csv. Inherited October 2026 migration hypothesis; verify actual release, migration and rights locally. Pin a shared commit with the return file; provider requests citation; no raw redistribution conclusion. Historical link note, not fresh verification: Exact provider download URL displayed; web preview visible, file not acquired.
- **OSAP_LS — October 2026 original-paper monthly long-short returns**: PredictorLSretWide.parquet. Route: https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet. Provider: https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet. Inherited candidate description of end-of-month portfolio returns; verify locally; pin same verified shared release with SignalDoc; exact columns, units and rights unverified. Historical link note, not fresh verification: Exact provider download URL displayed; binary not retrieved.

### Acceptance of the local input set

Pin actual sentiment workbook and matching eight OSAP signals/dictionary, state definition and fixed selection. Use lagged states and common months, show alpha=a+c*z and beta interactions, joint date-block uncertainty with familywise/FDR sensitivity and predeclared regime robustness. No data substitution without supervisor approval.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

If sentiment version or eight matched OSAP signals fail, defer or narrow with approval; preserve lag and release caveats.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

Baker-Wurgler monthly sentiment https://pages.stern.nyu.edu/~jwurgler/data/SENTIMENT.xlsx (author page https://pages.stern.nyu.edu/~jwurgler/main.htm; listed July 1965-Dec 2025); OSAP long-short parquet and SignalDoc https://huggingface.co/datasets/OpenSourceAP/CrossSection; monthly French FF3/FF5/momentum https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Preselect 8-12 signals across valuation, profitability, issuance and investment by metadata before viewing results; common sample proposed 1970-2025 subject to coverage. Lag sentiment at least two months, standardize using expanding historical moments, acknowledge revised index; no point-in-time claim.

## Design-specific acceptance

Pin actual sentiment workbook and matching eight OSAP signals/dictionary, state definition and fixed selection. Use lagged states and common months, show alpha=a+c*z and beta interactions, joint date-block uncertainty with familywise/FDR sensitivity and predeclared regime robustness. No data substitution without supervisor approval.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish funded wealth from zero-investment spreads, gross from net performance, allocation-time moments from realized risk, and actual turnover from hypothetical trading costs.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
