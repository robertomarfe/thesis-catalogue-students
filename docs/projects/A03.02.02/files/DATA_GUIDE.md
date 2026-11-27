# Data and model setup | A03.02.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Annual two-state surplus S=0.08/0.20, symmetric transition stay probability p=0.55/0.75/0.9/0.97; marginal pi=(0.5,0.5). Consumption log growth g=mu+sigma*epsilon, mu=0.02,sigma=0.02, epsilon=+/-1. Conditional on stay/switch, choose joint G and S_j so lower surplus tends to occur with negative growth: for feasible joint probabilities use Pr(eps=+1,S_j=high|i)=0.5*p_iH+c_i, where |c_i|<=0.5*min(p_iH,1-p_iH); set c_i=0 or 0.4*min(p_iH,1-p_iH). beta=0.96/0.98/0.99,gamma=1/2/4/6. Compare CRRA at same growth law; optional macro targets from FRED consumption and Shiller valuations, not required for simulation.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Distinguish physical growth laws, state-price kernels and traded payoff definitions. Optional external context does not change the synthetic core.

## Frozen research design (original catalogue)

Annual two-state surplus S=0.08/0.20, symmetric transition stay probability p=0.55/0.75/0.9/0.97; marginal pi=(0.5,0.5). Consumption log growth g=mu+sigma*epsilon, mu=0.02,sigma=0.02, epsilon=+/-1. Conditional on stay/switch, choose joint G and S_j so lower surplus tends to occur with negative growth: for feasible joint probabilities use Pr(eps=+1,S_j=high|i)=0.5*p_iH+c_i, where |c_i|<=0.5*min(p_iH,1-p_iH); set c_i=0 or 0.4*min(p_iH,1-p_iH). beta=0.96/0.98/0.99,gamma=1/2/4/6. Compare CRRA at same growth law; optional macro targets from FRED consumption and Shiller valuations, not required for simulation.

## Design-specific acceptance

For every persistence value record transition probabilities, realized conditional shock-surplus covariance, stationary law, mean and SD of log P/D, conditional rate and premium, and stationary second moments including between-state variation. Compare independent-coupling and constant-surplus controls; independently simulate one interior case with burn-in and MC uncertainty.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Separate model-implied curves from traded prices, real safe payoffs from ex post real returns, and conditional from unconditional moments.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
