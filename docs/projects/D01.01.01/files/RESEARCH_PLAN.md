# Research plan | D01.01.01

## Study design and independent work

Separate each input perturbation from a change in the terminal law. Hold other inputs fixed for Greeks; for the mixture preserve the forward and arithmetic second moment at every maturity. Report units and distinguish small perturbations from scenario repricing.

## Required tasks

1. Derive BSM and implement prices and Greeks with explicit rate/dividend units.

2. Check put-call parity, limiting cases and centered finite-difference Greeks at multiple step sizes.

3. Plot price and Greek surfaces across strikes and maturities; identify where vega and gamma concentrate.

4. Hold forward and terminal second moment fixed and compare mixture versus BSM prices and implied volatility.

5. Rank economically meaningful scenario price changes in dollars per share and implied-vol points; distinguish local Greeks from nonlinear changes.

## Required exhibits

Price and Greek maps, analytical-versus-numerical error table, sensitivity and mixture smile panels, documented Python functions and fixed parameter grid.

## Robustness

Use at least two maturities and volatility regimes; handle near-expiry limits separately rather than dividing by zero. Validate parity and bounds for both distributions. Do not infer a market pricing error, realistic probabilities or dynamic mixture hedge performance.

## Minimum viable thesis

BSM derivation and validated implementation, four input sensitivity experiments, one controlled non-lognormal comparison and an economic interpretation of the observed differences.

## Optional extension

Repeat the terminal experiment using a compensated jump-diffusion with an independent price reference; keep the main thesis distinct from empirical Heston calibration.

## Prerequisites

Probability, basic stochastic calculus, derivatives pricing and Python NumPy/SciPy. No external quotes required.

## Thesis outline

1. Replication and no-arbitrage;

2. BSM and Greeks;

3. Controlled scenario design;

4. Input and distributional sensitivity;

5. Interpretation and limitations.

## Milestones

W1-3: derive pricing and sensitivities; W4-6: implement and test BSM; W7-9: run parameter grids; W10-12: build matched-moment mixture and diagnostics; W13-16: interpret and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
