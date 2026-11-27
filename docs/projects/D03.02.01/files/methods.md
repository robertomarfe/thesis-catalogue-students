---
title: "Focused methods — Multi-Horizon Volatility Forecasting with HAR Models"
subtitle: "D03.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Horizon and information set
Define $v_t^{(k)}=k^{-1}\sum_{j=0}^{k-1}u_{t-j}^2$ and $Y_{t,H}=H^{-1}\sum_{j=1}^H u_{t+j}^2$. Direct HAR forecasts $Y_{t,H}$ with regressors $(1,v_t^{(1)},v_t^{(5)},v_t^{(22)})$. At formation $t$, training observation $s$ is eligible only if its label end $s+H\le t$ and the underlying data are available. Never shift a centered rolling average into a predictor.

## Comparable benchmarks
For stationary GARCH(1,1), $E_t[h_{t+j}]=\bar h+(\alpha+\beta)^{j-1}(h_{t+1}-\bar h)$; average across $j=1,\ldots,H$. Use the same demeaning convention for every model. Predetermine a positive training-only floor and record clipping. Use $\ell=\log f+Y/f$ and squared error; target overlap motivates paired HAC or block resampling. Daily squared returns are a noisy variance proxy, not intraday realized variance.

## Research checks

Record the origin, last training label end and target end for each forecast. An average and a sum differ by the horizon; compare only matching units. Report all horizons and null rankings.
