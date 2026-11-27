# Research plan | A06.01.01

## Study design and independent work

Manually verify December dates and units; report missing years and log-to-simple growth conversion, iso-P/D contours and required-return/growth pairs. Compare one- and two-stage prices with identical growth limit and terminal share; show sensitivity to horizon and a small joint parameter perturbation. Do not use historical growth as investor forecast without a model.

## Prespecified implementation

Normalize Shiller workbook P,D,CPI using December rows; parse numeric YYYY.MM including .10 as October, maintain missing years. D annual trailing interpolated, P monthly average; use real D and same CPI for P/D. Historical growth scenarios are not survey expectations. DDM uses simple annual growth and required return, k>g; two-stage terminal share and implied k=g+(1+g)/(P/D). Use rolling 20-year contiguous growth, alternative windows and annual payout caveats.

## Required tasks

1. Derive one- and two-stage DDM, validate limiting cases and scale invariance.

2. Plot historical P/D, annual real dividend growth and rolling historical means; report sample construction and payout caveats.

3. Compute valuation surfaces over g and k, e.g. real g -1% to 4%, k 3% to 10%, mask k<=g.

4. For historical P/D quantiles solve implied k over prespecified g scenarios and plot observational-equivalence curves; do not call these estimates of true expected returns.

5. Compare two-stage values for temporary growth shock and permanent shift, report terminal-value shares and percentage valuation effects.

## Required exhibits

Historical ratio and growth figures, admissible valuation heatmaps, iso-P/D curves, two-stage scenarios and economic sensitivity table.

## Robustness

Use nominal rather than real data consistently as separate exercise, compare subperiods and growth window; distinguish dividend growth from total payout growth when buybacks matter. Year-end price is a monthly average proxy. Avoid mixing annual D with monthly return cash flows. Terminal assumption drives results near k=g.

## Minimum viable thesis

Verified historical series, analytical DDM sensitivities, iso-valuation restrictions, one two-stage scenario and explicit nonidentification discussion.

## Optional extension

Add Campbell-Shiller log-linear present-value decomposition or total payout series only after separate acquisition; retain simple DDM as primary.

## Prerequisites

Discounted cash flow, algebra, elementary statistics and Python. Foundation level.

## Thesis outline

1. Present-value valuation;

2. Gordon and multistage models;

3. Aggregate data;

4. Valuation scenarios and growth sensitivity;

5. Identification and limitations.

## Milestones

W1-3: derive DDM; W4-5: historical dataset; W6-9: valuation and implied-rate scenarios; W10-12: multistage and robustness; W13-16: interpretation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
