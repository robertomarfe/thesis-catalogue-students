# Research plan | D09.02.01

## Study design and independent work

Report survival curves and repricing residuals in basis points. Compare alternative recovery at fixed quotes, rather than relabeling the physical hazard. Retain infeasible noisy cases and disclose the objective and penalty.

## Required tasks

1. Derive survival, expected recovery and par spread; verify constant-hazard continuous result s=(1-R)lambda.

2. Generate synthetic spreads with quarterly accrual-on-default and bootstrap; check repricing and hazard recovery.

3. Plot Q cumulative default and survival; compare bond term structures using recovery of par.

4. Change recovery and spread noise; report infeasible negative hazard cases and constrained residuals.

5. Compare exact integration and coarse payment-grid approximations; show recovery-hazard identification sensitivity.

## Required exhibits

Hazard, survival and bond-spread curves; CDS repricing table; recovery/noise sensitivity and infeasibility diagnostics.

## Robustness

Do not silently clip negative hazards while claiming exact fit. CDS accrued premiums, payment schedule and discounting must be consistent. Q survival is not physical default forecast; spread is not pure expected loss in real markets.

## Minimum viable thesis

Synthetic four-bucket bootstrap, constant hazard check, repricing and recovery sensitivity with explicit convention. Distinct from structural default projects D09.01.

## Optional extension

Stochastic intensity CIR with conditional survival transform; compare synthetic term structures.

## Prerequisites

Discounting, probability, numerical root finding, credit-risk basics.

## Thesis outline

1. Intensity and survival;

2. CDS and bond pricing;

3. Bootstrap algorithm;

4. Sensitivity and identification;

5. Conclusions.

## Milestones

W1-3: derivations; W4-6: integration and CDS generator; W7-9: bootstrap; W10-12: stress and bond prices; W13-16: documentation.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
