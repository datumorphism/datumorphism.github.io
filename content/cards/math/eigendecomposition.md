---
title: "Eigenvalues and Eigenvectors"
date: 2019-05-06
category:
  - 'Math'
tags:
  - 'Linear Algebra'
  - 'Basics'
references:
  - name: Eigenvectors and Eigenvalues @ Explained Visually
    link: https://setosa.io/ev/eigenvectors-and-eigenvalues/
links:
  - cards/math/diagonalize-matrix.md
---

To find the eigenvectors $\mathbf x$ of a matrix $\mathbf A$, we construct the eigen equation

$$
\mathbf A \mathbf x = \lambda \mathbf x,
$$

where $\lambda$ is the eigenvalue.

We rewrite it in the components form,

$$
\begin{equation}
A_{ij} x_j = \lambda x_i.
\label{eqn-eigen-decomp-def}
\end{equation}
$$

Mathematically speaking, it is straightforward to find the eigenvectors and eigenvalues.

## Eigenvectors are Special Directions

Judging from the definition in Eq.($\ref{eqn-eigen-decomp-def}$), the eigenvectors do not change direction under the operation of the matrix $\mathbf A$.


## Reconstruct $\mathbf A$

We can reconstruct $\mathbf A$ using the eigenvalues and eigenvectors.

First of all, we will construct a matrix of eigenvectors,

$$
\mathbf P = \begin{pmatrix}\mathbf x_1 & \mathbf x_2 & \cdots & \mathbf x_n \end{pmatrix}.
$$

We also construct a diagonalized matrix $\mathbf \Lambda$

$$
\mathrm{diag} (\mathbf \Lambda)  =  \begin{pmatrix}\lambda_1 & \lambda_2 & \cdots & \lambda_n \end{pmatrix}.
$$

The original matrix $A$ is reconstruct by

$$
\mathbf A = \mathbf P \mathbf \Lambda \mathbf P^T.
$$

