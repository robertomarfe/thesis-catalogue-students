# Research plan | A09.02.01

## Study design and independent work

Before estimation verify outright versus points, quote orientation, fixing and outcome dates; audit rights and actual coverage. Do not splice observed and synthetic forwards or infer G10 carry from a bilateral regression.

## Required tasks

1. Verify units/quote direction, settlement dates, series discontinuation and matched month-end data; compute forward premium and log proxy.

2. Estimate Fama regression with HAC intervals for b=1 and a=0; compare random-walk spot forecast with forward and regression forecast in a fixed chronological split (train first 60%, evaluate last 40%).

3. Check algebra of excess-return slope; report changes across predeclared 1990-2007 and 2008-2021 windows and finite-sample persistent-regressor uncertainty.

4. For G10 published carry baskets, compute high-minus-low returns with provider's return convention, annualized mean/volatility, crash episodes and gross/net comparison.

5. Explain why bilateral UIP results do not identify cross-sectional carry premia; compare on common dates and report turnover/cost limitations.

## Required exhibits

Quote/timing audit, Fama regression and forecast tables, forward-premium and spot plots, carry summary and downside diagnostics.

## Robustness

Do not extend actual-forward sample using synthetic forwards silently. Historical BoE midquotes are not executable returns, exact value dates may differ from month-end. Published baskets do not disclose underlying individual quotes; do not reconstruct them from portfolio returns. Log approximations and Jensen terms matter, inference low power for persistent premia.

## Minimum viable thesis

One actual spot-forward pair with verified common history and UIP regression; published G10 carry gross panel or explicitly conditional fallback. If core source fails, redesign title/application with supervisor. Distinct from D10.03.01 synthetic CIP pricing.

## Optional extension

Acquire additional historical BoE currency forward pairs if present, or approved academic panel with individual forward quotes; estimate pooled UIP and cross-sectional decompositions.

## Prerequisites

International finance, exchange-rate conventions, predictive regression and Python.

## Thesis outline

1. CIP, UIP and currency payoffs;

2. Observed quotes and portfolio data;

3. Bilateral regression;

4. Carry evidence and comparison;

5. Limitations.

## Milestones

W1-3: verify quotes, rights and theory; W4-6: align bilateral and carry data; W7-9: UIP and forecast; W10-12: carry analysis and robustness; W13-16: interpretation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
