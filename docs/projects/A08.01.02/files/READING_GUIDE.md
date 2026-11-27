# Reading guide | A08.01.02

Read Ledoit–Wolf on covariance shrinkage and DeMiguel et al. on naive allocation; distinguish improved covariance conditioning from out-of-sample risk.

Read the focused methods note supplied with this workspace. The following references are the frozen proposal references; source routes selectively verified in v31; academic references inherited, remaining metadata/full text not yet fully audited. Verify final citations and editions.

1. Markowitz, H. (1952). Portfolio Selection. Journal of Finance, 7, 77-91.
2. Ledoit, O., and Wolf, M. (2004). A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices. Journal of Multivariate Analysis, 88, 365-411. https://doi.org/10.1016/S0047-259X(03)00096-4
3. DeMiguel, V., Garlappi, L., and Uppal, R. (2009). Optimal Versus Naive Diversification: How Inefficient Is the 1/N Portfolio Strategy? Review of Financial Studies, 22, 1915-1953.

## Bibliographic and reading review | v45

Original reading list retained. Selected publisher metadata checked; all other references normalized from frozen citations, with independent verification and full-text reading pending.

1. Markowitz, H. (1952). Portfolio Selection. Journal of Finance, 7, 77-91. — qualified inherited metadata. Frozen citation; independently verify metadata and full text.
2. Ledoit, O., and Wolf, M. (2004). A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices. Journal of Multivariate Analysis, 88, 365-411. https://doi.org/10.1016/S0047-259X(03)00096-4 — selected publisher metadata. Elsevier confirms 2004, 88(2), 365-411; scaled identity shrinkage, not a guarantee of lower held-out variance.
3. DeMiguel, V., Garlappi, L., and Uppal, R. (2009). Optimal Versus Naive Diversification: How Inefficient Is the 1/N Portfolio Strategy? Review of Financial Studies, 22, 1915-1953. — qualified inherited metadata. Frozen citation; independently verify metadata and full text.

**Reading focus:** Covariance-estimation risk in GMV without expected-return estimates.

Sample covariance ddof=1 and sklearn LedoitWolf covariance use different scaling; uniform scale has no GMV weight effect but changes predicted variance. Singular sample covariance must be recorded, not silently replaced by shrinkage. Universe and lookbacks must not be picked by future performance.


Read the original articles for assumptions and derivations; validate editions and exact metadata before citation. The bibliographic record is inherited from the earlier selective review, not a new full-text verification. Historical provider-route notes are provisional and must be checked against current provider documentation.
