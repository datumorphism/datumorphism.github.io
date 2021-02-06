---
title: Measures of Generalizability
date: 2020-11-08
category:
  - Model Selection
tags:
  - Model Selection
  - Generalizability
references:
  - link: "https://www.oxfordhandbooks.com/view/10.1093/oxfordhb/9780199957996.001.0001/oxfordhb-9780199957996-e-14"
    name: "Vandekerckhove, J., & Matzke, D. (2015). Model comparison and the principle of parsimony. Oxford Library of Psychology."
  - name: "Roelofs, R. (2019). Measuring Generalization and Overfitting in Machine Learning. Doctoral Dissertation, UC Berkeley, 1–171."
    link: "https://escholarship.org/uc/item/6j01x9mz"
links:
  - cards/machine-learning/measurement/empirical-loss.md
  - cards/machine-learning/measurement/population-loss.md
weight: 3
---

To measure the generalization, we define a generalization error,

{{< m >}}
\begin{align}
\mathcal G = \mathcal L_{P}(\hat f) - \mathcal L_E(\hat f),
\end{align}
{{< /m >}}

where $\mathcal L_{P}$ is the population loss, $\mathcal L_E$ is the empirical loss, and $\hat f$ is our model by minimizing the empirical loss.

However, we do not know the actual joint probability $p(x, y)$ of our dataset $\\{x_i, y_i\\}$. Thus the population loss is not known. In machine learning, we usually use cross validation where we split our dataset into train and test dataset. We approximate the population loss using the test dataset.