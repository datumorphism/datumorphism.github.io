---
title: "NMF: Nonnegative Matrix Factorizatioin"
description: "Nonnegative Matrix Factorizatioin has a bright future"
date: 2019-06-13
categories:
  - "Machine Learning"
tags:
  - "Machine Learning"
  - "Factorization"
references:
  - link: http://arxiv.org/abs/1401.5226
    name: 'Gillis, N. (2014). The Why and How of Nonnegative Matrix Factorization.'
  - link: https://en.wikipedia.org/wiki/Spherical_harmonics#Connection_with_representation_theory
    name: Spherical Harmonics
  - link: https://blog.acolyer.org/2019/02/18/the-why-and-how-of-nonnegative-matrix-factorization/
    name: The why and how of nonnegative matrix factorization
links:
  - cards/math/svd.md
  - cards/math/eigendecomposition.md
  - wiki/machine-learning/unsupervised/pca.md
  - wiki/machine-learning/unsupervised/svm.md
  - cards/math/frobenius-distance.md
weight: 2
---

## Decomposition

For simplicity, we start with a data point $\mathbf P$ in a $k$-dimensional space spanned by $k$ basis vectors $\mathbf V^k$. Naturally, we could write down the component decomposition of the point using the basis vectors $\mathbf V^k$,

$$
\mathbf P = P_k \mathbf V^k.
$$

This is immediately obvious to us since we have been dealing with rank 2 $(k, 1)$ basis vectors and we are talking about the $k$ coordinates for a point.

This point is represented by a matrix of rank 2 $(k, 1)$ given this basis.

$$
\mathbf P \to \begin{pmatrix} P_1, P_2, \cdots, P_k \end{pmatrix}
$$

If we assume a cartesian coordinate system, the basis are normal vectors.

{{<m>}}
\mathbf V^1 \to \begin{pmatrix}
1\\
0\\
\vdots\\
0
\end{pmatrix}, \mathbf V^2 \to \begin{pmatrix}
0\\
1\\
\vdots\\
0
\end{pmatrix}, \cdots
{{</m>}}

These representations of the basis vectors can be joined together

{{<m>}}
\mathbf V \to
\begin{pmatrix}
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \vdots\\
0 & 0 & 0 & 1
\end{pmatrix}
{{</m>}}

Using these representations of the abstract vectors, we could represent the point $\mathbf P$ using

{{<m>}}
\mathbf P \to \begin{pmatrix}
P_1, P_2, \cdots, P_k
\end{pmatrix} \begin{pmatrix}
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \vdots\\
0 & 0 & 0 & 1
\end{pmatrix},
{{</m>}}

*which is insanely trivial since the representation of basis in this case is an identity matrix.*

{{< message title="Spherical Harmonics" class="info" >}}

Now we ask this question:

**Can we decompose the point using some other basis?**

The answer is yes.

While it is easier to perceive using the above matrix picture, it is much more convinent to use the index notation.

In physics, we are already dealing with this situition. We use spherical harmonics to decompose a field.

$$
\begin{equation}
f(r=1, \theta, \varphi) = \sum_{\ell=0}^\infty \sum_{m=-\ell}^\ell f_\ell^m  Y_\ell^m (\theta, \varphi ).
\end{equation}
$$

A general form of decomposition using rank 2 matrix is

$$
\mathbf P \to P_\ell^m V_m^\ell.
$$
{{</message>}}


NMF is talking about the same idea: coordinate transformations,

$$
X_{n}^{\phantom{n}k} = H_n^{\phantom{n}r} W_r^{\phantom{r}k}.
$$

We will view $X_{n}^{\phantom{n}k}$ as a vertical stack of $n$ points:

{{<m>}}
\begin{pmatrix}
\mathbf P_1 \\
\mathbf P_2 \\
\vdots \\
\mathbf P_n
\end{pmatrix} \to \begin{pmatrix}
P_{11} & P_{12} & \cdots & P_{1k} \\
P_{21} & P_{22} & \cdots & P_{2k} \\
\vdots & \vdots & \ddots & \vdots \\
P_{n1} & P_{n2} & \cdots & P_{nk}
\end{pmatrix} = \begin{pmatrix}
H_{11} & H_{12} & \cdots & H_{1r} \\
H_{21} & H_{22} & \cdots & H_{2r} \\
\vdots & \vdots & \ddots & \vdots \\
H_{n1} & H_{n2} & \cdots & H_{nr}
\end{pmatrix} \begin{pmatrix}
W_{11} & W_{12} & \cdots & W_{1k} \\
W_{21} & W_{22} & \cdots & W_{2k} \\
\vdots & \vdots & \ddots & \vdots \\
W_{r1} & W_{r2} & \cdots & W_{rk}
\end{pmatrix} \leftarrow \begin{pmatrix}
\mathbf H_1 \\
\mathbf H_2 \\
\vdots \\
\mathbf H_n
\end{pmatrix} \begin{pmatrix}
\mathbf W^1 & \mathbf W^2 & \cdots & \mathbf W^k
\end{pmatrix}
{{</m>}}

For a point $i$, we have

$$
\mathbf P_i = \mathbf H_i \begin{pmatrix}\mathbf W^1 & \mathbf W^2 & \cdots & \mathbf W^k \end{pmatrix}
$$

Compare this with the decomposition of a point in the cartesian coordinate system, this is a decomposition of each point on a basis spanned by $\mathbf W^i$.

{{< message title="Another View?" class="info" >}}

{{<m>}}
\begin{pmatrix}
\mathbf H^1 &
\mathbf H^2 &
\cdots  &
\mathbf H^r
\end{pmatrix} \begin{pmatrix}
\mathbf W_1 \\
\mathbf W_2 \\
\vdots \\
\mathbf W_r
\end{pmatrix}
{{</m>}}

Then we have the sum of a bunch of $(n, k)$ matrices,

$$
\mathbf H^1 \mathbf W_1 + \mathbf H^2 \mathbf W_2 + \mathbf H^3 \mathbf W_3 \cdots
$$

This is not providing more insights to me. It seems to be rewriting the original matrix in "a coordinate system" of r bases.
{{</message>}}

## Nonnegative Matrix Factorization

NMF is a dimension reduction method that decomposes $X_{n}^{\phantom{n}k}$ using

{{<m>}}
\begin{equation}
X_{n}^{\phantom{n}k} \sim H_n^{\phantom{n}r} W_r^{\phantom{r}k}.
\label{eq-nmf}
\end{equation}
{{</m>}}

while requiring the elements of the decomposition to be nonnegative. **But there are many possible decompositions!** Then we require this approximation to be as accurate as possible.

How do we measure the approximations?

We use the {{< c "cards/math/frobenius-distance.md" "Frobenius distance" >}} between the matrix $X_{n}^{\phantom{n}k}$ and $H_n^{\phantom{n}r} W_r^{\phantom{r}k}$,

$$
\lVert X_{n}^{\phantom{n}k} - H_n^{\phantom{n}r} W_r^{\phantom{r}k} \rVert^2 \equiv \sum_{n,k} (X_{n}^{\phantom{n}k} - H_n^{\phantom{n}r} W_r^{\phantom{r}k})^2.
$$

So NMF will require this Frobenius distance to be minimal.

## Why Does It Even Work?

Well, it doesn't always work. **We might have many different NMFs for one single matrix.**


{{< message title="Compare with SVD" class="warning" >}}

For a $n\times p$ matrix $\mathbf X$, we use SVD to get the singular value,

$$
\mathbf{U}^{\mathbf T}\mathbf{X} = \mathbf{D}\mathbf{V}^{\mathbf T}.
$$

In this case, we have $\mathbf D$ being uniquely determined but neither $\mathbf U$ nor $\mathbf V$.
{{</message>}}


How do we find a proper decomposition using NMF? We put restrictions on it, such as penalties. Apart from this, we also need to choose the rank of the decomposition $r$ in Eq. ($\ref{eq-nmf}$). Even if we fixed all these problems, NMF is computation expensive.
