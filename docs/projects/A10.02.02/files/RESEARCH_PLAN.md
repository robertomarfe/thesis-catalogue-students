# Research plan | A10.02.02

## Study design and independent work

Assert no date appears on both sides of a fold; same test rows across models; labels mature before fitting; feature scaler learned on training only; check asset-specific mean benchmark and date-level averaging.

## Prespecified implementation

Use monthly 25 size/BM VW and matched FF3 RF. Lag own 1/12-month returns and vol plus market features, fixed label one-hot intercepts. Keep all portfolios of each date together; expanding annual refits, past-date MLP early stopping and five fixed seeds. Historical mean per asset. Standardize only training dates, report validation epoch/seed and pooled versus per-asset losses. OSAP is optional.

## Required tasks

1. Simulate panel with linear/nonlinear known signal and common date shocks; verify pipeline and leakage test.

2. Build aligned features and targets, keep all portfolios of a date in same split, scale only training data.

3. Fit models on identical training information, tune small grid and freeze protocol.

4. Evaluate pooled and per-portfolio OOS R2 against expanding historical mean; paired date-block loss differences and seed dispersion.

5. Optional long-short forecast-ranked portfolios on lagged weights, report gross returns and turnover; no stock-level claim.

## Required exhibits

Sample/split diagram, training diagnostics, per-model forecast errors, OOS R2 by portfolio, date-bootstrap intervals and seed sensitivity.

## Robustness

No random row-level cross-validation. Do not train on test labels or rescale full sample. Effective date sample is limited; repeated tuning on test invalid. Published portfolio series may be revised; no firm-level forecasts.

## Minimum viable thesis

French panel, same features for ridge/MLP, one locked chronological test and uncertainty across dates/seeds. Distinct from aggregate tree-based A10.02.01.

## Optional extension

OSAP long-short panel from pinned release; compare nonlinear interactions and stability without expanding model search.

## Prerequisites

Regression, basic ML, Python scikit-learn, temporal validation.

## Thesis outline

1. Forecasting and nonlinear models;

2. Panel design;

3. Model training;

4. Held-out results;

5. Economic interpretation.

## Milestones

W1-3: theory and simulation; W4-6: data/splits; W7-9: tuning; W10-12: test and robustness; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
