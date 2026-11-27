# Research plan | D08.04.02

## Study design and independent work

Separate single-horizon synthetic choice from historical rolling strategies. Verify equal net wealth, budget and extreme-spot payoff limits; report cost, expected return, tail protection, upside and paired uncertainty.

## Required tasks

1. Derive payoff diagrams and solve budget-constrained strikes/quantities; verify initial wealth identity and realistic upper bound on covered call quantity.

2. Compare expected return, loss probability, VaR and ES, upside participation and terminal stress outcomes versus unhedged stock.

3. Plot efficient frontier of ES versus premium using only prespecified contracts; if choosing an optimal hedge, choose on design sample and report performance on independent paths.

4. Stress implied premiums, jump tails and financing assumptions; report residual exposure below lower put strike and above call strike.

## Required exhibits

Budget/payoff table, terminal wealth and ES distributions, protection-cost frontier, tail stress table, sensitivity to Q-P differences and upside cost. Confidence intervals from simulation replications or independent seed batches.

## Robustness

Use matched initial wealth and feasible quantities, no free arbitrage from pricing choices, common random draws and explicit Q/P separation. Report budget utilization and separate severe scenarios from expected performance. Historical French returns may contextualize physical volatility but cannot establish historical option returns; no actual executable backtest is claimed.

## Minimum viable thesis

Three feasible hedge structures and unhedged benchmark, explicit budget and financing, baseline and jump-tail physical distributions, cost/ES trade-off and limiting cases; results may favor different hedges by criterion.

## Optional extension

Add repeated monthly roll in a fully specified joint P/Q simulation with transaction cost, or public Cboe put-protection benchmark as a separate descriptive comparison after access check.

## Prerequisites

Vanilla option pricing, risk measures, simulation and elementary optimization. No proprietary quotes required.

## Thesis outline

1. Portfolio insurance and tail risk;

2. Pricing, budget and wealth accounting;

3. Physical scenario design;

4. Hedge comparisons and robustness;

5. Economic interpretation.

## Milestones

W1-3: payoff and ES definitions; W4-6: implement pricing and budget constraints; W7-10: run independent scenario comparisons; W11-13: frontier and tail robustness; W14-16: write and reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
