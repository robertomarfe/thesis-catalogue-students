# Research plan | D10.04.02

## Study design and independent work

Check martingale, parity, zero intensity, truncation including stock-weighted tail, ATM feasibility and independent Monte Carlo. Report infeasible cases; no observed smile claim.

## Required tasks

1. Derive compensator and conditional moments; check E_Q[S_T]=F and parity.

2. Implement mixture and MC reference, verify zero-intensity limit.

3. Solve ATM price match, compare skew, butterfly and wing implied vol in fixed log-forward moneyness.

4. Vary jump frequency and severity at approximately fixed jump variance; assess observational equivalence and failure of single-slice identification.

5. Reverse quote direction only using the correct foreign measure/numeraire, or keep original orientation throughout; document interpretation.

## Required exhibits

Martingale and parity tests; ATM calibration table; smiles by jump scenario; wing error/identification plots.

## Robustness

P jump estimates do not identify Q jump risk. Compare same forward and maturity; do not naively invert S under the same pricing measure. No claim to empirically explain market FX risk reversals without quotes.

## Minimum viable thesis

Domestic-Q Merton mixture, matched ATM scenarios, skew/curvature comparisons and independent MC check. Distinct from equity jump pricing and diffusion FX pricing D10.04.01.

## Optional extension

Compare symmetric versus asymmetric double-exponential jump models or multi-maturity synthetic calibration.

## Prerequisites

FX derivatives, jump processes, implied volatility and Python.

## Thesis outline

1. FX pricing and numeraires;

2. Jump model;

3. Mixture and ATM matching;

4. Smile implications;

5. Identification limits.

## Milestones

W1-3: derivation; W4-6: mixture/MC; W7-9: calibration grid; W10-12: wing/identification checks; W13-16: writing and replication.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
