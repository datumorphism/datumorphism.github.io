---
title: "Jargons"
description: "Jargons in statistics, accuracy, precision, population, sample, etl"
date: 2018-11-24
categories:
- 'Statistics'
tags:
- 'Statistics'
- 'Basics'
references:
- name: "Elements of Statistics by Stephen Bernstein and Ruth Bernstein"
  title: ''
weight: 2
---

## Accuracy and Precision

1. Accuracy: the measurement compared to the truth
2. Precision: variability of repeated measurements; the more precise, the less variations during each measurement.

|   | Accurate | Inaccurate |
|:----:|:-----:|:-----:|
| Precise |  Close to true value, small variations in each measurement | Far from true value, small variations in each measurement  |
| Imprecise |  Close to true value, large variations in each measurement  |  Far from true value, large variations in each measurement  |

Here is an example. Suppose we have a huge population (with true mean $M_0$) and we draw samples from it. For the first time, we have sample $S_1$. We could calculate the mean of the sample, $M_1$. Then we do it for a second time, and get sample $S_2$ and its mean $M_2$. It is not surprising that $M_1$ might not be the same as $M_2$.

Now we do this for 1000 times and get 1000 means, $\\{M_i\\}$. These means  $\\{M_i\\}$ is actually a distribution. Then we can calculate the expectation of these means and get $E(M_i) = M_e$.

In an ideal world, we would have the expectation value of all the sample means $M_e$ equal to the true mean $M_0$. In this case, our estimation of mean is not biased and **accurate**. The difference $M_e-M_0$ (or the absolute value of it) measures the accuracy.

Since all the sample means form a distribution. We would expect that most of the cases, the sample mean is close to the true mean. We would have a dispersion of this distribution. The dispersion is the precision.

It is quite similar to shooting. If someone shoots all his bullets on almost the same point on the target, we would say he is precise. But the point may not be at the center of the target, then we say he is not accurate.

## Population and Sample

Physical Population and Measurement Population

1. Physical population: all the physical objects that satisfy the constraints of the measurement
2. Measurement population: the specified property of the physical population that is to be measured

Finite and Infinite

1. Finite population: finite number of elements in the population, such as the measurement of 11 football players in a match
2. Infinite population: infinite number of elements in the population, such as the 'size' of the stars in the universe through all time
3. Hypothetical population: if the infinite population doesn't really exist

Sample

1. Physical sample: subset of physical population
2. Measurement sample: measurement of the physical sample

| | Population | Sample |
|:----:|:-----:|:------:|
| Physical | physical objects | physical subset of the physical population |
| Measurement | measurement of the physical population |  measurement of the physical sample  |

## Hypothesis

1. Statistical hypothesis: hypothesis about the measurement population
2. Research hypothesis or scientific hypothesis or working hypothesis: hypothesis about the physical population

## Loss Functions

1. RSS: residual sum-of-squares: $(\mathbf Y - \hat{\mathbf Y})^T(\mathbf Y - \hat{\mathbf Y})$ where $\mathbf Y$ is the actual data and $\hat{\mathbf Y}$ is the prediction

## Z Transformation

If we have our dataset as an array $\\{X_i\\}$, $\mu$ is the mean, $\sigma$ is the variance. A z transformation standardizes the dataset by

$$
Z_i = \frac{ X_i - \mu }{\sigma}.
$$

Note that $\mu$ is the sample mean and $\sigma$ is the sample standard deviation.

## Abbreviations

1. MSE: mean squared error
2. EPE: expected prediction error
3. RSS: sum of squares
