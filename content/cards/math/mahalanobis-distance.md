---
title: "Mahalanobis Distance"
description: "Distance between a point and a distribution by measuring the distance between the point and the mean of the distribution using the coordinate system defined by the principal components."
date: 2020-03-11
category:
- 'Math'
tags:
- 'Distance'
- 'Metric'
references:
- name: Mahalanobis distance @ Wikipedia
  link: https://en.wikipedia.org/wiki/Mahalanobis_distance
---


Mahalanobis distance is a distance calculated using the inverse of the covariance matrix as the metric. For two vectors $\mathbf x$ and $\mathbf y$, the Mahalanobis distance is

$$
d^2 = (x_i - \bar x) g_{i,j} (y_j - \bar y),
$$

where $g_{ij} = (S^{-1})_{ij}$ and $\mathbf S$ is the covariance matrix.

The covariance is a normalization that mitigates the covariances.

