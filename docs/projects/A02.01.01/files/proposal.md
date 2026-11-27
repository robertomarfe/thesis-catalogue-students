---
title: Can Valuation Ratios Predict the Equity Premium?
---

**A02.01.01 / Asset pricing / Empirical / Difficulty 2/3 / 16 weeks / Data gate: pending**

Current research proposal. Not approved for assignment.

## Motivation

Equity prices summarize both expected cash flows and the rates used to discount them. A high dividend-price ratio may therefore signal a higher expected equity premium, weaker expected dividend growth, or both. Estimating that relation in historical data is not enough: investors must form forecasts without future information. This project asks whether valuation ratios add predictive information beyond a recursively estimated historical mean and whether that gain survives changes in the sample.

## Research question

Can lagged dividend-price and earnings-price ratios improve monthly US equity excess-return forecasts over the historical mean, and is their performance stable across decades? Assess whether the gains remain after accounting for parameter uncertainty and timing conventions.

## Model and economic intuition

Let $r^e_{t+1}=R^{\mathrm{tot}}_{t+1}-R^f_{t+1}$ denote next month's simple excess return (both legs expressed as decimal returns). Define the predictor $x_t$ using the dividend-price or earnings-price ratio available at the forecast origin. Estimate

$$r^e_{t+1}=a+b x_t+u_{t+1}.$$

Persistent predictors and correlated innovations may distort conventional in-sample inference. A chronological forecast evaluates a different question: whether parameter estimation improves future predictions. Use a common information cutoff for the regression and historical-mean benchmark; a conservative extra lag for earnings probes availability risk.

## Data and research design

Use the GW/GWZ monthly workbook from Amit Goyal, targeting 1927--2025 subject to actual common coverage. Train initially through 1964 and evaluate from 1965; a revised-data exercise is pseudo-out-of-sample, not real-time. Validate the return definition, risk-free rate, predictor construction and release timing before freezing origins. A 20-year rolling window is a prespecified alternative to expanding estimation.

\newpage

## Applied research programme

1. Audit variable definitions, month identifiers and release assumptions; retain missing observations as missing.
2. Estimate the two in-sample regressions separately; report HAC intervals and predictor persistence.
3. Produce expanding forecasts and historical-mean forecasts on identical origins; repeat with a fixed 240-month rolling window.
4. Report out-of-sample $R^2$, cumulative squared-error gains, Clark--West adjustment in the nested setting, block uncertainty and predeclared subperiods.
5. Explain economic magnitude and instability; compare the extra earnings lag without selecting the best lag on the test set.

## Deliverables and acceptance

Data dictionary and coverage; in-sample coefficients; chronological forecasts; cumulative loss gains; common-origin OOS score and subperiod tables; lag sensitivity. Weak predictive evidence is a valid result. Optional: constrained timing rule with predeclared risk aversion and costs.

**Minimum viable thesis.** Two predictors, one historical-mean benchmark, correctly lagged chronological forecasts, OOS R2 and uncertainty, and an explanation of weak/unstable or strong performance. No requirement to beat the historical mean.

## Work plan

Weeks 1--3: theory and source review; 4--6: data or numerical setup; 7--10: core implementation; 11--13: robustness; 14--16: writing and replication. Preserve the more detailed canonical milestones.

## Core reading

Campbell and Shiller (1988); Goyal and Welch (2008); Goyal, Welch and Zafirov (2024); Clark and West (2007). Use the inherited reading guide for exact metadata and consult the papers before citing their claims.
