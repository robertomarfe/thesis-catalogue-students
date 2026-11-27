# Research plan | A12.04.02

## Study design and independent work

Pin eight named signals and OSAP dictionary, common factor sample; report cost/turnover grid with exact units, negative alphas and uncertainty. Verify intercept translation with constant costs; use exact matched turnover only when authorized and documented, else scenario exercise. Do not compound unfunded spread or claim tradability.

## Prespecified implementation

Pin matching OSAP returns/metadata and FF3/5+Mom; select 8-12 signal holding periods/categories before observing Sharpe; common 1990-2025, 1990-2009 descriptive and 2010-25 comparison. Returns already long-short; verify leverage/turnover convention and whether gross or net. If no matched turnover, use monthly tau .1/.25/.5/1/2, cost 5..100bp; net spread r-c*tau, break-even c=mean/tau with units; negative mean has no nonnegative break-even. For constant deduction alpha shifts equally under same factor matrix, distinguish mean break-even and alpha break-even. If actual turnover use same portfolio/vintage/leverage only. No funded wealth/compounding on zero-cost spreads. Report paired inference and multiplicity, no investability assertion.

## Required tasks

1. Check units, gross/net definitions and capital normalization.

2. Estimate gross mean, alpha and HAC intervals.

3. Compute scenario net returns and break-even frontiers with uncertainty.

4. Compare rankings by costs and holding-period categories; distinguish fixed versus hypothetical state-dependent turnover.

5. Add separately stated financing and borrow-cost scenarios; test gross-notional convention sensitivity.

## Required exhibits

Break-even cost/turnover contours, gross and scenario-net alpha table, data/provenance audit and uncertainty.

## Robustness

Return-only series cannot recover traded notional, spreads, market impact, borrow or capacity. Scenario analysis is not historical executable net performance. No turnover inferred from return autocorrelation. Avoid look-ahead signal selection.

## Minimum viable thesis

Eight signals, common factor sample, two-dimensional cost grid and explicit no-turnover-data limitation.

## Optional extension

Use verified published holdings/turnover for a subset, then compare scenario and observed turnover-based estimates.

## Prerequisites

Factor models, portfolio accounting, regression, Python.

## Thesis outline

1. Implementation frictions;

2. Cost accounting;

3. Data;

4. Break-even analysis;

5. Limits.

## Milestones

W1-3: source/turnover audit; W4-6: gross benchmarks; W7-9: cost grids; W10-12: alpha and uncertainty; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
