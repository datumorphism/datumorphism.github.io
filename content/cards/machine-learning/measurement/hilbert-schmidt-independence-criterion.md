---
title: "Hilbert-Schmidt Independence Criterion (HSIC)"
description: ""
date: 2021-11-08
categories:
  - "Machine Learning"
tags:
  - "Data"
  - "Representation"
  - "Similarity"
links:
  - cards/math/statistics-centering-matrix.md
---

Given two kernels of the feature representations $K=k(x,x)$ and $L=l(y,y)$, HSIC is defined as[^Gretton2005][^Kornblith2019]

$$
\operatorname{HSIC}(K, L) = \frac{1}{(n-1)^2} \operatorname{tr}( K H L H ),
$$

where

- $x$, $y$ are the representations of features,
- $n$ is the dimension of the representation of the features,
- $H$ is the so-called {{< c "cards/math/statistics-centering-matrix.md" "centering matrix" >}}.

We can choose different kernel functions $k$ and $l$. For example, if $k$ and $l$ are linear kernels, we have $k(x, y) = l(x, y) = x \cdot y$. In this linear case, HSIC is simply $\parallel\operatorname{cov}(x^T,y^T) \parallel^2_{\text{Frobenius}}$.


[^Kornblith2019]: Kornblith S, Norouzi M, Lee H, Hinton G. Similarity of Neural Network Representations Revisited. arXiv [cs.LG]. 2019. Available: http://arxiv.org/abs/1905.00414

[^Gretton2005]: Gretton A, Bousquet O, Smola A, Schölkopf B. Measuring Statistical Dependence with Hilbert-Schmidt Norms. Algorithmic Learning Theory. Springer Berlin Heidelberg; 2005. pp. 63–77. doi:10.1007/11564089_7
