---
title: "Unsupervised Learning: PCA"
excerpt: "unsupervised learning: principle component analysis"
date: 2018-05-25
toc: true
category:
- 'Machine Learning::Unsupervised Learning'
tag:
- 'PCA'
- 'Unsupervised Learning'
- 'Statistical Learning'
- 'Basics'
weight: 901
---

Principle Component Analyis (PCA) is a commonly used trick for dimensionality reduction.


## How to PCA

Given a set of features,

\begin{equation}
   \mathbf X = \begin{pmatrix}
   \mathbf X_1 \\
   \mathbf X_2 \\
   \cdots \\
   \mathbf X_n
   \end{pmatrix},
\end{equation}

we define a transformation matrix $U_{ji}$ which transform the features to a new set of features,

\begin{equation}
   \mathbf Z_i = \mathbf X_j U_{ji} .
\end{equation}

Notice that $\mathbf Z_i$ and $\mathbf X_i$ are vectors and $U_{ji}$ should apply to all the elements of $\mathbf X_i$.

<div class="card">
	<header class="card-header">
		<p class="card-header-title card-toggle">How does $\mathbf X_j U_{ji}$ work</p>
	</header>
	<div class="card-content is-hidden">
		<div class="content">
Here is an example for $i=3$, $j=2$. Suppose we have

$$
\mathrm X_3 = \begin{pmatrix}
1\\
2\\
3\\
4
\end{pmatrix}
$$

and

$$
U_{32} = 0.5.
$$

We have

$$
\mathbf X_3 \cdot U_{32} = \begin{pmatrix}
0.5\\
1\\
1.5\\
2
\end{pmatrix}.
$$

		</div>
	</div>
</div>


The transformation matrix is normalized,

\begin{equation}
   \operatorname{Diag}(\mathbf U \mathbf U^{\mathrm T}) = ( 1, 1, ... , 1 )
\end{equation}

The coefficients are called **loadings**.

The first principle component is the $\mathbf Z_1$ that has the largest variance, where we have to adjust the coefficients or loadings to make it ture. The coefficients $U_{i1}$ are the elements of the loading vector.

To make it clear, we take an example where each feature has $N$ sample data points. The values for the first principle compunent is

\begin{equation}
   z_{n1}  = x_{n m} U_{m1},
\end{equation}

where I have used the Einstein summation notation. The variance of the first principle component is

\begin{equation}
   \frac{1}{n}\sum_{n=1}^N z_{n1},
\end{equation}

which should be maximized.


<div class="card">
	<header class="card-header">
		<p class="card-header-title card-toggle">Relation between PCA and Linear Regression</p>
	</header>
	<div class="card-content is-hidden">
		<div class="content">
			The ESL has a very nice explanation of this geometrically.
		</div>
	</div>
</div>

## How to find the loadings?

The idea behind PCA is to find the mixings of the features so that the new axes give us the largest variance. We could invent an algorithm to explore the whole parameters space (shifts, scales and rotations of the axes) and find the best parameters. However, this would be rather inefficient.

Alternatively, we could use the [covariance matrix](/wiki/statistics/correlation-coefficient/).

<div class="card">
	<header class="card-header">
		<p class="card-header-title card-toggle">Why the covariance matrix?</p>
	</header>
	<div class="card-content is-hidden">
		<div class="content">
We need would like to find a way to mix the features so that the new feature are mostly decoupled. In other words, we will require the covariance matrix to be almost diagonalized.
		</div>
	</div>
</div>


So given features $\{X_i\}$, the new features $\{Z_i\}$ are related through the $\mathbf U$ matrix,

\begin{equation}
Z_i = U_{ij} X_j.
\end{equation}

The covariance matrix for $\{X_i\}$ is

$$
\mathbf{C_{X}} = \begin{pmatrix}
\sigma_{X_1, X_1} & \sigma_{X_1, X_2} & \cdots & \sigma_{X_1, X_n} \\
\sigma_{X_2, X_1} & \sigma_{X_2, X_2} & \cdots & \sigma_{X_1, X_n} \\
\vdots & \vdots & \ddots & \vdots \\
\sigma_{X_n, X_1} & \sigma_{X_n, X_2} & \cdots & \sigma_{X_n, X_n}
\end{pmatrix}
$$

Recall that

$$
\sigma_{X_i,X_j}^2 = \frac{ (X_i - \bar X_i)^T (X_j - \bar X_j) }{ n }.
$$

Now we see **why it is important to shift our data to be centered by the mean**. If we alway prepare our data so that the mean is 0, i.e., $\bar X_i = 0$, the covariance could be written as

$$
\sigma_{X_i,X_j}^2 = \frac{  X_i^T X_j }{ n }.
$$

If we were to calculate the covariance matrix for the new features $\{Z_i\}$,

$$
\sigma_{Z_i,Z_j}^2 = \frac{ (U_{ik}X_k)^T (U_{jl}X_l) }{ n } =  U_{ik}^T U_{jl} \frac{ X_k^TX_l }{ n } .
$$

From this we could easily derive that a linear transformation for the covariance matrice indicates a linear transformation of the features.

$$
\mathbf{C_{Z}} = \mathbf U^T \mathbf{C_{X}} \mathbf U.
$$

If we were to require the covariance matrix for $\mathbf{C_{Z}}$ to be diagonalized, we would have found that $\mathbf{C_{Z}}$ is basically composed of the eigenvalues. We could deliberately remove those eigenvectors with small eigenvalues and keep those that help us the most with the variance of the data.

To summarize, we could find the principle components by finding the eigenvectors of the covariance matrix:

1. Standardize the data: shift the data so that the mean is 0.
2. Calculate the covariance matrix of the features.
3. Calculate the eigenvectors of the covariance matrix.
4. Construct the transformation matrix.
5. Transform the data.