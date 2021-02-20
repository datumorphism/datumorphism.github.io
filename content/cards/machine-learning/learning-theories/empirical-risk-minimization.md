---
title: "ERM: Empirical Risk Minimization"
date: 2021-02-18
category:
- 'Machine Learning::Theories'
tags:
- 'Data'
- 'Loss'
references:
- name: "Murphy, K. P. (2012). Probabilistic Machine Learning: An Introduction."
  link: "https://mitpress.mit.edu/books/machine-learning-1"
published: true
---

Empirical risk $R$ is a measurement the goodness of fit based on empirical information. Empirical risk minimization minimizes the empirical risk to select a good model $\hat f$ out of all possible models $f$ in our hypothesis space for a dataset $\mathcal D$,

{{< m >}}
\hat f = \operatorname{argmin} R(f, \mathcal D).
{{< /m >}}

## Empirical Risk Example

For example, the emprical risk can be represented by the negative log likelihood.

A negative log likelihood (NLL) for a model $\theta$ of dataset $\mathcal D$

{{< m >}}
NLL(\theta) = -\log  p(\mathcal D\mid\theta) = -\sum_n \log (y_n \mid x_n, \theta).
{{< /m >}}

An empirical risk loss function $\mathcal L$ is

{{< m >}}
\mathcal L(\theta) = \frac{1}{N} \sum_n \mathscr l(y_n, \theta; x_n),
{{< /m >}}

where $\mathscr l$ is a loss. For example, one could design a stepwise loss in classification

{{< m >}}
\mathscr l = \begin{cases}
0, \qquad \text{if prediction matches data} \\
1 \qquad \text{if prediction doesn't match data}
\end{cases}
{{< /m >}}

Another possibility is surrogate loss which is continuous.


## Regularized Risk

However, ERM may lead to overfitting. One method to solve this is to add a penalty based on the complexity of the model $C(f)$,

{{< m >}}
R_{Reg}(f, \mathcal D) = R(f, \mathcal D) + \lambda C(f).
{{< /m >}}