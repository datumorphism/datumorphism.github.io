---
title: "Statistical Sign Test"
description: "Statistical test without assuming models"
date: 2019-01-20
categories:
- 'Statistical Hypothesis Testing'
tags:
- 'Statistics'
- 'Basics'
- 'Hypothesis Testing'
references:
- link: "https://www.coursera.org/learn/inferential-statistics/lecture/UvETp/6-02-the-sign-test"
  name: 'The sign test @ inferential statistics'
weight: 4
---

We have a small dataset, but it doesn't satisfy the t-test conditions. Then we would use as little assumptions as possible.

## Wine Taste

Suppose we have two bottles of wine, one of them is 300 euros while the other is 100 euros.

Now we ask the question:

Does expensive wine taste better?

We find 10 experts and give them some experiments. The result is recorded then processed into the following table.

| expert # | expensive is better |
|:--------:|:-------------------:|
| 1        | yes                 |
| 2        | no                  |
| 3        | yes                 |
| 4        | yes                 |
| 5        | yes                 |
| 6        | no                  |
| 7        | yes                 |
| 8        | yes                 |

Naively, we could simply count the number of yes and find the probability of yes in this sample, i.e.,

{{<m>}}
\frac{\text{number of yes}}{\text{total experiments}} = \frac{6}{8} = 75\%.
{{</m>}}

It seems that we have more experts find that expensive wine tastes better.

Is expensive wine really better? Remember that we could have fluctuations when drawing samples from the population. We need a statistical test.

The sign test fits perfectly into this scenario. If the wines are the same, then we would have a probability of 0.5 for an expert to identify the differences between the wines, $p_0=0.5$. Then we ask this question:

What is the probability that we would find 6 experts that tell the difference out of 8 experts, given the condition that the wins are the same?

This becomes a binomial distribution problem. To have 6 successful experiments out of 8 given a success probability of 0.5, we have

$$
C_8^6 0.5^6(1-0.5)^2 = 28 * \frac{1}{2^6} * \frac{1}{2^2} = 0.109
$$

This means that the probability that we find 6 experts speaking for the expensive wine is 0.109 even if the wines are not different by the taste. We usually don't think this is a rare event. That being said, we can not determine if the expensive wine tastes better by using these data.

## The Sign Test

We just performed a sign test. Here is a bit of summary.

1. The null hypothesis: the wines taste the same, i.e., the probability for an expert to find the difference is $p_0 = 0.5$.
2. The alternative hypothesis: the wines taste different, i.e., $p_0! = 0.5$.

We use the null hypothesis to calculate the probability of X success ($X=6$ in our example) from N tests ($N=8$ in our example). If the probability is too high, then we would think that the case we get from the sample is actually quite possible even if the wines are the same. Then we could not make a decision from the data.
