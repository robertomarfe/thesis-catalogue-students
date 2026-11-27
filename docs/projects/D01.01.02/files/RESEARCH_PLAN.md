# Research plan | D01.01.02

## Study design and independent work

Freeze the ATM definition and calibration date. Record held-out prices separately from matched-path hedge losses. Build the cash ledger before changing physical jump intensity; do not equate a smaller time step with complete jump-risk replication.

## Required tasks

1. Validate Merton price via independent Monte Carlo, zero-jump BSM limit and parity.

2. Compute ATM implied vol, held-out price/IV errors and sensitivities to intensity and jump size.

3. Implement a self-financing hedge initialized at common true premium; verify cash ledger and terminal liability.

4. Compare discounted P&L error distributions for unhedged, BSM and true-model delta strategies under matched paths; report jump and no-jump subsets.

5. Refine grid to separate discrete errors and residual jump risk; repeat with different physical intensity and independent seeds.

## Required exhibits

IV and pricing-error panels, calibration diagnostics, hedge P&L RMSE/tails, jump-conditioned figures and Monte Carlo uncertainty.

## Robustness

Model delta is not necessarily the variance-minimizing incomplete-market hedge. No claims of empirical accuracy or exact jump-risk replication. Distinguish initial valuation bias from hedge performance; if using differing initial prices report separately. Keep D01.01.01 terminal sensitivities and D04.01.01 diffusion convergence separate.

## Minimum viable thesis

Verified jump pricer and BSM limit, two intensities, two maturities, held-out strikes, matched-path P&L for both hedges and two grids.

## Optional extension

Compare the minimum-variance local hedge or a second traded option as a jump-risk hedge under a documented Q/P specification.

## Prerequisites

Risk-neutral valuation, BSM, Poisson processes, stochastic calculus and Python simulation.

## Thesis outline

1. Complete and incomplete option models;

2. Merton jump pricing and delta;

3. Calibration and experiment;

4. Pricing and hedging error;

5. Model-risk interpretation.

## Milestones

W1-3: Merton model and conditional pricing; W4-6: pricer and inversion tests; W7-9: cross-strike calibration; W10-12: P-path hedge experiments; W13-16: sensitivity and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
