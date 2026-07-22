"""Reproduce the two portfolio A/B-test decisions from aggregate inputs."""

from math import sqrt
from scipy import stats

# H&M email-open experiment
CONTROL_OPENS = 836
CONTROL_SENT = 4764
TEST_OPENS = 894
TEST_SENT = 4673

control_rate = CONTROL_OPENS / CONTROL_SENT
test_rate = TEST_OPENS / TEST_SENT
pooled = (CONTROL_OPENS + TEST_OPENS) / (CONTROL_SENT + TEST_SENT)
standard_error = sqrt(pooled * (1 - pooled) * (1 / CONTROL_SENT + 1 / TEST_SENT))
z_score = (test_rate - control_rate) / standard_error
p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))

print(f"H&M control open rate: {control_rate:.3%}")
print(f"H&M test open rate: {test_rate:.3%}")
print(f"H&M two-sided p-value: {p_value:.6f}")

# Warby Parker experiment uses verified summary statistics from 3,365 ratings
control_n = 1666
control_mean = 3.2767106842737093
control_sd = 1.2084378953329662
test_n = 1699
test_mean = 3.337257210123602
test_sd = 1.2273271490761337

result = stats.ttest_ind_from_stats(
    mean1=test_mean, std1=test_sd, nobs1=test_n,
    mean2=control_mean, std2=control_sd, nobs2=control_n,
    equal_var=False,
)
print(f"Warby Parker Welch t-test p-value: {result.pvalue:.6f}")
