---
title: "Global versus Regional Equity Factor Models"
subtitle: "Research proposal | A09.01.01"
---

**Asset pricing · International finance, FX and commodities · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Investors can hold portfolios across developed equity markets, but global factor exposures need not explain local average returns equally well. Comparing global and local models on identical test assets isolates differences in empirical pricing performance without equating those differences with market segmentation.

## Research question

Do developed-market factors price regional equity portfolios as effectively as regional factors? Is the incremental explanatory or pricing power of local factors stable across regions and sample periods?

## Economic mechanism

For the same regional asset $i$, compare $R^e_{i,t}=\alpha_i+\beta_i^\top f_t+\epsilon_{i,t}$ using global or regional factors $f_t$.

## Research design

Construct the prescribed USD-denominated regional portfolios and Developed and regional FF3 factors. Match asset sets, dates and risk-free return, estimate equal-dimensional global and local specifications, and assess paired alpha and fit differences across regions and subsamples.

Audit identical USD units and RF, dates, portfolio definition and factor count. Report N, T, K, covariance conditioning and paired uncertainty. Separate factor-construction overlap from the economic interpretation.

\newpage

## Required exhibits

Regional factor correlation matrix, alpha heatmaps, benchmark comparison by region, joint-test and incremental-factor tables, paired uncertainty intervals, documented common-currency sample.

## Minimum viable thesis

Two or more verified regional portfolio panels plus developed/region FF3; matched USD excess returns, global/local alpha and fit comparisons, joint or dependence-aware tests, and careful interpretation of overlap and integration.

## Scope and feasibility

Use identical asset sets/dates and number of factors in primary comparisons; disclose portfolio-factor construction overlap, regional size breakpoints and global factor inclusion of tested region. GRS may be invalid for near-redundant portfolios; shrink test set transparently or report bootstrap inference. Integration is not identified by alpha differences alone; currency risks may be omitted.

**Prerequisites:** CAPM, FF factors, multivariate OLS, hypothesis testing and Python.

**Optional extension:** Add FF5 or currency factors and a formal partial-integration model, only after checking test assets and sample compatibility.

## Milestones

W1-3: theory and exact data gate; W4-6: align factor and asset panels; W7-10: estimate matched models and tests; W11-13: overlap, rank and subperiod robustness; W14-16: write and reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
