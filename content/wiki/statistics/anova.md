---
title: "ANOVA"
description: "analysis of variance"
date: 2021-03-07
authors:
  - "LM"
categories:
  - "statistics"
tags:
  - "statistics"
  - "variacne"
  - "ANOVA"
references:
  - name: "Fox, J. Applied Regression Analysis and Generalized Linear Models. (SAGE Publications, 2015)."
    link: ""
  - name: "A Simple Introduction to ANOVA (with applications in Excel)"
    link: "https://www.analyticsvidhya.com/blog/2018/01/anova-analysis-of-variance"
weight:
links:
  - "wiki/statistical-hypothesis-testing/hypothesis-testing.md"
---

In many problems, we have to test if the distributions of several groups are the same. We will use the null hypothesis:

The distributions of several groups are the same.

ANOVA tests the null hypothesis by comparing the variability between groups and within groups. If the variability between groups are significantly larger than the variability within groups, we are more confident that the distributions of different groups are different.


We will use two groups as an example. We use a fake dataset:


| Group A     |
| ----------- |
| $x^A_1$     |
| $x^A_2$     |
| ...         |
| $x^A_{N_A}$ |





| Group B     |
| ----------- |
| $x^B_1$     |
| $x^B_2$     |
| ...         |
| $x^B_{N_B}$ |




## Within Group Variability

The within group variablility is proportional to

$$
\sigma_{in} \propto \sum_{i_A} (x_{i_A} - \bar x^A ) + \sum_{i_B} (x_{i_B} - \bar x^B ),
$$

where $\bar x^A$ is the mean within group $A$ and $\bar x^B$ is the mean within group $B$.

We use limitation to get the normalizing constant. We can tolerate larger $\sum_{i_A} (x_{i_A} - \bar x^A ) + \sum_{i_B} (x_{i_B} - \bar x^B )$ if we have more data points $N_A+N_B$. On the other hand, the more groups we have, we can tolerate smaller $\sum_{i_A} (x_{i_A} - \bar x^A ) + \sum_{i_B} (x_{i_B} - \bar x^B )$.

A naive guess would lead to

$$
\sigma_{in} = \frac{\sum_{i_A} (x_{i_A} - \bar x^A ) + \sum_{i_B} (x_{i_B} - \bar x^B )}{N_A+N_B - k},
$$

where $k=2$ is the number of groups.


## Between Group Variability


The between group variability is measured by the differences in the group means.

The mean of group A is $\bar x^A$ and the mean of group B is $\bar x^B$. Here we define the gran mean $\bar x = \sum_{\text{all in group A and B}} x_i/(N_A+N_B)$.

The variability between groups is proportional to the sum of variability based on the means

$$
\sigma_{between} = \frac{N_A(\bar x^A - \bar x )^2 + N_B(\bar x^B - \bar x )^2}{k},
$$

where $k=2$ is the number of groups.


## ANOVA

ANOVA is essentially a F-test,

$$
F = \frac{\sigma_{between}}{\sigma_{in}}.
$$

The $p$ value can be looked up in a F-table.



## Python Code




```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Generate Gaussian data
a_dist = np.random.normal(loc=0, scale=1, size=1000)
b_dist = np.random.normal(loc=0.5, scale=1, size=1000)

# Create plot for the two distributions
fig, ax = plt.subplots(figsize=(10, 6.18))
ax.hist(a_dist, bins=50, density=True)
ax.hist(b_dist, bins=50, density=True)
ax.set_xlabel("Values")
ax.set_title("Histogram of Distribution A and B")
plt.show()

```

{{< figure src="../assets/anova/hist_a_and_b.png" >}}


![[inbox.ml/statistics/analysis-of-variance/assets/hist_a_and_b.png]]

Now we performance a one-way ANOVA.

```python

# One-way ANOVA
stats.f_oneway(a_dist, b_dist)
```

We get

```python
F_onewayResult(statistic=135.10932572037217, pvalue=2.873326981106292e-30)
```




## N-way ANOVA

ANOVA test can be done on the effect multiple categorical variables. For example, for two variables, we built a table with the rows being the classes of one variable and the columns being the classes of another variable. The samples spanned by these two directions can be used to test the effect of the variables on different combinations of the variables.



