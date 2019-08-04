---
title: "Eigenvalues and Eigenvectors"
excerpt: ""
date: 2019-05-06
category:
- 'Math'
tag:
- 'Linear Algebra'
---

To find the eigenvectors $\mathbf X$ of a matrix $\mathbf A$, we construct the eigen equation

$$
$\mathbf A$ $\mathbf X$ = \lambda $\mathbf A$,
$$

where $\lambda$ is the eigenvalue.

To make it seaier to understand, we rewrite it in the components form,

$$
A_{ij} X_j = \lambda X_j.
$$

Mathematically speaking, it is straightforward to find the eigenvectors and eigenvalues.


## Reconstruct $\mathbf A$

We can reconstruct $\mathbf A$ using the eigenvalues and eigenvectors.

First of all, we will construct a matrix of eigenvectors,

$$
\mathbf P = \begin{pmatrix}\mathbf X_1 & \mathbf X_2 & \cdots & \mathbf X_n \end{pmatrix}.
$$

We also construct a diagonalized matrix $\mathbf \Lambda$

$$
\mathrm{diag} (\Lambda)  =  \begin{pmatrix}\lambda_1 & \lambda_2 & \cdots & \lambda_n \end{pmatrix}.
$$

The original matrix $A$ is reconstrut by

$$
\mathbf A = \mathbf P \mathbf \Lambda \mathbf P^T.
$$

