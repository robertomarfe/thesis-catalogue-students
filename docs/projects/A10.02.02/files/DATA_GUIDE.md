# Data and model setup | A10.02.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French 25 size/BM monthly value-weighted portfolio returns, FF3 and RF: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Target 1970-2025. Features fixed: lagged own 1/12-month return (excluding target), trailing 12-month volatility, lagged market return, market volatility, portfolio labels. Train 1970-1999, validate 2000-2009, test 2010-2025; expanding annual re-estimation, hyperparameters locked or past-only. Compare historical mean, ridge, MLP widths 4/8/16, L2 penalty and early stopping on past validation dates, five fixed seeds. Optional OSAP separate universe, not required.

## Inputs
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF25M — US 25 size/BM monthly** (Core). Expected file: `25_Portfolios_5x5_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_5x5_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **OSAP_LS — October 2026 original-paper monthly long-short returns** (Optional extension). Expected file: `PredictorLSretWide.parquet`. [Download or provider route](https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet); [provider page](https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet). Historical v13 inventory note (unverified in current release): Exact provider download URL displayed; binary not retrieved. 1.44 MB; file page SHA256 fc01df25d4383153cb3ae9e0dd730cc34b6d15a5207abeff09f34beda45bca58; main may change. Freeze 2026.10 release and revision; historical card license label unverified; check current terms; Illiquidity/BidAskSpread/BetaLiquidityPS; original-paper definitions.
- **OSAP_DOC — October 2026 signal documentation** (Optional extension). Expected file: `SignalDoc.csv`. [Download or provider route](https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/SignalDoc.csv); [provider page](https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/SignalDoc.csv). Historical v13 inventory note (unverified in current release): Exact provider download URL displayed; web preview visible, file not acquired. Freeze same release/revision as portfolios; sign, weighting, quantile, construction, definitions and dates. Cite Chen-Zimmermann (2022), CFR 11(2), 207-264.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use monthly 25 size/BM VW and matched FF3 RF. Lag own 1/12-month returns and vol plus market features, fixed label one-hot intercepts. Keep all portfolios of each date together; expanding annual refits, past-date MLP early stopping and five fixed seeds. Historical mean per asset. Standardize only training dates, report validation epoch/seed and pooled versus per-asset losses. OSAP is optional.

## Acceptance and first meeting
Actual French files, portfolio labels and common date grid open; OSAP not required. Check temporal MLP early stopping and per-asset mean. Starter uses deliberately small artificial panel, not annual production training.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

French 25 size/BM monthly value-weighted portfolio returns, FF3 and RF: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Target 1970-2025. Features fixed: lagged own 1/12-month return (excluding target), trailing 12-month volatility, lagged market return, market volatility, portfolio labels. Train 1970-1999, validate 2000-2009, test 2010-2025; expanding annual re-estimation, hyperparameters locked or past-only. Compare historical mean, ridge, MLP widths 4/8/16, L2 penalty and early stopping on past validation dates, five fixed seeds. Optional OSAP separate universe, not required.

## Design-specific acceptance

Assert no date appears on both sides of a fold; same test rows across models; labels mature before fitting; feature scaler learned on training only; check asset-specific mean benchmark and date-level averaging.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
