---
title: "ANOVA"
description: "analysis of variance"
date: 2021-03-07
authors:
  - "LM"
categories:
  - "statistics"
tags:
  - "variacne"
references:
  - name: "Fox, J. Applied Regression Analysis and Generalized Linear Models. (SAGE Publications, 2015)."
    link: ""
  - name: "A Simple Introduction to ANOVA (with applications in Excel)"
    link: "https://www.analyticsvidhya.com/blog/2018/01/anova-analysis-of-variance"
weight:
links:
  - "wiki/statistical-hypothesis-testing/hypothesis-testing.md"
---

In many problems, we have to test if the distributions of several groups are the same. We will the null hypothesis:

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

