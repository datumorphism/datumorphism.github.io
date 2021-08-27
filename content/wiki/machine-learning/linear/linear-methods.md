---
title: "Linear Methods"
description: "linear methods"
date: 2018-05-25
categories:
  - "Machine Learning"
tags:
  - "Classification"
  - "Supervised Learning"
  - "Statistical Learning"
  - "Basics"
  - "Linear Models"
links:
  - "wiki/machine-learning/unsupervised/svm.md"
weight: 1
---

## Solving Classification Problems with Linear Models

One simple idea behind classification is to calculate the posterior probability of each class given the variables.

Suppose a dataset have features $F_\alpha$ where $\alpha = 1, 2, \cdots, K$, with corresponding class labels $G_\alpha$. The dataset that provides $N$ datapoints with each deoted as $X_i$. The posterior of the classification is $P(G = G_\alpha \vert X = X_i)$.

A naive idea is to classify the data into two classes $m$ and $n$ using the boundary of a linear model

$$
P(G = G_\alpha \vert X = X_i) = P(G = G_\beta \vert X = X_i).
$$

For a linear model, the boundary is a hyperplane in the feature space, $f(x_1, x_2, \cdots, x_K) = 0$.

Is this linear model terribly bad because it is linear? Not necessarily. With feature engineering, such as feature crossing, a linear separation plane in the engineered feature space can be mapped to complicate boundaries in the original feature space.