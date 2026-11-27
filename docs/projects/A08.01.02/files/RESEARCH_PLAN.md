# Research plan | A08.01.02

## Study design and independent work

Document shrinkage target, intensity and denominator; compare eigenvalues, condition numbers, KKT, weights and predicted risk on common origins. Same costs and drift, equal weight and sample GMV; report singular windows and predefined fallback, compare paired net OOS variance/turnover and block intervals.

## Prespecified implementation

Use value-weighted 30 industries, fixed complete asset universe justified ex ante, common first test date after 120 months. Compare sample covariance (ddof=1) and sklearn LedoitWolf (ML scaling, identity shrinkage target), note scaling difference does not affect unpenalized GMV weights. Verify positive definiteness; if sample covariance singular report and apply declared ridge sensitivity, not silent pseudoinverse. Use monthly 60/120 lookbacks, identical EW, GMV constraints, ledger scale=1; report covariance eigenvalues, condition numbers, concentration and paired realized squared-return/variance differences; full re-fit bootstrap sensitivity.

## Required tasks

1. Validate sample covariance, LW shrinkage and QP solution on synthetic examples; check symmetry, PSD and weights.

2. Compute rolling GMV for sample and shrunk estimates and 1/N under identical constraints; store forecasts, weights and subsequent realized return separately.

3. Compute net returns with drift-adjusted turnover, annualized volatility, mean, Sharpe (consistent RF), drawdown and effective number of assets 1/sum(w_i^2). Compare realized variance via paired block bootstrap and report condition numbers and concentration.

4. Relate performance to N/T and cost assumptions, compare lookbacks and predeclared stress subperiods; evaluate whether lower estimated risk transfers to lower realized risk.

## Required exhibits

Rolling condition numbers and shrinkage intensity; weight-concentration chart; cumulative net wealth, drawdown and volatility plots; risk/turnover/Sharpe table with bootstrap differences; cost and lookback sensitivity. Explain why equal weighting is a demanding benchmark and not a straw man.

## Robustness

Do not invert singular covariance silently: solve constrained QP, document numerical ridge only as separate benchmark. Keep identical asset universe, constraints and OOS sample; include initial allocation costs consistently or state exclusion. Do not use future returns in covariance estimates or choose cost rate by performance. Industry portfolios are published research portfolios, not directly tradable funds; backtest ignores implementation frictions beyond stylized costs.

## Minimum viable thesis

Long-only GMV using sample and Ledoit-Wolf covariance plus equal weight, chronological backtest, two lookbacks, risk and turnover metrics, and a cost sensitivity table. Weak shrinkage gains remain a valid result.

## Optional extension

Compare alternative shrinkage targets or exponentially weighted covariance, or use a small verified ETF universe with explicit data availability; no need to estimate expected returns.

## Prerequisites

Matrix algebra, covariance estimation, optimization, portfolio return arithmetic, Python/SciPy/scikit-learn. No stock-level histories needed.

## Thesis outline

1. Portfolio choice and estimation error;

2. GMV and shrinkage theory;

3. Data, constraints and backtesting design;

4. Risk, weights and performance;

5. Sensitivity and practical limitations.

## Milestones

W1-3: derive GMV and shrinkage, download industries; W4-6: validate data and QP/backtest accounting; W7-10: run rolling comparison with frozen choices; W11-13: bootstrap risk, costs and concentration; W14-16: write and reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
