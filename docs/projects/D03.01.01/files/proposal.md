---
title: Forecasting Equity Market Volatility — GARCH versus Historical Volatility
subtitle: 'Research proposal | D03.01.01'
---
**Derivatives · Volatility forecasting · 16 weeks · Level 2/3**  
**Data:** US daily market returns; input validation pending. **Status:** current draft; not approved for assignment.

## Motivation

Volatility clusters in equity markets: large price movements tend to be followed by large movements, regardless of their sign. A conditional volatility model is useful only if it forecasts future risk more accurately than a simple historical benchmark. This question matters for risk limits, margin and derivative applications. The object here is physical-measure return variance, not the risk-neutral volatility embedded in option prices.

## Research question

Does GARCH(1,1) improve genuinely out-of-sample forecasts of daily and 21-trading-day market variance relative to rolling historical variance? Is the ranking stable in high- and low-volatility periods?

## Model and economic mechanism

Let $u_t$ be the daily log-return innovation under a predetermined mean convention and $h_{t+1|t}=\operatorname{Var}(u_{t+1}\mid\mathcal F_t)$, where $\mathcal F_t$ is information available after day $t$. The GARCH recursion is
$$h_{t+1|t}=\omega+\alpha u_t^2+\beta h_{t|t-1}.$$
Require $\omega>0$, $\alpha,\beta\ge0$ and $\alpha+\beta<1$. The unconditional variance is $\bar h=\omega/(1-\alpha-\beta)$. Conditional forecasts revert to this level at rate $\alpha+\beta$. Under conditionally uncorrelated innovations, cumulative expected variance over $H$ future trading days is the sum of the individual forecasts. Evaluate it against $Y_{t,H}=\sum_{j=1}^H u_{t+j}^2$. This proxy is noisy; it is not intraday realized variance.

## Data and chronological design

Use the US daily Fama/French three-factor file. Construct the total market simple return from `Mkt-RF` plus `RF`, converting percentages to decimals exactly once; take $\log(1+R_t)$ where defined. Preserve the downloaded vintage, remove missing sentinel observations only according to a documented rule and never insert zero returns on missing dates. Target 1990–2025, subject to file inspection. Use 1990–2004 as initial estimation and 2005–2025 for sequential evaluation. Compare 21- and 252-day rolling historical variance with Gaussian QML GARCH estimated over a five-year rolling window, refitted monthly and filtered daily. Fix the forecast origin and use only outcomes available at that time.

\newpage

## Research tasks and deliverables

1. Acquire and validate the daily file. Plot returns, squared returns and their autocorrelations; examine ARCH diagnostics and declare the mean and trading-calendar conventions.
2. Fit the model on past observations only; record optimizer failures, stationarity and persistence. Include constant and rolling-variance benchmarks.
3. Construct forecasts at horizons 1 and 21, matching the sum of future squared innovations on a common evaluation sample. Score each model by QLIKE, MSE and forecast bias, declaring any variance floor.
4. Compare losses using HAC inference or a block bootstrap. Report nonoverlapping 21-day dates as a robustness check and use lagged information to define volatility regimes. Vary window and refit frequency, investigate 2008 and 2020 without selecting samples by outcomes, and report the economic magnitude of improvement.

Deliverables: data-quality and autocorrelation summaries, parameter and persistence table, dated forecast/proxy plots, loss and uncertainty comparisons by horizon and regime, convergence and failure report. No model is required to win.

## Minimum viable thesis and acceptance criteria

One clean daily series; rolling historical and GARCH forecasts at both horizons on a common evaluation sample; QLIKE and MSE, uncertainty-aware loss comparisons, and honest treatment of noisy targets. No requirement that GARCH wins.

## Research plan and scope

| Weeks | Deliverable |
|:--|:--|
| 1–3 | Acquire file, review GARCH and scoring |
| 4–6 | Validate targets and historical benchmarks |
| 7–10 | Estimate, refit and forecast chronologically |
| 11–13 | Loss comparisons, uncertainty and regimes |
| 14–16 | Reproducibility, interpretation and writing |

Prerequisites: time-series econometrics, maximum likelihood, Python and data handling. Optional extension: EWMA, GJR-GARCH or Student-t innovations; VIX is a distinct risk-neutral predictor requiring horizon matching. No empirical results are supplied; evaluate the model comparisons on authorized data.

## Core reading and source

Bollerslev (1986), *Journal of Econometrics*, 31, 307–327.  
Andersen and Bollerslev (1998), *International Economic Review*, 39, 885–905.  
Patton (2011), *Journal of Econometrics*, 160, 246–256.  
[French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Use the supplied FF3D source recipe; inspect rights, dates and columns before assignment. Full-text literature review remains pending.
