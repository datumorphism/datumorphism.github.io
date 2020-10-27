---
title: "Naive Bayes"
description: "Naive Bayes"
date: 2019-06-17
category:
  - 'Machine Learning'
tags:
  - 'Machine Learning'
  - 'Classification'
  - 'Bayesian'
references:
  - name: "Naive Bayesian"
    link: https://www.saedsayad.com/naive_bayesian.htm
  - name: "Naive Bayes classifier @ Wikipedia"
    link: https://en.wikipedia.org/wiki/Naive_Bayes_classifier
links:
  - cards/statistics/bayes-theorem.md
  - cards/statistics/conditional-probability-table.md
weight: 1
---

Naive Bayesian is a classifier using [Bayes' theorem](/cards/statistics/bayes-theorem) with 'naive' assumptioins.

Suppose we are solving a classification problem, with features denoted as $\mathbf X$, and class results as $\mathbf Y$. We would like to train a classifier for the class results given some feature values. Bayes' theorem tells us the probability

$$
\begin{equation}
P(\mathbf Y \mid \mathbf X) = \frac{ P(\mathbf X \mid \mathbf Y) P(\mathbf Y) }{ P(\mathbf X) }.
\end{equation}
$$


{{< message title="Why Don't We Just Calculate $P(\mathbf Y \mid \mathbf X)$" class="info">}}

Because it would be hard to calculate it if we have too many features. In fact, $P(\mathbf X)$ is hard to calculate too.

For details of the calculation of $P(\mathbf Y \mid \mathbf X)$, please refer to [conditional probability table](/cards/statistics/conditional-probability-table.md).

{{</message>}}

Being "naive", we will assume that the features are independent of each other, i.e., don't have interactions with each other in terms of predictions. In this case, we simply write down the theorem as

$$
\begin{equation}
P(\mathbf Y \mid \mathbf X) = \frac{ P(\mathbf Y) \prod_i P(X_i \mid \mathbf Y) }{ \prod_i P(X_1) } \propto P(\mathbf Y)  \prod_i P(X_i \mid \mathbf Y) .
\label{eq-naive-approximation}
\end{equation}
$$

We do not care about $\prod_i P(X_1)$ because it only serves as a normalization factor. Besides, it could be hard to calculate in some cases.

## Log-Likelihood

In Eq. $\eqref{eq-naive-approximation}$, we have a bunch of probabilities multiplied together. Probabilities are no larger than 1 so this expression is usually tiny. It is not our computer's biggest strength to deal with tiny numbers. So we will simply place a log on both sides of the equation in order to work with normal numbers.

$$
\log \left( P(\mathbf Y \mid \mathbf X) \right) = \log \left( P(\mathbf Y) \right) + \sum_i  \log \left( P(X_i \mid \mathbf Y) \right) + \mathrm{Const.}.
$$


## Other Topics

1. Laplace Correction
2. Continuos Values for $\mathbf Y$: Gaussian Naive Bayes, etc
