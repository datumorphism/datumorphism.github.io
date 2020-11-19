---
title: "Correlation Coefficient and Covariance for Numeric Data"
description: "Detecting correlations using correlations for numeric data"
date: 2018-11-18
category:
- 'Statistics'
tags:
- 'Statistics'
- 'Basics'
- 'Correlation'
references:
- name: "Data Mining by Jiawei Han, Micheline Kamber, Jian Pei"
  link: ''
links:
  - cards/statistics/covariance-matrix.md
  - wiki/statistics/multidimensional-data.md
  - wiki/statistics/correlation-analysis-chi-square.md
weight: 4
---



## Covariances

{{< message class="info">}}
Correlation coefficient is also known as the Pearson's product moment coefficient.
{{</message>}}


### Review of Standard Deviation

For a series of data A, we have the standard deviations

$$
\sigma_A = \sqrt{ \frac{ \sum (a_i - \bar A)^2 }{ n } },
$$

where $n$ is the number of elements in series A.

The standard deviation is very easy to understand. It is basically the average Eucleadian distance between the data points and the average value. In this article, we will take another point of view.

Now imagine we have two series
$(a_i - \bar A)$ and $(a_j - \bar A)$. The geometric mean squared for $i=j$ is

$$
M_i^2 = (a_i - \bar A)^2.
$$

From this point of view, the standard deviation is in fact a measure of the mean of **geometric mean of the deviation of each element**.

{{< card title="Standard Deviation of the Sample" >}}

If we are dealing with a sample instead of the whole population, the standard deviation should be defined as
$$
\sigma_A = \sqrt{ \frac{ \sum (a_i - \bar A)^2 }{ n - 1 } }.
$$

Why the $n-1$? We could easily understand this by taking extreme cases. Suppose we have only 1 sample data point, the standard deviation knowledge that we can infer should be infinite since we have no idea what the standard deviation is.
{{</card>}}

### Generalize Standard Deviation to Covariances

> Knowledge card: [Covariance matrix](/cards/statistics/covariance-matrix/).

Similarly, for two series A and B of the same length, we could define a quantity to measure the geometric mean of the deviation of the two series correspondingly

$$
\sigma_{A,B}^2 = \frac{ \sum (a_i - \bar A) (b_i - \bar B) }{ n },
$$

which is named the covariance of A and B, i.e., $\text{Cov} ({A,B})$.

It is easy to show that

$$
\mathrm{Cov}({A,B}) = E( A,B ) - \bar A \bar B.
$$

{{< message class="info">}}

At first glance, the square in the definition seems to be only for notation purpose at this point.

Meanwhile, using this idea of the mean of geometric mean, we could easily generalize it to the covariance of three series,

$$
\sigma_{A,B,C}^3 = \frac{ \sum (a_i - \bar A) (b_i - \bar B)(c_i - \bar C) }{ n },
$$

or even arbitrary N series,

$$
\sigma_{A_1, A_2, ..., A_N }^N = \frac{ \sum_{i=1}^{n} \text{ geometric mean of the ith elements to the Nth power }  }{ n }  = \frac{ \sum (a_{1,i} - \bar A_1) \cdots (a_{N,i} - \bar A_{N})}{ n },
$$

which should be called the covariance of all the N series, $\mathrm{Cov} ({A_1, A_2,\cdots, A_N })$.

Of course, we do not use these since we could easily build a covariance matrix to indicate all the possible covariances between any two variables, for example,

$$
\mathbf{C} = \begin{pmatrix}
\mathrm{Cov} (A_1, A_1) & \mathrm{Cov} (A_1, A_2) \\\\
\mathrm{Cov} (A_2, A_1) & \mathrm{Cov} (A_2, A_2)
\end{pmatrix}
$$

{{</message>}}

Covariance measures the correlation of these two series. To see this, we assume that we have two series A = B, which leads to $\sigma_{A,B} = \sigma_{A}$. Suppose we have two series at a completely opposite phase,

| index | A | B |
|--|---|---|
| 1 | 1 | -1 |
| 2 | -1 | 1 |
| 3 | 1 | -1 |
| 4 | -1 | 1 |
| 5 | 1 | -1 |
| 6 | -1 | 1 |
| 7 | 1 | -1 |

we have $\sigma_{A,B} = -1 $. The negative sign tells us that our series are anti-correlated.

{{< message class="info">}}
Covariance is also related to [dispersion matrix](../multidimensional-data).
{{</message>}}

## Correlation Coefficient

However, we would find that the value of the covariance depends on the values of the standard deviation of each series, which makes it hard to determine how strong the correlation is.

The obvious normalization factor is the multiplication of covariance of the two series, $\sigma_A$ and $\sigma_B$, i.e.,

$$
r_{A,B} = \frac{ \text{Cov}(A,B)  } { \sigma_{A} \sigma_{B} } = \frac{ \sum_i (a_i - \bar A) (b_i - \bar B) }{ n\sigma_{A} \sigma_{B} }
$$

<div class="notes--info" markdown="1">
The geometric mean view of it is

$$
r_{A,B} = \frac{ \sum_{i} ( \text{Sign}(a_i - \bar A) M_{i}^a ) ( \text{Sign}(b_i - \bar B) M_i^b ) }{ \sum_i { M_i^a } \sum_j { M_j^b } }
$$

which is some kind of geometric mean of the geometric mean of each series.
</div>
