---
title: "SVD: Singular Value Decomposition"
excerpt: ""
date: 2019-06-18
category:
- 'Math'
tag:
- 'Matrix'
- 'Factorization'
- 'Linear Algebra'
---

Given a matrix $\mathbf X \to X_{m}^{\phantom{m}n}$, we can decompose it into three matrices

$$
X_{m}^{\phantom{m}n} = U_{m}^{\phantom{m}k} D_{k}^{\phantom{k}l} (V_{n}^{\phantom{n}l} )^{\mathrm T},
$$

where $D_{k}^{\phantom{k}l}$ is diagonal.

Here we actually have $\mathbf U$ being constructed by the eigenvectors of $\mathbf X \mathbf X^{\mathrm T}$, while $\mathbf V$ is being cunstructed by the eigenvectors of $\mathbf X^{\mathrm T} \mathbf X$ (which is also the reason we keep the transpose).