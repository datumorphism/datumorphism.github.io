---
title: "Bias-Variance"
excerpt: "Bias Variance Trade off"
date: 2019-06-07
toc: true
category:
- 'Statistical Learning'
tag:
- 'Statistical Learning'
- 'Basics'
references:
- link: http://scott.fortmann-roe.com/docs/BiasVariance.html
  name: 'Understanding the Bias-Variance Tradeoff'
- link: https://towardsdatascience.com/the-bias-variance-trade-off-explanation-and-demo-8f462f8d6326
  name: 'The Bias-Variance trade-off : Explanation and Demo'
- link: https://web.stanford.edu/~hastie/ElemStatLearn/
  name: 'The Element of Statistical Learning'
weight: 2
---

* ToC
{:toc}

## Bias and Variance

Suppose we have a perfect model $f(X)$ that represent a tight model of the dataset $(X,Y)$ but some irredicible error,

$$
\begin{equation}
Y = f(X) + \epsilon.
\label{dataset-using-true-model}
\end{equation}
$$

On the other hand, we could get another model using a specific model such as k-nearest neighbors, which we denote as $$k(X)$$.

<div class="card">
<header class="card-header">
<p class="card-header-title card-toggle">Why the two models?</p>
</header>
<div class="card-content is-hidden">
<div class="content" markdown="1">

Why are we talking about the perfect model and a model using a specific method?

The perfect model $f(X)$ is our ultimate goal, while the model using a specific method $k(X)$ is our effort of approaching the ultimate model.

</div>
</div>
</div>

What is our bias? It measures the deficit between $k(X)$ and the perfect model $f(X)$,

$$
\operatorname{Bias}[k(X)] = E[k(X)] - f(X)
$$

Zero bias means we are matching the perfect model.

<div class="card">
<header class="card-header">
<p class="card-header-title card-toggle">E[g(X)]</p>
</header>
<div class="card-content is-hidden">
<div class="content">
Expectation of the function.
</div>
</div>
</div>

What is variance? Variance is about the model itself:

$$
\operatorname{Variance} ( k(X) ) = \operatorname{E} \left( ( k(X) - \operatorname{E}( k(X) ) )^2 \right)
$$

The larger the variance, the more wiggly the model is.


## Mean Square Error

Bias measures the deficit between the specific model and the perfect model. How do we measure the deficit between the specific model and the actual data point? We need Mean Squared Error (MSE).

The Mean Squared Error (MSE) is defined as

$$
\begin{equation}
\operatorname{MSE}(X) = \operatorname{E} \left( ( Y - k(X) )^2  \right).
\end{equation}
$$

A straightforward decomposition using equation ($\ref{dataset-using-true-model}$) shows that we have three components in our MSE. To make the equations look nice, we drop the $(X)$, hence $k$ in the equation means $k(X)$.

$$
\begin{align}
\operatorname{MSE}(X) &= \operatorname{E} \left( ( Y - k )^2  \right) \nonumber \\
&=  \operatorname{E} \left( ( f + \epsilon - k )^2  \right)  \\
&= \operatorname{E} \left(  (f - k)^2 + \epsilon^2 {\color{red}+ 2 \epsilon (f - k ) } \right) \\
&= \operatorname{E} \left(  (f - k)^2 \right)  + \operatorname{E} \left( \epsilon^2 \right) \\
&= \operatorname{E} \left( (f - \operatorname{E}(k) +  \operatorname{E}(k) -k )  \right) + \operatorname{E} \left( \epsilon^2 \right) \\
&= \operatorname{E} \left( (f - \operatorname{E}(k) )^2 \right) + \operatorname{E} \left( ( \operatorname{E}(k) -k  )^2 \right) {\color{red}+ 2 \operatorname{E}\left((f - \operatorname{E}(k))( \operatorname{E}(k) -k ) \right)} + \operatorname{E} \left( \epsilon^2 \right) \\
&= \operatorname{Bias} ( k )^2 + \operatorname{Variance} (k) + \text{Irreducible Error}
\end{align}
$$

We have this Irreducible Error because the mean of the irreducible error is required to be zero, $\operatorname{E}(\epsilon)=0$. If this is not zero then the model $f(X)$ is not perfect.


## Bias-Variance Tradeoff

The more parameters we introduce in the model, it is more likely to reduce the bias. However, at some point, the more complexity we have in the model, the more wiggles the model will have. Thus the variance will be larger.

<div class="card">
<header class="card-header">
<p class="card-header-title card-toggle">Free Parameters</p>
</header>
<div class="card-content is-hidden">
<div class="content" markdown="1">
Fermi once said,

> I remember my friend Johnny von Neumann used to say, with four parameters I can fit an elephant, and with five I can make him wiggle his trunk.

There is a [nice story](http://lilith.fisica.ufmg.br/~dsoares/fdyson.htm) about Dyson and Fermi behind this.
</div>
</div>
</div>