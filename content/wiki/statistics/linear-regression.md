---
title: "Linear Regression"
excerpt: "Linear regression of multidimensional data"
date: 2019-01-01
toc: true
category:
- 'Statistics'
tag:
- 'Statistics'
- 'Basics'
- 'Linear Regression'
references:
- name: "The Elements of Statistical Learning by Jerome H. Friedman, Robert Tibshirani, and Trevor Hastie"
  link: ''
weight: 5
published: true
---

<div class="notes--warning" markdown="1">
In this article, we will use the Einstein summation convention. For example,
$$
X_{ij}\beta_ j
$$
is equivalent to
$$
\sum_j X_{ij}\beta_ j
$$
</div>

<div class="notes--info" markdown="1">
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
</div>

* ToC
{:toc}

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

$$
\begin{align}
\partial_{\beta_m} L =& (\partial_{\beta_m} ( Y_i - X_{ij}\beta_j ) ) ( Y_i - X_{ik}\beta_k ) +  ( Y_i - X_{ij}\beta_j ) \partial_{\beta_m} ( Y_i - X_{ik}\beta_k ) \\
=& - X_{ij} \delta_{jm}( Y_i - X_{ik}\beta_k ) + ( Y_i - X_{ij}\beta_j ) ( - X_{ik}\delta_{km} ) \\
=& - 2 X_{im} ( Y_i - X_{ij}\beta_j )
\end{align}
$$

Solving $- 2 X_{im} ( Y_i - X_{ij}\beta_j ) = 0$, we have
$$
\begin{align}
& 0 = X_{im} ( Y_i - X_{ij}\beta_j )  \\
& X_{im} X_{ij}\beta_j   = X_{im} Y_i \\
& \beta_j = ( X_{im} X_{ij} )^{-1} X_{im} Y_i
\end{align}
$$

In the abstract matrix notation,

$$
\boldsymbol \beta = ( \mathbf X^T \mathbf X )^{-1} \mathbf X^T \mathbf Y.
$$
