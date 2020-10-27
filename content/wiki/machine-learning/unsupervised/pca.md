---
title: "Unsupervised Learning: PCA"
description: "Principal component analysis is a method to remove redundancies of the features by looking into the variances."
date: 2018-05-25
category:
- 'Machine Learning'
tags:
- 'PCA'
- 'Unsupervised Learning'
- 'Statistical Learning'
- 'Basics'
references:
  - name: "Shlens, J. (2003). A Tutorial on Principal Component Analysis"
    link: "https://www.cs.princeton.edu/picasso/mats/PCA-Tutorial-Intuition_jp.pdf"
links:
  - cards/statistics/covariance-matrix.md
weight: 2
---

{{< message class="warning">}}
We use the Einstein summation notation in this article.
{{</message>}}

Principal Component Analysis (PCA) is a commonly used trick for dimensionality reduction so that the new features represents most of the variances of the data.

{{< card title="Representations of Dataset">}}

In theory, a dataset can be represented by a matrix if we specify the basis. However, the initial given basis is not always the most convinient one. Suppose we find a new set of basis for the dataset, the matrix representation may be simpler and easier to use.

For convenience, we do not distinguish the representation and the abstract dataset in this article.
{{</card>}}

Give a dataset of $n$ features and $m$ rows,

{{<m>}}
\begin{equation}
   \mathbf X = \begin{pmatrix}
   \mathbf X_1 \\
   \mathbf X_2 \\
   \cdots \\
   \mathbf X_n
   \end{pmatrix},
\end{equation}
{{</m>}}

where each $\mathbf X_i$ is a $m$ dimensional column vector.

We are looking for a $n\times p$ matrix $\mathbf P$ so that

$$
Z_{ik} = X_{ij}P_{jk},
$$

where $i\in [1, m]$, $k\in [1,p]$, and $j\in [1, n]$. This projection will select out $p$ features.

{{< card title="Vector Notation Formalism">}}
Given features $\{\mathbf X_i\}$, the new features $\{\mathbf Z_i\}$ are related through the $\mathbf U$ matrix,

\begin{equation}
\mathbf Z_k = \mathbf X_j P_{jk}.
\end{equation}
{{</card>}}

The coefficients $P_{jk}$ are called **loadings**.


## What is PCA

The transformation $\mathbf P$ select out features that represents the most variances. How are the variances represented? The [covariance matrix](/cards/statistics/covariance-matrix/) sheds light on the problem.

In an ideal condition, the covariance matrix of the dataset matrix is diagonalized. This indicates that the dataset matrix features are not correlated, i.e., the basis axes are in the direction of the spread.

In order to perform PCA, we have to acquire a new transformed dataset matrix $\mathbf Z$ so that the covariance matrix $\mathbf {C_{Z}}$ of $\mathbf Z$ is (mostly) diagonalized. It requires

{{<m>}}
\begin{align}
\mathbf {C_{Z}} =& \frac{\mathbf{Z}^{T} \mathbf {Z} }{n-1} \\
=& \frac{ (\mathbf{X}\mathbf P)^{T} \mathbf {X} \mathbf P}{n-1} \\
=& \frac{\mathbf P^T\mathbf X^T\mathbf X \mathbf P   }{n-1} \\
=&  \mathbf P^T\frac{ (\mathbf X^T\mathbf X) }{n-1} \mathbf P.
\label{eqn-pca-cov-mat-diag}
\end{align}
{{</m>}}

**The covariance matrix** $\mathbf {C_{Z}}$ **is diagonalized if choose** $\mathbf P$ **so that it diagonalizes the matrix** $(\mathbf X^T\mathbf X)$, i.e.,

$$
\begin{equation}
(\mathbf X^T\mathbf X) = \mathbf P^T \mathbf {D_{X^TX}} \mathbf P
\end{equation}
$$

> Notice that $\mathbf P \mathbf P^T = \mathbf I$.

The component $\mathbf Z_i$ that has the largest variance is the first principal component. In most cases, we arrange the transformation $\mathbf P$ so that the first component $\mathbf Z_1$ is the first principal component. The variance of the first principle component is

\begin{equation}
   \frac{1}{n}\sum_{n=1}^N z_{n1},
\end{equation}

which is maximized.


{{<card title="Relation between PCA and Linear Regression">}}
The ESL has a very nice explanation of this geometrically.
{{</card>}}

## Why is $\mathbf P$ related to the covariance matrix, again?

The idea behind PCA is to find the mixings of the features so that the new axes give us the largest variance. We could invent an algorithm to explore the whole parameter space (shifts, scales, and rotations of the axes) and find the best parameters. However, this would be rather inefficient. The proof Eq. ($\ref{eqn-pca-cov-mat-diag}$) provides theoretical support.


{{< card title="Why the covariance matrix?">}}
We need would like to find a way to mix the features so that the new features are mostly decoupled. In other words, we will require the covariance matrix to be almost diagonalized.
{{</card>}}


The covariance matrix for $\{\mathbf X_i\}$ is

{{<m>}}
\mathbf{C_{X}} = \begin{pmatrix}
\sigma^2_{\mathbf X_1, \mathbf X_1} & \sigma^2_{\mathbf X_1, \mathbf X_2} & \cdots & \sigma^2_{\mathbf X_1, \mathbf X_n} \\
\sigma^2_{\mathbf X_2, \mathbf X_1} & \sigma^2_{\mathbf X_2, \mathbf X_2} & \cdots & \sigma^2_{\mathbf X_1, \mathbf X_n} \\
\vdots & \vdots & \ddots & \vdots \\
\sigma^2_{\mathbf X_n, \mathbf X_1} & \sigma^2_{\mathbf X_n, \mathbf X_2} & \cdots & \sigma^2_{\mathbf X_n, \mathbf X_n}
\end{pmatrix}
{{</m>}}

Recall that

$$
\sigma_{X_i,X_j}^2 = \frac{ (\mathbf X_i - \bar X_i)^T (\mathbf X_j - \bar X_j) }{ n }.
$$

**We shift our data to be centered by the mean**. If we always prepare our data so that the mean is 0, i.e., $\bar X_i = 0$, the covariance could be written as

$$
\sigma_{\mathbf X_i,\mathbf X_j}^2 = \frac{  X_i^T X_j }{ n }.
$$

If we were to calculate the covariance matrix for the new features $\{Z_i\}$,

$$
\sigma_{Z_i,Z_j}^2 = \frac{ (U_{ik}X_k)^T (U_{jl}X_l) }{ n } =  U_{ik}^T U_{jl} \frac{ X_k^TX_l }{ n } .
$$

From this, we could easily derive that a linear transformation for the covariance matrice indicates a linear transformation of the features.

$$
\mathbf{C_{Z}} = \mathbf U^T \mathbf{C_{X}} \mathbf U.
$$

If we were to require the covariance matrix for $\mathbf{C_{Z}}$ to be diagonalized, we would have found that $\mathbf{C_{Z}}$ is composed of the eigenvalues. We could deliberately remove those eigenvectors with small eigenvalues and keep those that help us the most with the variance of the data.

To summarize, we could find the principal components by finding the eigenvectors of the covariance matrix:

1. Standardize the data: shift the data so that the mean is 0.
2. Calculate the covariance matrix of the features, $\mathbf {C_{X}}$.
3. Calculate the eigenvectors of the covariance matrix.
4. Construct the transformation matrix, $\mathbf P$.
5. Transform the data using $\mathbf U$, $\mathbf Z = \mathbf X \mathbf P$.
6. Decide the number of principal components $p$ and choose the first $p$ columns of $\mathbf Z$.

## SVD and PCA

It is straightforward to prove that the principal components are he orthonormal basis that spans the row space of $\mathbf X$ in our setup [^1].

[^1]: Shlens, J. (2003). [A Tutorial on Principal Component Analysis](https://www.cs.princeton.edu/picasso/mats/PCA-Tutorial-Intuition_jp.pdf).