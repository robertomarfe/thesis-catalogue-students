# Research plan | D04.04.01

## Study design and independent work

The student develops the network, objective, ledger and complete comparison. Report tail loss, turnover, risk objective and stability; in-sample improvement alone is insufficient.

## Required tasks

1. Validate discounted self-financing ledger and BSM delta benchmark.

2. Train network at fixed eta and cost using minibatch stable loss; select checkpoint on validation paths.

3. Tune band and calendar benchmark on same validation sample; freeze all rules.

4. Compare independent test mean loss, SD, ES95, entropic risk and turnover with paired bootstrap.

5. Repeat seeds and stress under changed drift/volatility and jump paths without retuning.

## Required exhibits

Policy slices versus moneyness/position; held-out loss and turnover tables; learning curves; seed sensitivity and stress results.

## Robustness

No future price input; shared information and initial premium; avoid optimizing on test paths. Include liquidation costs, separate model risk and sampling uncertainty. No claim of global optimality or empirical trading performance.

## Minimum viable thesis

One ATM call, GBM, two cost levels, neural vs delta and band, independent test and ledger checks.

## Optional extension

Heston with observable variance or a noisy past-return volatility proxy; separate information advantage from policy advantage.

## Prerequisites

Options, numerical simulation, optimization, basic neural networks and Python.

## Thesis outline

1. Hedging with frictions;

2. Risk objectives and neural policies;

3. Synthetic training;

4. Held-out comparison;

5. Robustness.

## Milestones

W1-3: ledger and risk; W4-6: benchmarks; W7-9: training; W10-12: held-out stress; W13-16: reproducible code and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
