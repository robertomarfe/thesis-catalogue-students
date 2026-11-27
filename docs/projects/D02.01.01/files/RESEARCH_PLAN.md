# Research plan | D02.01.01

## Study design and independent work

Do not begin an empirical claim before the source vintage and use permission pass. Freeze the -5% event and chronological split; retain all missing labels, compare common origins and discuss event scarcity rather than adjusting the threshold after inspection.

## Required tasks

1. Document methodology vintage, release dates and daily/monthly alignment; plot SKEW, VIX and downside events.

2. Estimate in-sample nested logit models and interpret marginal effects, not causal effects.

3. Expanding-window forecasts with fixed models; compare Brier/log score and calibration against VIX and base rate.

4. Report block-bootstrap intervals and event counts, especially in test years.

5. Repeat with threshold -3%, quantile regression and post-launch sample; separate methodology versions if both available.

## Required exhibits

Data audit, index correlation and event plot, coefficient and forecast-score tables, calibration curve and event-count table.

## Robustness

The October 5, 2026 Cboe consultation proposed methodology changes and a restated history from 2013; confirm final decision before download. Do not splice legacy and new histories or treat back-calculated values as contemporaneous observations. FF market return is a proxy for SPX. Rare events limit statistical power; no significant incremental effect required.

## Minimum viable thesis

One consistently defined licensed skew series, VIX and market proxy; documented event count and chronological score comparison. If unavailable, simulate Gaussian and asymmetric Q mixtures with P tail scenarios, label exercise as non-empirical and obtain supervisor approval for redesign.

## Optional extension

If lawful strike-level option data become available, compare third-moment index with fixed-delta skew on matched expiries.

## Prerequisites

Option pricing, logistic regression, probability, time-series validation and Python.

## Thesis outline

1. Risk-neutral moments and skew;

2. Index definitions and data;

3. Tail-event forecast design;

4. Incremental information and robustness;

5. Limits and conclusions.

## Milestones

W1-3: validate index history and theory; W4-6: align returns and audit events; W7-9: estimate nested models; W10-12: chronological scores and robustness; W13-16: interpret and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
