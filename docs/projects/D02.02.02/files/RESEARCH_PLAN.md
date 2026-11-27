# Research plan | D02.02.02

## Study design and independent work

Do not assign the original empirical design until rights, underlying/forward synchronization and accepted dates/strikes are verified. Freeze cleaning variants, objective and held-out contracts; compare identical observations and retain rejected quote counts.

## Required tasks

1. Audit license, schema, quote coverage and forward/parity consistency before accepting thesis.

2. Implement BSM IV and calibrated synthetic benchmark, compare Heston and SVI.

3. Fit on alternating eligible strikes with fixed date-wise splits, hold out strikes and one maturity only for joint Heston (SVI interpolation requires an explicit maturity rule).

4. Compare midpoint and spread-weighted loss, fraction inside spreads, price/IV error and arbitrage-grid diagnostics.

5. Assess sensitivity to cleaning, multistart and date/maturity selection.

## Required exhibits

Quote coverage/exclusions table, market-fit and held-out surface panels, spread-normalized errors, parameter stability and finite-grid arbitrage checks.

## Robustness

Bid/ask is a range, not an executable trade at mid; quotes do not ensure synchronous prices. No global arbitrage-free claim from finite grid. License may forbid redistribution. Distinct from synthetic D02.02.01.

## Minimum viable thesis

Permission and coverage gate, 10+ suitable dates with 3 expiries, BSM plus SVI/Heston comparison on common held-out strikes, auditable cleaning and uncertainty.

## Optional extension

Fit a constrained surface parametrization with explicit calendar/butterfly sufficient conditions, compare pricing error.

## Prerequisites

Options, IV inversion, nonlinear optimization, data engineering; licensed data access mandatory.

## Thesis outline

1. Market quote structure;

2. IV and calibration;

3. Data cleaning and split;

4. Comparative fit;

5. Model and data limitations.

## Milestones

W1-3: secure permission and coverage; W4-6: clean and benchmark; W7-9: calibration; W10-12: holdouts and robustness; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
