# Data and model setup | D03.01.01

No empirical input bytes are included or validated.

## Input contract

French US daily Fama/French 3 Factors, columns Mkt-RF and RF, reconstructed market simple return in decimals; use log(1+R) where defined. Target 1990-2025, subject to file inspection. Use 1990-2004 initial estimation, 2005-2025 untouched sequential evaluation; document any shorter common sample. Fix rolling windows 21 and 252 days and a 5-year GARCH estimation window; monthly refits with daily filtering. Keep the data vintage, ignore missing sentinel codes, never fill missing dates as zero. Daily target is squared demeaned return using a predetermined mean convention; 21-day target is the sum of squared future innovations over trading days. Source: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html

## Acquisition and acceptance

Only required file: `F-F_Research_Data_Factors_daily_CSV.zip`, [direct download](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip). Official [library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Use daily US factors from a single version. Store raw bytes privately, record original filename, date, hash, provider copyright and permitted use. No central upload required. VIX is optional, not a required second input. Do not redistribute without permission.


## Sample, timing and transformations
Target 1990-01 to 2025-12 (dates inclusive subject to availability), initial estimation/choice 1990–2004, evaluation origins from 2005 through final dates whose future labels are fully observed within 2025. Proposed acceptance before work: continuous available series covering initial 1990–2004 training and at least 15 calendar years of evaluation, no unexplained missing daily returns; if shorter seek supervisor approval of a revised frozen split before viewing forecast performance. No padding missing trading days. Fixed initial demean convention: use training-only mean for all models/targets (alternative past-only rolling mean in robustness). Define u_t=x_t-mu_train. Label daily v_{t,1}=u_(t+1)^2; cumulative v_{t,21}=sum_{j=1}^{21}u_(t+j)^2 over 21 trading observations with complete coverage. Store origin date, first/last target date, horizon and maturity indicator. For historical forecast h, use only preceding 21 or 252 observed squared innovations; for GARCH refit monthly using preceding 5 years, update variance daily. Both horizons sum forecasts in per-horizon variance units, not annualized volatility. Fit/validation uses only matured target labels when necessary. No model selection on test losses. Omit the last 21 origins lacking complete labels. QLIKE log(h)+v/h with positive documented h floor; MSE in matching units; same valid origins for comparisons. Explain why noisy squared innovations are not intraday realized variance; 21 trading days not exactly one calendar month. Main analysis and inference remain student tasks.

## Week 1–2 input gate
Deliver local manifest, independently implemented input validation, counts missing and excluded by reason, sample date coverage and dated label preview (no raw-data transfer if not entitled). Manually check first and final complete target windows and the training/test split. If raw access, acceptable coverage or units fail: stop, ask supervisor for approved source/sample redesign, never imply GARCH forecast result. A passed recipe or toy test alone does not pass the actual-data gate. If accepted, continue W3–6 benchmark and W7–10 main analysis per proposal.


Use standard Python ZIP/CSV tools to inspect the actual file and manually reconcile header, rows and calendar; no reader or forecasting implementation is provided.

## First-meeting acceptance record

Record actual source version or simulation specification, acquisition rights, date and SHA-256 for any local inputs, schema/units, exclusions, sample or parameter grid and independently designed acceptance checks. Stop and agree a revised design if the specified input is not obtainable. No automatic data or assignment approval.
