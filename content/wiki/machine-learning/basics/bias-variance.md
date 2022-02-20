---
title: "Bias-Variance"
description: "Bias Variance Trade off is a key concept in statistical learning"
date: 2019-06-07
categories:
  - "Machine Learning"
  - "Basics"
tags:
  - "Statistical Learning"
  - "Basics"
references:
  - link: "http://scott.fortmann-roe.com/docs/BiasVariance.html"
    name: "Understanding the Bias-Variance Tradeoff"
  - link: "https://towardsdatascience.com/the-bias-variance-trade-off-explanation-and-demo-8f462f8d6326"
    name: "The Bias-Variance trade-off : Explanation and Demo"
  - link: "https://web.stanford.edu/~hastie/ElemStatLearn/"
    name: "The Element of Statistical Learning"
  - link: "https://books.google.de/books?id=qcI_AAAAQBAJ&source=gbs_navlinks_s"
    name: "James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). An Introduction to Statistical Learning. In Springer Texts in Statistics. Springer Science & Business Media."
weight: 2
links:
  - cards/machine-learning/learning-theories/empirical-risk-minimization.md
---


## Bias and Variance

Suppose $f(X)$ is a perfect model that represents a "tight" model of the dataset $(X,Y)$ but some irredicible error $\epsilon$,

$$
\begin{equation}
Y = f(X) + \epsilon.
\label{dataset-using-true-model}
\end{equation}
$$

On the other hand, we build another model using a specific method such as k-nearest neighbors, which is denoted as $k(X)$.

{{< message title="Why the two models?" class="info" >}}

Why are we talking about the perfect model and a model using a specific method?

The perfect model $f(X)$ is our ultimate goal, while the model using a specific method $k(X)$ is our effort of approaching the ultimate model.

{{< /message >}}

The bias measures the deficit between $k(X)$ and the perfect model $f(X)$,

$$
\operatorname{Bias}[k(X)] = E[k(X)] - f(X)
$$

Zero bias means we are matching the perfect model.

{{< message title="$E[g(X)]$" class="info" >}}
$E[g(X)]$ is the expectation of the function.
{{< /message >}}

The variance of the model is a measurement of the consistency

$$
\operatorname{Variance} ( k(X) ) = \operatorname{E} \left( ( k(X) - \operatorname{E}( k(X) ) )^2 \right)
$$

The larger the variance, the more wiggly the model is.


## Mean Square Error

Bias measures the deficit between the specific model and the perfect model. To measure the deficit between the specific model and the actual data point, we need the Mean Squared Error (MSE).

The Mean Squared Error (MSE) is defined as

$$
\begin{equation}
\operatorname{MSE}(X) = \operatorname{E} \left( ( Y - k(X) )^2  \right).
\end{equation}
$$

This form of expected error can also be used to evaluate models, i.e., calculate expectations by varying models. A straightforward decomposition using equation ($\ref{dataset-using-true-model}$) shows that we have three components in our expected error. There are several ways to derive the decomposition of the expected error. We only show one here.

{{< m >}}
\begin{align}
\operatorname{Expected Error}(X) &= \operatorname{E} \left( ( Y - k )^2  \right) \nonumber \\
&=  \operatorname{E} \left( ( f + \epsilon - k )^2  \right)  \\
&= \operatorname{E} \left( (f - \operatorname{E} k - (k - \operatorname{k}) + \epsilon)^2 \right) \\
&= \operatorname{E} \left( (f - \operatorname{E} k)^2 + (k - \operatorname{E}k)^2 + \epsilon^2 - (f - \operatorname{E} k)(k - \operatorname{E}k) +   (f - \operatorname{E} k) \epsilon -  (k - \operatorname{E}k)\epsilon \right) \\
&=  \operatorname{E} \left( (f - \operatorname{E} k)^2\right) + \operatorname{E}\left((k - \operatorname{E}k)^2\right) + \operatorname{E} \left( \epsilon^2 \right) {\color{red}- 2\operatorname{E} \left( (f - \operatorname{E} k)(k - \operatorname{E}k) \right) +  2\operatorname{E} \left(  (f - \operatorname{E} k) \epsilon \right) -  2\operatorname{E} \left( (k - \operatorname{E}k)\epsilon \right)} \\
&= (f - \operatorname{E} k)^2 + \operatorname{E}\left((k - \operatorname{E}k)^2\right) + \operatorname{E} \left( \epsilon^2 \right)\\
&= \operatorname{Bias} ( k )^2 + \operatorname{Variance} (k) + \text{Irreducible Error}
\end{align}
{{< /m >}}

In this derivation, we've used several relations.

1. We used $\operatorname{E} \left( (f - \operatorname{E} k)^2\right) = (f - \operatorname{E} k)^2$ becuase the term $(f - \operatorname{E} k)^2$ is constant thus the expectation value is itself.
2. We have dropped the terms in red. They are related to the fact that the irreducible error is required to be zero, $\operatorname{E}(\epsilon)=0$. If it is not zero then the model $f(X)$ is not perfect.
   1. $\operatorname{E} \left( (f - \operatorname{E} k)(k - \operatorname{E}k) \right)= (f - \operatorname{E} k)\operatorname{E} \left( (k - \operatorname{E}k) \right)= 0.$
   2. $\operatorname{E} \left(  (f - \operatorname{E} k) \epsilon \right) = (f - \operatorname{E} k) \operatorname{E} \left(   \epsilon \right) = 0.$
   3. $\operatorname{E} \left( (k - \operatorname{E}k)\epsilon \right) = 0.$


## Bias-Variance Tradeoff

The more parameters we introduce in the model, it is more likely to reduce the bias. However, at some point, the more complexity we have in the model, the more wiggles the model will have. Thus the variance will be larger.

{{< message title="Free Parameters" class="light" >}}
Fermi once said,

> I remember my friend Johnny von Neumann used to say, with four parameters I can fit an elephant, and with five I can make him wiggle his trunk.

There is a [nice story](http://lilith.fisica.ufmg.br/~dsoares/fdyson.htm) about Dyson and Fermi behind this.

{{< /message >}}
