# Research plan | A06.03.02

## Study design and independent work

Normalize two positive cash-flow profiles to identical PV, confirm weights sum to one and analytic duration/convexity via central differences at multiple step sizes. Compare parallel/nonparallel shifts and explicit changed cash-flow scenario; test 50/100y truncation. Historical evidence is optional; no claim about observed growth/value beta without matched data.

## Prespecified implementation

Use c_j profiles exactly as proposal and continuous discount convention y=.08; scale to same initial PV, report duration=sum j*w_j and convexity=sum j^2*w_j. 50/100-year truncation, finite changes, nonparallel shifts, reprice growth revisions explicitly; no infinite terminal unless g<discount convention. FF25M/FF3/GSW optional illustration requires actual data. Separate theoretical rate derivative at fixed cash flow from descriptive return-rate beta.

## Required tasks

1. Derive duration and convexity; verify finite differences and cash-flow weights sum to one.

2. Compare price sensitivity at matched baseline P, vary transition horizon and terminal growth with finite price restrictions.

3. Decompose sensitivity across cash-flow maturity buckets and nonparallel curve shocks.

4. If files acquired, estimate descriptive growth/value return betas on yield changes, HAC and rolling stability; keep market-control results separate from raw exposure.

5. Introduce illustrative growth revisions offsetting a rate rise; demonstrate nonidentification of cash-flow duration from observed return beta.

## Required exhibits

Cash-flow and PV profiles, duration/convexity table, rate-shock plots, optional portfolio exposure estimates and interpretation.

## Robustness

Stylized DDM is not estimated firm cash flow or equity strip data. Treasury yield changes are not pure discount-rate shocks; growth news and risk premia may co-move. High/low BM portfolios are proxies for investment styles. Avoid treating rate beta as structural duration.

## Minimum viable thesis

Two matched-price cash-flow profiles, analytic/numerical sensitivity and offsetting-news experiment. Historical evidence is optional S-class extension, explicitly distinguished from theory. Distinct from A06.01.01 valuation ratios and A06.02.01 strip data.

## Optional extension

Use GKK model-implied style equity curves to compare cash-flow timing under additional assumptions.

## Prerequisites

Discounted cash flow, duration, numerical derivatives, regression for optional evidence.

## Thesis outline

1. Equity cash-flow timing;

2. Duration and DDM;

3. Controlled profiles;

4. Sensitivity and optional evidence;

5. Identification limits.

## Milestones

W1-3: derive sensitivity; W4-6: build and validate profiles; W7-9: parallel/nonparallel shocks; W10-12: news scenario and optional data; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
