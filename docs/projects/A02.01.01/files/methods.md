---
title: Focused methods note | A02.01.01
---

**Focused methods / A02.01.01**

## 1. Economic motivation and forecast timing

The log-linear present-value identity relates the dividend-price ratio to discounted future returns and dividend growth, plus a terminal term. It does not establish that either ratio forecasts excess returns in finite samples. Define monthly origins $t$ and target completion dates $e=t+1$. The conservative admissible estimation set is

$$\mathcal I_t=\{s:s<t,\ e_s<t,\ x_s,y_s\ \text{observed}\}.$$

Use this same set for the mean benchmark and OLS. At a forecast origin, $x_t$ must be available; the strict label rule alone does not establish predictor availability. Earnings-release lags require a separate data audit. For a 240-month window add $s\geq t-240$. Do not replace missing calendar months with adjacent rows.

## 2. Evaluation

Let $y_t=r^e_{t+1}$, $f_t$ be the fitted forecast and $b_t$ the historical mean. Over the same complete evaluation origins $\mathcal T$,

$$R^2_{\mathrm{OS}}=1-\frac{\sum_{t\in\mathcal T}(y_t-f_t)^2}{\sum_{t\in\mathcal T}(y_t-b_t)^2}.$$

The cumulative gain uses $d_t=(y_t-b_t)^2-(y_t-f_t)^2$. Positive values favor the regression. Never use a full-sample mean or standardization. Negative $R^2_{\mathrm{OS}}$ does not invalidate a research design.

\newpage

## 3. Inference and robustness

For nested forecast models the Clark--West adjusted loss differential is

$$d_t^{CW}=d_t+(f_t-b_t)^2.$$

Distinguish its one-sided comparison from the raw loss differential, an in-sample HAC $t$-statistic, and a claim of population economic predictability. A paired date-block bootstrap of fixed forecasts addresses score variability but not all re-estimation uncertainty. Longer-horizon returns require compounding total-return and bill legs separately, and overlapping target dependence.

## 4. Implementation contract

| Symbol | Implementation | Convention |
|:--|:--|:--|
| $t$ | `origin` | integer calendar month |
| $e_t$ | `end` | target completion month |
| $y_t$ | `target` | decimal excess return |
| $x_t$ | predictor column | known at origin |
| $f_t,b_t$ | forecasts | same training and test dates |

The student's notebook must build data validation, recursive forecasting, loss evaluation and robust inference. Retain the exact source vintage and unit conversion; document the release lag and all rejected observations. No empirical inputs or estimated coefficients are supplied.
