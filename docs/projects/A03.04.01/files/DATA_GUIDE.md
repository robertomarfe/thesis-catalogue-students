# Data and model setup | A03.04.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Annual synthetic scenarios beta=.97-.99, gamma=2-8, p=0,.01,.02,.04, J=-.15,-.30,-.45 log points, ordinary sigma=.02, mu=.02, dividend leverage phi=1,2,3; benchmark match unconditional mean growth by adjusting mu, compare also variance-matched feasible cases. Disaster inflation 0 or positive jump and bond recovery .5-1; distinguish defaultable real claim and nominal claim. Optional public historical disaster calibration only after permission/data gate, not required.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Distinguish physical growth laws, state-price kernels and traded payoff definitions. Optional external context does not change the synthetic core.

## Frozen research design (original catalogue)

Annual synthetic scenarios beta=.97-.99, gamma=2-8, p=0,.01,.02,.04, J=-.15,-.30,-.45 log points, ordinary sigma=.02, mu=.02, dividend leverage phi=1,2,3; benchmark match unconditional mean growth by adjusting mu, compare also variance-matched feasible cases. Disaster inflation 0 or positive jump and bond recovery .5-1; distinguish defaultable real claim and nominal claim. Optional public historical disaster calibration only after permission/data gate, not required.

## Design-specific acceptance

Report ordinary variance required by total variance law before solving, regime probabilities and q_d, q_f and payoff prices. Check p=0 and deterministic-mixture exact values, then stratified simulation with disaster counts; compare fixed-mean and feasible fixed-variance designs. Show conditional-on-no-disaster versus unconditional premium without labeling one a population estimate.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Separate model-implied curves from traded prices, real safe payoffs from ex post real returns, and conditional from unconditional moments.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
