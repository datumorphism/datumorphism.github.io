---
title: "Describing Multi-dimensional Data"
excerpt: "Describing multi-dimensional data"
date: 2018-12-03
toc: true
category:
- 'Statistics'
tag:
- 'Statistics'
- 'Basics'
- 'Covaraince'
references:
weight: 6
published: false
---

* ToC
{:toc}

## Descriptions of Multidimensional Data

### Dispersion Matrix

As defined in [Correlation Coefficient and Covariance for Numeric Data](../correlation-coefficient), covariance is about the variance of two series. This property makes it easy to generalize it to multidimensional data.

The generalized quantity is named as **dispersion matrix**. Suppose we have a $p$ dimensional dataset $X$,



| index | $x_1$ |  $x_2$ | ... | $x_p$ |
|--|--|--|--|--|
| 1 |  2.3 | 12.3 | 83.2 | 9.3 |
| ... |  ... | ... | ... | ... |
| N |  3.1 | 5.6 | 23.6 | 8.2 |

We could then calculate the pairwise covariance between the different dimensions. 

| | $x_1$ |  $x_2$ | ... | $x_p$ |
| $x_1$ |   |  |  | |
| $x_2$ | | | | |
| ... | | | | |
| $x_p$ | | | | |

