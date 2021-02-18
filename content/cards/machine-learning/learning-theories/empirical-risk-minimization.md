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