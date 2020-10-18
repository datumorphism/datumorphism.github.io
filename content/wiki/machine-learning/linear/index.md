---
title: "Linear Methods"
excerpt: "linear methods"
date: 2018-05-25
toc: true
category:
- 'Machine Learning::Linear Models'
tag:
- 'Classification'
- 'Supervised Learning'
- 'Statistical Learning'
- 'Basics'
weight: 1000
---

One simple idea behind classification is the posterior probability of each class given the variables.

Suppose we have a dataset with feature $F_\alpha$ with $\alpha = 1, 2, \cdots, K$, with corresponding class labels $G_\alpha$. Then we have a dataset that provides $N$ datapoints with each deoted as $X_i$. The posterior of the classification are $P(G = G_\alpha \vert X = X_i)$.

A naive idea is to classify the data into two classes $m$ and $n$ according to the boundary

$$
P(G = G_\alpha \vert X = X_i) = P(G = G_\beta \vert X = X_i).
$$

The boundary is a hyperplane in the feature space, $f(x_1, x_2, \cdots, x_K) = 0$.