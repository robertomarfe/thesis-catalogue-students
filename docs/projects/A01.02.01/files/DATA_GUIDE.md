# Data and model setup | A01.02.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

Actual raw files not acquired or validated. The inherited candidate routes from the [French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html) are listed below; verify the current provider listings. Download the CSV archives in one session only if your academic use is authorized; do not redistribute them without checking applicable terms. Record date, provider URL, exact file SHA256, file format/vintage and rights decision. Save to a local folder outside the distributed package.

| Input | Download | Required block |
|---|---|---|
| FF3M | [F-F_Research_Data_Factors_CSV.zip](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip) | Monthly 3 factors plus RF |
| FF5M | [F-F_Research_Data_5_Factors_2x3_CSV.zip](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip) | Monthly 5 factors plus RF |
| FF30M | [30_Industry_Portfolios_CSV.zip](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/30_Industry_Portfolios_CSV.zip) | 30 value-weighted monthly industry returns |
| FF25M | [25_Portfolios_5x5_CSV.zip](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_5x5_CSV.zip) | 25 value-weighted monthly size/BM returns |

The FF5 details page reports July 1963 onward and specifies SMB as an average across size/BM, size/profitability, size/investment constructions. RF source changes in June 2024; January 2025 data releases use CIZ instead of FIZ. Treat revised history as a single vintage, not as information available at each historical date. The two asset files must contain the explicit `Average Value Weighted Returns -- Monthly` block, not equal-weighted, annual, number of firms, or firm size blocks. Percent returns /100; sentinels -99.99 and -999 become missing. Never apply percent conversion twice. Validate actual headers before relying on parser.

Run from the extracted workspace:
Build an independent local preflight for hashes, calendar coverage, RF equality and schema.
Your independent preflight should report hashes, common-date coverage and RF equality, not fitted models. Require at least 120 complete months in each prespecified subperiod (provisional rule), check T>N+K, report every missing month and any asset loss. Do not infer access from URL alone. If 30 industries fail covariance, 10 industries is an permitted sensitivity only (use official library row). No silent fallback or replacement.

For each portfolio set, compute simple excess returns once using common RF, compare literal factors on identical dates. Record intersection losses before computing results. The data sample ends December 2025 even if newer data are available. The initial acquisition gate requires real files, rights and supervisor approval.

## Design-specific acceptance

Require the monthly return blocks, matched RF and common complete calendar, positive GRS degrees of freedom, and at least the original provisional subperiod coverage. Refit paired alpha differences in joint time blocks. Document covariance singularity rather than silently regularizing the classical GRS statistic.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
