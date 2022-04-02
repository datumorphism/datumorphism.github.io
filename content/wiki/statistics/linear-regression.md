---
title: "Linear Regression"
description: "Linear regression of multidimensional data"
date: 2019-01-01
categories:
  - "Statistics"
tags:
  - "Statistics"
  - "Basics"
  - "Linear Regression"
references:
  - name: "The Elements of Statistical Learning by Jerome H. Friedman, Robert Tibshirani, and Trevor Hastie"
    link: ""
  - name: "Shafer G, Vovk V. A tutorial on conformal prediction. arXiv [cs.LG]. 2007. Available: http://arxiv.org/abs/0706.3188"
    link: "http://arxiv.org/abs/0706.3188"
    key: "Shafer2007"
weight: 6
published: true
---

{{< message class="warning" >}}
In this article, we will use the Einstein summation convention. For example,
$$
X_{ij}\beta_ j
$$
is equivalent to
$$
\sum_j X_{ij}\beta_ j
$$
{{</message>}}

{{< message class="info" >}}
In statistics, we have at least three categories of quantities:

1. data and labels
2. abstract theoretical quantities
3. parameters and predictions of models

The convention is that quantities with $\hat {}$ are the model quantities. Sometimes we do not distinguish the abstract theoretical quantities and model quantities.

If it is necessary to use different notations for the abstract theoretical quantities and the model quantities, we would use bold symbols ($\mathbf Y$) or latin sub/super indices ( $Y_a$ ) for theoretical quantities and greek letters ( $Y_\alpha$ ) for model quantities.

So we use the following conventions in this article.

1. $\mathbf X$ or $X_{ij}$: data
2. $\mathbf Y$ or $Y_{i}$: results
3. $\hat{\mathbf Y}$ or $\hat Y_{i}$: predicted results
{{</message>}}


## A Model

A model is an estimator of the data that maps the inputs $\mathbf X$ to the predicted outputs $\hat{\mathbf Y}$, $\hat{\mathbf Y} = F( \mathbf X )$. The map $F$ might require some parameters, ${\boldsymbol\alpha, \boldsymbol\beta, \cdots }$.

Then we should have an estimator that tells us how good the model is given some parameters. For example, we could define a loss function $L(\mathbf Y,\hat{\mathbf Y} )$ that estimates the deficit between the actual data and the predicted results. Then we minimize this deficit.

So a model usually has

1. map,
2. esitmator.

## Linear Model

The model is simple

$$
\hat Y_i = X_{ij}\beta_ j + \beta_0
$$

One might want to create a augmented dataset by including a 0th column $X_{i0} = 1$, so that we have
$$
\hat Y_i = X_{ij}\beta_ j
$$
with $j=0,1,2,...$.

Using least squares as our estimator, we minimize the RSS loss function $L$ by choosing the suitable parameters $\beta_j$. The loss function is

$$
L = ( Y_i - X_{ij}\beta_j )( Y_i - X_{ik}\beta_k ).
$$

Minimizing it 'requires' $\partial_{\beta_m} L = 0$ and $\partial_{\beta_m}\partial_{\beta_n} L > 0 $.

We have

{{<m>}}
\begin{align}
\partial_{\beta_m} L =& (\partial_{\beta_m} ( Y_i - X_{ij}\beta_j ) ) ( Y_i - X_{ik}\beta_k ) +  ( Y_i - X_{ij}\beta_j ) \partial_{\beta_m} ( Y_i - X_{ik}\beta_k ) \\
=& - X_{ij} \delta_{jm}( Y_i - X_{ik}\beta_k ) + ( Y_i - X_{ij}\beta_j ) ( - X_{ik}\delta_{km} ) \\
=& - 2 X_{im} ( Y_i - X_{ij}\beta_j )
\end{align}
{{</m>}}

Solving $- 2 X_{im} ( Y_i - X_{ij}\beta_j ) = 0$, we have

{{<m>}}
\begin{align}
& 0 = X_{im} ( Y_i - X_{ij}\beta_j )  \\
& X_{im} X_{ij}\beta_j   = X_{im} Y_i
\end{align}
{{</m>}}

Note that it is multiplication and summation on the left since we are using Einstein summation convention. This is better understood in the abstract matrix notation,

$$
\boldsymbol \beta = ( \mathbf X^T \mathbf X )^{-1} \mathbf X^T \mathbf Y.
$$

## Scalar $\mathbf X_i$

For scalar $\mathbf X_i = x_i$, we can replace $\mathbf X$ with a vector $\vec x$ for all data points. we have

{{< m >}}
\beta = \frac{x_j y_j}{x_i x_i}.
{{< /m >}}

More generally, least square leads to the following results[^Shafer2007]

{{< m >}}
\begin{align}
k &= \frac{\sum_j (x_j - \bar x) y_j}{\sum_i (x_i - \bar x)(x_i - \bar x)} \\
b &= \bar y - k \bar x,
\end{align}
{{< /m >}}

where $\bar x$ and $\bar y$ are the mean values. Then the model

{{< m >}}
y = k x + b
{{< /m >}}

can be obtained.


[^Shafer2007]: {{< cite key="Shafer2007" >}}