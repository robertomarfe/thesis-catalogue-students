# Research plan | D01.03.03

## Study design and independent work

Predeclare gamma caps and fallback before comparing stress scenarios. Use matched paths, initial capital and funding; report ES uncertainty and the frequency of constrained positions, including the no-jump subset.

## Required tasks

1. Validate jump compensator and series prices against MC and lambda=0 BSM.

2. Derive and test self-financing ledgers, common initial wealth and terminal payoffs.

3. Compare BSM delta, Merton delta and delta-gamma policies, with predeclared cap/fallback for small secondary gamma.

4. Estimate mean, RMSE, 95% ES and paired loss differences under baseline and stress P.

5. Separate no-jump from jump paths, report hedging frequency and trading cost sensitivity.

## Required exhibits

Jump residual versus size, hedge error distributions and tail tables, paired bootstrap intervals, turnover and stress loss decomposition.

## Robustness

Stress is a stipulated scenario not a calibrated market disaster probability. Gamma matching is local, secondary option has its own jumps and transaction costs; compare common caps and capital, disclose rare-tail uncertainty. Distinct from D01.03.01, which emphasizes pricing and diffusion/jump identification.

## Minimum viable thesis

Merton pricing reference, common-path delta versus capped delta-gamma hedge under two P scenarios with ES uncertainty and funding checks.

## Optional extension

Choose hedge ratios by conditional squared jump residual or training-sample ES; freeze policy before independent tests.

## Prerequisites

Option Greeks, jump diffusion, portfolio accounting, Monte Carlo, ES.

## Thesis outline

1. Gap risk and replication;

2. Q pricing and P stress;

3. Hedge construction;

4. Tail-loss comparisons;

5. Practical constraints.

## Milestones

W1-3: jump model and hedge algebra; W4-6: benchmark/ledger; W7-9: simulation; W10-12: tail and costs; W13-16: dissertation.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
