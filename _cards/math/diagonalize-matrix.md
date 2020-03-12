---
title: "Diagnolize Matrice"
excerpt: "Diagnolizing a matrix is a transformation using its eigen space."
date: 2020-03-11
category:
- 'Math'
tag:
- 'Linear Algebra'
---


Given a matrix $\mathbf A$, it is diagonalized using its [eigenvectors](../eigendecomposition).

<div class="card">
	<header class="card-header">
		<p class="card-header-title card-toggle">Why are the eigenvectors needed?</p>
	</header>
	<div class="card-content is-hidden">
		<div class="content">
Eigenvectors of a matrix $\mathbf A$ are the preferred directions. From the definition of eigenvectors,

$$
\mathbf A \mathbf x = \lambda \mathbf x,
$$

we know that the matrix $\mathbf A$ only scales the eigenvectors and no rotations. These directions are special to the matrix $\mathbf A$.

		</div>
	</div>
</div>


1. Find the eigenvectors $\mathbf x_i$ of the matrix $\mathbf A$; If we find degerations, the matrix is not diagonalizable.
2. Construct a matrix $\mathbf S = \begin{pmatrix} \mathbf x_1 & \mathbf x_2 & \cdots & \mathbf x_n \end{pmatrix}$;
3. The matrix $\mathbf A$ is diagonalize using $\mathbf S^{-1} \mathbf A \mathbf S = \mathbf {A_D}$