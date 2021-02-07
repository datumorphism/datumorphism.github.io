---
title: "Empirical Loss"
description: "The loss calculated on all the data points"
date: 2021-02-06
category:
- 'Machine Learning'
- 'Measurement'
tags:
- Data
- Model Selection
links:
  - wiki/model-selection/measures-of-generalizability.md
  - cards/machine-learning/measurement/population-loss.md
---


Given a dataset with records $\\{x_i, y_i\\}$ and a model $\hat y_i = f(x_i)$ the empirical loss is calculated on all the records

{{< m >}}
\begin{align}
\mathcal L_{E} = \frac{1}{n} \sum_i^n d(y_i, f(x_i)),
\end{align}
{{< /m >}}

where $d(y_i, f(x_i))$ is the distance defined between $y_i$ and $f(x_i)$.
