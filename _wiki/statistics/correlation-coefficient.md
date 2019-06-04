---
title: "Correlation Coefficient and Covariance for Numeric Data"
excerpt: "Detecting correlations using correlations for numeric data"
date: 2018-11-18
toc: true
category:
- 'Statistics'
tag:
- 'Statistics'
- 'Basics'
- 'Correlation'
references:
- name: "Data Mining by Jiawei Han, Micheline Kamber, Jian Pei"
  link: ''
weight: 3
---

* ToC
{:toc}

## Covariances

<div class="notes--info" markdown="1">
Correlation coefficient is also known as Pearson's product moment coefficient.
</div>


### Review of Standard Deviation

For a series of data A, we have the standard deviations

$$
\sigma_A = \sqrt{ \frac{ \sum (a_i - \bar A)^2 }{ n } },
$$

where $n$ is the number of elements in series A. Now imagine we have two series
$(a_i - \bar A)$ and $(a_j - \bar A)$. The geometric mean squared for $i=j$ is 

$$
M_i^2 = (a_i - \bar A)^2.
$$

From this point of view, standard deviation is in fact a measure of the mean of **geometric mean of the deviation of each element**.


### Generalize Standard Deviation to Covariances

Similarly, for two series A and B of the same length, we could define a quantity to measure the geometric mean of the deviation of the two series correspondingly

$$
\sigma_{A,B}^2 = \frac{ \sum (a_i - \bar A) (b_i - \bar B) }{ n },
$$

which is named the covariance of A and B, i.e., $\text{Cov} ({A,B})$.

It is easy to show that

$$
\mathrm{Cov}({A,B}) = E( A,B ) - \bar A \bar B.
$$

<div class="notes--info" markdown="1">

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
</div>



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


<div class="notes--info" markdown="1">
Covariance is also related to [dispersion matrix](../multidimensional-data).
</div>

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