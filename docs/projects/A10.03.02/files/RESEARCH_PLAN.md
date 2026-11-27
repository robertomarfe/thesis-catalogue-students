# Research plan | A10.03.02

## Study design and independent work

Use one shared OSAP revision and distinct file hashes; freeze candidate selection and common SPD weight on training only. Check KKT, scale and unpenalized FF3. Compare same assets future and different assets future, fixed kernel, mean and scale, common metric. No post-selection p-values. Conditional access; no silent substitution.

## Prespecified implementation

Pin OSAP long-short file and metadata in one shared revision with separate file hashes; choose 30–60 signals from metadata/availability without performance. Fit normalized SDF using training industry moment covariance; FF3 unpenalized, ridge/L1 on added factors. Tune common positive definite W and lambda using training industries only. Freeze centering, scale and b; evaluate industries later and separate size/BM portfolios later, no held-out asset input. Negative SDF allowed as diagnostic, not positive feasibility.

## Required tasks

1. Build aligned factor panel and freeze candidate universe; document missingness.

2. Implement penalized moment fit and synthetic known-sparse check.

3. Select lambda by blocked training-only folds and lock models.

4. Compare held-out pricing RMSE, maximum absolute moment and selection frequency over rolling training windows.

5. Compare ridge and alternative asset panels, common-date bootstrap of frozen model scores; report unstable selection.

## Required exhibits

Factor selection path, held-out moment table, overlap/conditioning audit, selection stability and uncertainty.

## Robustness

Shared underlying stocks and correlated factors limit independent validation. No post-selection classical p-values; no claim of unique true factors. Pin OSAP release and exact definitions; equal weighting across assets as baseline.

## Minimum viable thesis

One pinned candidate panel, two held-out asset/date tests, FF3 and ridge comparison, training-only tuning.

## Optional extension

Elastic net and grouped factors by documented economic families, with nested chronological validation.

## Prerequisites

Linear algebra, regularization, SDF moments, Python.

## Thesis outline

1. Factor proliferation;

2. Sparse SDF moments;

3. Data and splits;

4. Transfer and stability;

5. Limits.

## Milestones

W1-3: data and moments; W4-6: synthetic/benchmark; W7-9: nested fit; W10-12: held-out and stability; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
