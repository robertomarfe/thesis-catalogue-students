# Data and model setup | D06.02.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Risk-neutral GBM, S0=80/100/120,K=100,r=0.05,q=0,sigma=0.2/0.4,T=1; 4,12,52 exercise dates, maturity included. Exact GBM simulation; nested CRR reference aligned with exercise dates and refine until price stable. Train N=2,000/10,000/50,000 with seeds 2027+, independent validation/evaluation N>=100,000; repeat 20 train seeds for selected scenarios. Basis constants plus scaled powers degree 2-5, Laguerre alternative, QR/SVD least squares and condition-number diagnostics.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
