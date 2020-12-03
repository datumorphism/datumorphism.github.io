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
  - name: "Ross, S. M. (2021). Introduction to Probability and Statistics for Engineers and Scientists (6th ed.). Academic Press."
    link: ""
links:
  - cards/statistics/bayes-theorem.md
  - cards/statistics/conditional-probability-table.md
  - wiki/pattern-mining/association-rules.md
weight: 1
---

Naive Bayesian is a classifier using {{< c "cards/statistics/bayes-theorem.md" >}} with 'naive' assumptions.


## Problems with Conditional Probability Calculation

By definition, the conditional probability of event $\mathbf Y$ given features  $\mathbf X$ is
{{<m>}}
\begin{equation}
P(\mathbf Y\mid \mathbf X) = \frac{P(\mathbf Y, \mathbf X)}{ P(\mathbf X) },
\label{def-cp-y-given-x}
\end{equation}
{{</m>}}
where
- $P(\mathbf X)$ is probability of an event having the features $\mathbf X$,
- $P(\mathbf Y, \mathbf X)$ is the probability of the event $Y$ with features $\mathbf X$.

In equation $\eqref{def-cp-y-given-x}$, the estimation of $P(\mathbf X)$ is not easy. Imagine the size of the space spanned by 10 features. It is a 10-dimensional space and a lot of combinations. This is usually not accurate in many limited datasets. An accurate estimation of the probability of one specific combination requires a large dataset with a lot of occurrences of events with all kinds of feature combinations.

It is the same situation for the estimation of $P(\mathbf X \mid \mathbf Y)$ and $P(\mathbf Y, \mathbf X)$.


On the other hand, the conditional probability of event $Y$ given a set of features $\mathbf X$ can also be calculated using the Bayes' theorem,
{{<m>}}
\begin{equation}
P(\mathbf Y\mid \mathbf X) = \frac{P(\mathbf Y) P(\mathbf X \mid \mathbf Y)}{ P(\mathbf X) },
\label{cp-by-bayes-theorem-init}
\end{equation}
{{</m>}}

where
- $P(\mathbf Y)$ is the probability of event $Y$.

In equation $\eqref{cp-by-bayes-theorem-init}$, we will be calculating $P(\mathbf X\mid \mathbf Y)$ instead of $P( \mathbf Y\mid \mathbf X)$ which will be better defined in a small dataset.



## Naive Bayes

Suppose we are solving a classification problem, with features denoted as $\mathbf X$, and class results as $\mathbf Y$. We would like to train a classifier for the class results given some feature values. Bayes' theorem tells us the probability

$$
\begin{equation}
P(\mathbf Y \mid \mathbf X) = \frac{ P(\mathbf X \mid \mathbf Y) P(\mathbf Y) }{ P(\mathbf X) }.
\end{equation}
$$


{{< message title="Why Don't We Just Calculate $P(\mathbf Y \mid \mathbf X)$ Using the Naive Assumption in $\eqref{def-cp-y-given-x}$" class="info">}}

1. The calculation of $P(\mathbf Y, \mathbf X)$ requires a scan of the whole dataset which is quite costly.
2. In a biased dataset, $P(\mathbf Y, \mathbf X)$ will be biased. Assuming $\mathbf Y$ indicates if the flight is late. $\mathbf Y$ has two possible values, NL (not late) and L (late). In this dataset, the data pipeline records the cases with L more reliably because these are more important. For $\mathbf Y=NL$, the dataset has a lot of missing records because these are not so important. In such a dataset, it is not reliable to calculate $P(\mathbf Y, \mathbf X)$. However, it is more reliable to calculate conditional probabilities such as $P(\mathbf Y\mid \mathbf X)$.

For details of the calculation of $P(\mathbf Y \mid \mathbf X)$, please refer to [conditional probability table](/cards/statistics/conditional-probability-table).

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

In Eq. $\eqref{eq-naive-approximation}$, we have a bunch of probabilities multiplied together. Probabilities are no larger than 1 so this expression is usually tiny. It is not our computer's biggest strength to deal with tiny numbers. So we will simply place a log on both sides of the equation in order to work with normal numbers. After taking the log, the products becomes sums. This also makes it easy to deal with the terms.

$$
\log \left( P(\mathbf Y \mid \mathbf X) \right) = \log \left( P(\mathbf Y) \right) + \sum_i  \log \left( P(X_i \mid \mathbf Y) \right) + \mathrm{Const.}.
$$


## Other Topics

1. Laplace Correction
2. Continuous Values for $\mathbf Y$: Gaussian Naive Bayes, etc
