# Research plan | D10.04.01

## Study design and independent work

Check parity, fixed-strike sensitivities and self-financing ledger. Separate matched moneyness comparisons from Greeks. Keep quote orientation and foreign accrual explicit.

## Required tasks

1. Derive Garman-Kohlhagen from domestic Q and foreign numeraire; verify parity and limiting BSM.

2. Implement prices and analytic Greeks, validate by finite differences.

3. Compare rate sensitivities at fixed K vs forward moneyness; plot forward and discounting effects.

4. Simulate a self-financing EUR/USD delta hedge with correct foreign interest; compare incorrect zero-foreign-yield ledger as diagnostic.

5. Optional historical input scenarios with explicitly labeled rates; show not a calibration or realized option P&L.

## Required exhibits

Price and Greek grids; parity/finite difference checks; hedge error distribution; optional scenario charts.

## Robustness

Quote direction and units fixed. Money market yields are not necessarily risk-free or collateralized. Use domestic discounting and foreign accrual consistently; no claims about FX basis or market implied volatility from synthetic prices.

## Minimum viable thesis

Synthetic Garman-Kohlhagen pricing and Greek sensitivity with both rate and moneyness conventions. Delta ledger tested; historical inputs optional.

## Optional extension

Two deterministic term structures or stochastic rates and quanto adjustments.

## Prerequisites

BSM, probability, FX conventions, basic Python.

## Thesis outline

1. FX and numeraires;

2. FX option pricing;

3. Sensitivities;

4. Hedging/scenario analysis;

5. Limitations.

## Milestones

W1-3: derivation; W4-6: pricer and Greeks; W7-9: rate grid; W10-12: ledger and optional replay; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
