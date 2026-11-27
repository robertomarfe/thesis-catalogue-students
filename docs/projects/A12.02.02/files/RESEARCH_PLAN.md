# Research plan | A12.02.02

## Study design and independent work

Pin actual sentiment workbook and matching eight OSAP signals/dictionary, state definition and fixed selection. Use lagged states and common months, show alpha=a+c*z and beta interactions, joint date-block uncertainty with familywise/FDR sensitivity and predeclared regime robustness. No data substitution without supervisor approval.

## Prespecified implementation

Pin OSAP long-short and SignalDoc revision, preselect 8-12 signals by valuation/profitability/issuance/investment metadata before viewing outcomes. Baker–Wurgler SENTIMENT.xlsx author-linked; page snapshot here lists 196507-202312, frozen proposal says through Dec 2025: pin actual downloaded version and report shortened coverage, not infer missing 2024-25. Choose raw or orthogonalized series before results; minimum two-month lag and expanding past-only standardization, revised not real-time. FF3/5+Mom common sample, interactions in alpha and betas, joint calendar inference with multiplicity; no RF subtraction for long-short. No stock-level sorting from published factor series.

## Required tasks

1. Audit signal orientation, sample and index timing; register hypotheses and signs.

2. Compare unconditional and sentiment-sorted returns using past-only median thresholds.

3. Estimate conditional alpha regressions with FF3 and FF5+momentum.

4. Use common date block bootstrap, adjust multiple tests and report joint and individual effects.

5. Compare raw and orthogonalized sentiment and alternative lags; evaluate stable sign and magnitude in later subsample.

## Required exhibits

Signal selection log; conditional return plots; regression and joint inference table; lag/subsample sensitivity.

## Robustness

Do not use full-sample median for a trading rule or changes in revised sentiment as real-time innovations. Factor adjustment does not identify mispricing; account for correlated strategies, sample selection and revised data.

## Minimum viable thesis

Eight named portfolios, documented sentiment version, unconditional and conditional factor regressions, common-sample inference.

## Optional extension

Analyze cross-sectional heterogeneity by independently defined limits-to-arbitrage categories, not by selecting extreme estimated coefficients.

## Prerequisites

Factor regressions, bootstrap, financial econometrics, Python.

## Thesis outline

1. Sentiment and limits to arbitrage;

2. Conditional factor models;

3. Data and hypotheses;

4. Results and inference;

5. Interpretation.

## Milestones

W1-3: literature and data gate; W4-6: sample and hypotheses; W7-9: conditional models; W10-12: inference/robustness; W13-16: replication and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
