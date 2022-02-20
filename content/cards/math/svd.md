---
title: "SVD: Singular Value Decomposition"
date: 2019-06-18
categories:
- 'Math'
tags:
- 'Matrix'
- 'Factorization'
- 'Linear Algebra'
references:
- name: Matrix and Tensor Factorization from a Machine Learning Perspective
  link: http://statmath.wu.ac.at/research/talks/resources/talkfreudenthaler.pdf
---

Given a matrix $\mathbf X \to X_{m}^{\phantom{m}n}$, we can decompose it into three matrices

$$
X_{m}^{\phantom{m}n} = U_{m}^{\phantom{m}k} D_{k}^{\phantom{k}l} (V_{n}^{\phantom{n}l} )^{\mathrm T},
$$

where $D_{k}^{\phantom{k}l}$ is diagonal.

Here we have $\mathbf U$ being constructed by the eigenvectors of $\mathbf X \mathbf X^{\mathrm T}$, while $\mathbf V$ is being constructed by the eigenvectors of $\mathbf X^{\mathrm T} \mathbf X$ (which is also the reason we keep the transpose).

I find this slide from Christoph Freudenthaler very useful. The original slide has been added as a reference to this article.

{{< figure src="../assets/svd/svd-visualized.jpg" caption="SVD visualized by Christoph Freudenthaler" >}}

