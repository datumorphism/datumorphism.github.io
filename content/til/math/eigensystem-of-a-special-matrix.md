---
layout: til
title: "Eigensystem of A Special Matrix"
date: 2015-02-15 # not necessarily the date created but to ensure the sorting of posts
modified: 2015-08-18 # 2015-02-03 #2014-08-27T11:57:41-04:00
author: Lei Ma
comments: true
category:
- math
tags:
- 'Linear Algebra'
summary: Eigenstates of a very special matrix
---



One of the most used matrix in physics is

$$
\begin{pmatrix}
a + c \mathrm i & b \\
b & a + c \mathrm i
\end{pmatrix},
$$

where $a$, $b$, $c$ are real numbers.

It is interesting that as we go from

$$
\begin{pmatrix}
a + c \mathrm i & 0 \\
0 & a + c \mathrm i
\end{pmatrix},
$$

to the previous matrix, the eigenstates change from

$$
\begin{pmatrix}
1 \\
0
\end{pmatrix}, \mathrm{and } \begin{pmatrix}
0 \\
1
\end{pmatrix}
$$

to

$$
\begin{pmatrix}
1 \\
1
\end{pmatrix}, \mathrm{and } \begin{pmatrix}
1 \\
-1
\end{pmatrix}
$$

no matter how small $b$ is.


**A useful trick when solving the eigensystem is to remove an identity from the matrix because it only shifts the eigenvalue by a certain amount.**
