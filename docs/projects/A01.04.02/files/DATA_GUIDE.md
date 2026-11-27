# Data and model setup | A01.04.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French 30 industry monthly returns and FF3/5, 25 size/BM test portfolios https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; OSAP pinned long-short panel https://www.openassetpricing.com/ as alternative source of training assets subject to access. Baseline industry PC3/PC5 versus FF3/FF5, 1970-1999 fit, 2000-2009 validation, 2010-2025 frozen test. Use distinct test portfolio definitions, acknowledge stock overlap; no normalization using test dates. Define RF treatment for long-short vs long-only portfolios.

## Inputs
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF5M — US FF5 monthly** (Robustness). Expected file: `F-F_Research_Data_5_Factors_2x3_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **OSAP_LS — October 2026 original-paper monthly long-short returns** (Optional extension). Expected file: `PredictorLSretWide.parquet`. [Download or provider route](https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet); [provider page](https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/Portfolios/Full%20Sets%20OP/PredictorLSretWide.parquet). Historical v13 inventory note (unverified in current release): Exact provider download URL displayed; binary not retrieved. 1.44 MB; file page SHA256 fc01df25d4383153cb3ae9e0dd730cc34b6d15a5207abeff09f34beda45bca58; main may change. Freeze 2026.10 release and revision; historical card license label unverified; check current terms; Illiquidity/BidAskSpread/BetaLiquidityPS; original-paper definitions.
- **OSAP_DOC — October 2026 signal documentation** (Optional extension). Expected file: `SignalDoc.csv`. [Download or provider route](https://huggingface.co/datasets/OpenSourceAP/CrossSection/resolve/main/SignalDoc.csv); [provider page](https://huggingface.co/datasets/OpenSourceAP/CrossSection/blob/main/SignalDoc.csv). Historical v13 inventory note (unverified in current release): Exact provider download URL displayed; web preview visible, file not acquired. Freeze same release/revision as portfolios; sign, weighting, quantile, construction, definitions and dates. Cite Chen-Zimmermann (2022), CFR 11(2), 207-264.
- **FF30M — US 30 industries monthly** (Core). Expected file: `30_Industry_Portfolios_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/30_Industry_Portfolios_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF25M — US 25 size/BM monthly** (Core). Expected file: `25_Portfolios_5x5_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_5x5_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Baseline 30 VW industries, FF3/FF5 and 25 size/BM; 1970–1999 train, 2000–09 validation, 2010–25 frozen test. Fit covariance/correlation PCA only on train excess returns. Use fixed weights on raw excess returns for PC factor payoffs, not demeaned scores that erase premia. For same assets freeze estimated beta; for disjoint portfolios estimate exposures using their pre-holdout returns to frozen training-asset factors, never test means. Compare variance reconstruction and pricing separately, acknowledge shared underlying stocks; OSAP alternative only if permitted.

## Acceptance and first meeting
French baseline actual input gates pending; OSAP alternative conditional, not required to pass MVT. Actual source rights, bytes, dates, decimal units, common sample and covariance rank pending; 

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Freeze factor dimensions, weights, means and model selection before the test. Audit date and asset holdouts separately, report factor return scaling and rank, and retain common pricing moments. Optional OSAP alternative requires its own access verification.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
