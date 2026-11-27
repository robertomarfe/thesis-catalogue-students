---
title: Conditional variance forecasting — timing and evaluation
subtitle: 'Focused methods supplement | D03.01.01'
---
**Empirical design · Daily log returns · Variance in decimal squared units**

## 1. Forecast objects and recursion

Let $\mathcal F_t$ contain observations through trading day $t$. The return innovation $u_t$ is the log return minus the predetermined mean. For GARCH(1,1), write $h_{t|t-1}$ for the one-step conditional variance used when evaluating $u_t$. Gaussian QML minimizes the mean of
$$\ell_t(\omega,\alpha,\beta)=\tfrac12\left[\log h_{t|t-1}+u_t^2/h_{t|t-1}\right]$$
over the current training window. Reinitialize the filter at $\bar h=\omega/(1-\alpha-\beta)$ under the stated initialization convention and disclose the initialization. Require positive variance, nonnegative coefficients and persistence strictly below one. The fitted parameters are held fixed between declared refit dates, but the conditional variance incorporates each newly observed innovation.

At origin $t$ the first forecast is $h_{t+1|t}=\omega+\alpha u_t^2+\beta h_{t|t-1}$. Define $p=\alpha+\beta$. The $j$-step forecast and aggregate forecast are
$$h_{t+j|t}=\bar h+p^{j-1}(h_{t+1|t}-\bar h),$$
$$f_{t,H}=\sum_{j=1}^H h_{t+j|t}=H\bar h+(h_{t+1|t}-\bar h)\frac{1-p^H}{1-p}.$$
For a rolling historical window of length $w$, use
$$f^{\mathrm{hist}}_{t,H}=\frac{H}{w}\sum_{i=0}^{w-1}u_{t-i}^2.$$
Both are forecasts of a sum in **daily variance units**. Do not compare a daily forecast with annualized volatility, or 21 trading days with exactly 30 calendar days. A constant-variance benchmark can use a fixed training estimate.

## 2. Information and target maturation

For each origin $t$ record the training end date, refit identifier, horizon $H$, prediction and target end date $t+H$. The evaluation proxy is $Y_{t,H}=\sum_{j=1}^H u_{t+j}^2$; it is unavailable until $t+H$. Retain only common, mature outcomes for all compared forecasts. To set regimes or tune parameters, use information already available at the forecast origin, never the realized future proxy. Nonoverlapping 21-day origins address a separate dependence issue; they do not remove all serial dependence.

\newpage

## 3. Forecast comparison

For positive forecast $f$ and nonnegative proxy $Y$, define
$$L_{QL}(Y,f)=\log f+Y/f,\qquad L_{MSE}(Y,f)=(Y-f)^2.$$
QLIKE may be negative because of the log term. Smaller loss is better. Compare on identical origins within each horizon; the level of QLIKE is not comparable across differently scaled targets. The validity of relative loss comparisons with imperfect proxies requires suitable conditional unbiasedness assumptions. For loss difference $d_t=L_{QL}(Y_t,f_t^G)-L_{QL}(Y_t,f_t^H)$, negative mean favors GARCH. Use HAC or a block bootstrap to account for serial dependence (especially overlapping 21-day targets); declare bandwidth or block size and report uncertainty. The pilot's small artificial sample is not an inferential demonstration.

## 4. File acceptance and implementation

Download `F-F_Research_Data_Factors_daily_CSV.zip` from the [provider's exact file link](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip). Provider metadata was checked in the prior source audit; this release has not downloaded or inspected the raw file. Keep a local copy and record its hash and vintage. Run the original workspace's `src/local_preflight.py` and inspect the source recipe. Required columns are date (`YYYYMMDD`), `Mkt-RF`, `SMB`, `HML`, and `RF`, with factor returns in percent per day. Flag sentinel values and duplicate dates; check actual common sample, chronological ordering and positive gross returns before taking logs. Do not redistribute data without authorization.

| Object | Code convention |
|:--|:--|
| $u_t$ | `u` (daily decimal innovation) |
| $h_{t|t-1}$ | `filter_variance(u, p)[t]` |
| $h_{t+j|t}$ | `variance_path(history, p, H)[j-1]` |
| $f_{t,H}$ | sum of forecast path or `historical` |
| $Y_{t,H}$ | `labels(u, H)[t]` |
| $L_{QL}$ | `qlike` (declared positive forecast floor) |

The empirical thesis retains the 1990–2025 design, five-year rolling fit and monthly refits. The student must validate real input, specify mean treatment, handle actual calendar and sample issues, and conduct uncertainty-aware empirical comparisons.
