---
title: Focused methods note | A04.03.01
---

**Focused methods / A04.03.01**

## 1. Event and unit definitions

A valid key is $(\text{meeting},\text{window},\text{start UTC},\text{end UTC})$. Check uniqueness and the documented 30- or 70-minute length. Preserve the raw rate and equity units before normalizing. A change of 0.0025 in a decimal rate equals 25 basis points; an equity decimal return of 0.01 equals 1 percent.

For a window-specific regression $y_e=\alpha+\beta s_e+u_e$, the coefficient has units of decimal equity return per basis point. Report $100\times25\hat\beta$ as the estimated percent equity response to a 25-bp surprise. Scale confidence limits in the same way.

## 2. Paired meeting design

For meetings containing both windows define $D_e=1$ for a conference and zero for a statement. Estimate

$$y_e=\alpha+\beta s_e+\eta D_e+\delta D_e s_e+u_e.$$

The statement slope is $\beta$, the conference slope is $\beta+\delta$. Cluster by meeting date; this accounts for dependence between the two observations of the same meeting. A regression on every observed statement is a different sample from a matched-pair regression. Report both sample definitions.

\newpage

## 3. Identification and reporting

Use a surprise constructed without the same equity return being explained. A surprise may combine policy and central-bank information, even in a short window. Conditioning on the sign of the equity response and then estimating that response is mechanically endogenous. Treat rate-only regressions as conditional associations unless a separately justified structural identification strategy is available.

## 4. Data contract

| Variable | Code field | Unit |
|:--|:--|:--|
| Event date | `meeting` | provider date |
| Event type | `window` | statement/conference |
| Interval | `start`, `end` | UTC timestamp |
| $s_e$ | `surprise_bp` | basis points |
| $y_e$ | `equity` | decimal return |

Record the exact data release and hash after authorized acquisition. Verify coverage, labels and signs against provider documentation; no forward fills or unrecorded drops. Use HC3 for separate-window regressions, meeting clusters for paired observations and small-sample sensitivity. No empirical response estimates are supplied.
