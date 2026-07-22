# A/B Testing Decision Analysis

This case study compares two experiments and shows why a higher test average is not automatically enough to recommend a rollout.

## H&M email subject line

- Control: 836 opens from 4,764 emails (**17.55%**)
- Test: 894 opens from 4,673 emails (**19.13%**)
- Absolute lift: **1.58 percentage points**
- Two-sided p-value: **0.047**
- Decision: the test version performed better at the 5% significance level, while still falling short of the original 20% business target.

## Warby Parker landing page

- Control mean rating: **3.277** from 1,666 users
- Test mean rating: **3.337** from 1,699 users
- Welch t-test p-value: **0.149**
- Decision: the observed difference was not statistically significant, so the result should not be presented as proof that the new page improved satisfaction.

## Quality lesson

The work separates statistical evidence from business goals. It also documents possible Type I and Type II errors, checks whether the experiment was designed with an adequate sample and clear success metric, and recommends follow-up measurement such as conversion, revenue, and engagement rather than optimizing a single metric in isolation.

## Files

- [`analysis.py`](analysis.py): reproducible calculations from aggregate inputs
- [`experiment-summary.csv`](experiment-summary.csv): compact experiment comparison
