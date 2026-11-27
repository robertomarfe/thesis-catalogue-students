# Data and model setup | A12.04.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Baseline static cap L_0=L_1=L and finite-horizon reduced-form demand, F=100, beta=1, a=0.5, L=0,1,5,20,unlimited; n0 and eps Gaussian with SD 4 and rho=0,0.5,0.9, 50,000 paths seed 123. Vary a and caps; compare convergence at t=2 (p2=F), p1 changes, terminal self-financing payoff x0*(p1-p0)+x1*(F-p1) before holding cost. Define W0=20 and record negative wealth and constraint-binding rates, not a fully specified funding equilibrium. Optional wealth feedback extension must derive a unique or selected equilibrium.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Distinguish physical growth laws, state-price kernels and traded payoff definitions. Optional external context does not change the synthetic core.

## Frozen research design (original catalogue)

Baseline static cap L_0=L_1=L and finite-horizon reduced-form demand, F=100, beta=1, a=0.5, L=0,1,5,20,unlimited; n0 and eps Gaussian with SD 4 and rho=0,0.5,0.9, 50,000 paths seed 123. Vary a and caps; compare convergence at t=2 (p2=F), p1 changes, terminal self-financing payoff x0*(p1-p0)+x1*(F-p1) before holding cost. Define W0=20 and record negative wealth and constraint-binding rates, not a fully specified funding equilibrium. Optional wealth feedback extension must derive a unique or selected equilibrium.

## Design-specific acceptance

Verify analytical regime boundaries, continuity and clearing with independent scalar root solution; verify trading gains and wealth identities including cap=0/infinity. Use matched noise and report binding rates, loss/negative wealth and invalid price rates for every cell. Full 50k-path experiment and endogenous wealth constraint remain student work.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish funded wealth from zero-investment spreads, gross from net performance, allocation-time moments from realized risk, and actual turnover from hypothetical trading costs.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
