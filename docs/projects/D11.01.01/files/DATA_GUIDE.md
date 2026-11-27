# Data and model setup | D11.01.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Construct three- and five-state economies with a unit bond, stock and optional digital securities. Start with known strictly positive q (sum q=0.98), generate prices from X, then add/remove independent payoff columns. Perturb redundant asset prices to introduce explicit arbitrage and separately test a boundary case with nonnegative but not positive q. Use NumPy SVD and linear programming to maximize epsilon subject to X' q=p and q_i>=epsilon, q>=0. No empirical data.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Construct the required four cases and retain actual portfolio certificates, numerical rank and residuals. Vary collinearity and price perturbations. Keep this theorem-focused project distinct from the claim-specific bounds study.

## Timing, accounting and units

Specify physical versus risk-neutral probability, discounted versus undiscounted cash flows, maturity and year fractions, and whether rates and spreads are decimals, percentages or basis points. Document default timing and recovery. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For finite-state models define the state support, probability mass and numerical tolerance before fitting.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
