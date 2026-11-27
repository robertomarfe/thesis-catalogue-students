---
title: "Focused methods — Put Writing and the Compensation for Downside Risk"
subtitle: "D08.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Funding
With zero dividends, parity equates $S_0-C_0$ and $Ke^{-rT}-P_0$. Cash-secured writing requires collateral and receives premium; both determine initial funding. Rolling index returns do not isolate variance premium.

## Tail comparison
A lagged equity weight gives return $R^f_t+w_{t-1}(R^M_t-R^f_t)$. Disclose weight bounds and realized mismatch. Compute tail loss on common months with a consistent loss sign. Turbulence labels based on future returns are descriptive; lagged VIX regimes are a different, feasible design. Separate launch and backfill.

## Research checks

Focus on downside compensation and collateral rather than D08.03.01's upside capture. Defer or explicitly approve redesign if PUT rights or history fail. No silent BXM or synthetic substitution.
