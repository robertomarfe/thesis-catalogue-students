# Research plan | D01.03.01

## Study design and independent work

Build admissible variance-matched configurations before calculating prices. Hold forward fixed and compare several maturities; report ordinary and stock-weighted truncation diagnostics. Keep jump-size and intensity perturbations distinct.

## Required tasks

1. Derive conditional price and compensated martingale condition.

2. Validate lambda=0 against BSM and mixture against MC.

3. Vary one jump parameter at a time, holding total variance fixed; invert prices to implied vol.

4. Measure ATM level, finite-difference skew and OTM put premium across maturities, report inversion failures.

5. Compare left and right jump asymmetry and high-intensity small-jump limiting cases with uncertainty bounds.

## Required exhibits

Price/IV curves by maturity; skew heatmap; matched-variance table; mixture truncation and MC diagnostic.

## Robustness

Use Q rather than historical jump estimates for pricing; matching log variance does not match higher moments or option prices. Check no-arbitrage bounds and negligible wing vega. Distinct from D01.01.02 (hedging misspecification).

## Minimum viable thesis

Compensated mixture, independent MC, matched-variance BSM and three jump scenarios over three maturities, with error checks.

## Optional extension

Contrast Heston and jump-diffusion under matched ATM term structure; test identifiability on synthetic quotes.

## Prerequisites

BSM, Poisson processes, numerical integration, Python.

## Thesis outline

1. Diffusion and jump risk;

2. Risk-neutral mixture;

3. Numerical verification;

4. Smile comparative statics;

5. Limits.

## Milestones

W1-3: derive model; W4-6: implement mixture/MC; W7-9: implied vol and controls; W10-12: maturity and jump grid; W13-16: robustness and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
