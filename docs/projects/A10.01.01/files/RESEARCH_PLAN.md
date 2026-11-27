# Research plan | A10.01.01

## Study design and independent work

Persist scaler means/SD and mature fold IDs; perturb future features and immature labels; earlier tuning and forecasts must be invariant. Check zero penalty against OLS when rank permits; document alpha conventions and zero-variance features.

## Prespecified implementation

Freeze Goyal seven predictors and calendar. Standardize independently inside each training fold; unpenalized intercept. sklearn Ridge objective uses sum of squares plus alpha L2; LASSO objective uses SSE/(2n)+alpha L1: report actual conventions and scale grid accordingly. Tune ridge/LASSO/elastic net on nested past-origin errors only; no final selection.

## Required tasks

1. Inspect predictor construction and timing, persistence, correlations and complete sample. Implement expanding historical mean and OLS baselines.

2. For every forecast origin fit scaler and models only on past pairs with realized outcomes; choose lambda on inner expanding folds of past observations, fixed grid and loss. Freeze elastic-net mixing grid and tuning cadence before final test.

3. Compare OOS R2, MSE, MAE and cumulative squared error differences for all models on identical dates; report coefficient paths and selection stability.

4. Use paired block-bootstrap intervals for loss differences and Clark-West where nested linear restrictions justify it (not universal for penalized/tuned models). Report null/negative OOS results and no post-hoc predictor choice.

## Required exhibits

Predictor and coefficient plots, reproducible nested temporal split diagram, forecast series, OOS R2/loss table with uncertainty, selected penalty history and sample/timing log. Distinguish statistical accuracy from any optional economic value.

## Robustness

Prevent scaling, imputation, feature selection and outcome leakage; no full-sample winsorization. Verify one-month shift with a toy series and historical mean using only observed past returns. Compare fixed/expanding training and a prespecified subset of readily observed predictors. Treat revised data and release timing as limitations; do not tune using final results.

## Minimum viable thesis

Verified author file, fixed target and predictor list, mean/OLS/ridge/LASSO with nested chronological tuning, common untouched evaluation period, loss uncertainty and reproducible pipeline. Elastic net may be secondary if time is limited.

## Optional extension

Evaluate a prespecified capped mean-variance timing rule with realistic lag and hypothetical costs; compare with nonlinear method only after core tests.

## Prerequisites

OLS, matrix algebra, basic regularization, scikit-learn pipelines, time-series evaluation.

## Thesis outline

1. Equity premium forecasting;

2. Shrinkage and regularization;

3. Data/timing and nested evaluation;

4. Forecast performance and stability;

5. Economic interpretation and limitations.

## Milestones

W1-3: verify Goyal file and model theory; W4-6: clean data and test temporal pipeline; W7-10: fit/tune on development and run locked test; W11-13: uncertainty and sensitivities; W14-16: write and reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
