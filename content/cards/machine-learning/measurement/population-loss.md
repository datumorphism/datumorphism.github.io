---
title: "Population Loss"
description: "The loss calculated on all the whole population"
date: 2021-02-06
categories:
- 'Machine Learning'
- 'Measurement'
tags:
- Data
- Model Selection
links:
  - wiki/model-selection/measures-of-generalizability.md
  - cards/machine-learning/measurement/empirical-loss.md
---


Given a dataset with records $\\{x_i, y_i\\}$ and a model $\hat y_i = f(x_i)$. Suppose we know the actual generating process of the dataset and the joint probability density distribution of all the data points is $p(x, y)$, the population loss is defined on the whole assumed population,

{{< m >}}
\begin{align}
\mathcal L_{P} = \mathop{\mathbb{E}}_{p(x,y)}[ d(y, f(x))],
\end{align}
{{< /m >}}

where $d(y, f(x))$ is the distance defined between $y$ and $f(x)$.
