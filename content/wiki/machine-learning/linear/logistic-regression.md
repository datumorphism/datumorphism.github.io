---
title: "Logistic Regression"
description: "logistics regression is a simple model for classification"
date: 2021-05-27
categories:
  - "Machine Learning"
tags:
  - "Unsupervised Learning"
  - "Statistical Learning"
  - "Basics"
  - "Linear Models"
  - "Supervised Learning"
  - "Classification"
references:
  - name: "Hastie T, Tibshirani R, Friedman J. The Elements of Statistical Learning: Data Mining, Inference, and Prediction. Springer Science & Business Media; 2013. pp. 567–567. Available: https://play.google.com/store/books/details?id=yPfZBwAAQBAJ"
    link: "https://play.google.com/store/books/details?id=yPfZBwAAQBAJ"
  - name: "Friedman J, Hastie T, Tibshirani R. Additive Logistic Regression. The Annals of Statistics. 2000. pp. 337–374. doi:10.1214/aos/1016218223"
    link: "https://projecteuclid.org/journals/annals-of-statistics/volume-28/issue-2/Additive-logistic-regression--a-statistical-view-of-boosting-With/10.1214/aos/1016218223.full"
    key: "friedman2000"
  - name: "Mehta P, Wang C-H, Day AGR, Richardson C, Bukov M, Fisher CK, et al. A high-bias, low-variance introduction to Machine Learning for physicists. Phys Rep. 2019;810: 1–124. doi:10.1016/j.physrep.2019.03.001"
    link: "https://linkinghub.elsevier.com/retrieve/pii/S0370157319300766"
    key: "Mehta2019"
weight: 3
links:
  - "cards/statistics/likelihood.md"
  - "cards/information/cross-entropy.md"
  - "cards/machine-learning/neural-networks/activation-uni-polar-sigmoid.md"
published: true
---


In a classification problem, given a list of features values $x$ and their corresponding classes $\\{c_i\\}$, the posterior for of the classes, aka conditional probability of the classes, is

{{< m >}}
p(C=c_i\mid X=x).
{{< /m >}}

{{< message title="Likelihood" class="info" >}}

The likelihood of the data is

$$
p(X=x\mid C=c_i).
$$

{{< /message >}}

## Logistic Regression for Two Classes

For two classes, the simplest model for the posterior is a linear model,

{{< m >}}
\log \frac{p(C=c_1\mid X=x) }{p(C=c_2\mid X=x)} = \beta_0 + \beta_1 \cdot x,
{{< /m >}}

which is equivalent to

{{< m >}}
p(C=c_1\mid X=x)  = \exp\left(\beta_0 + \beta_1 \cdot x\right) p(C=c_2\mid X=x) .
{{< /m >}}

{{< message title="Why" class="info" >}}

The reason that we proposing a linear model for the quantity

$$
\log \frac{p(C=c_1\mid X=x) }{p(C=c_2\mid X=x)},
$$

is that it has a range from $-\infty$ to $\infty$ which matches the range of the linear model $ \beta_0 + \beta_1 \cdot x$.

We can also see in the following results that such relation guarantees that the conditional probabilities are restricted to 0 to 1 after applying the normalization constraint.

{{< /message >}}

Using the normalization condition

{{< m >}}
p(C=c_1\mid X=x) +  p(C=c_2\mid X=x)  = 1,
{{< /m >}}

we can derive the posterior for each classes

{{< m >}}
\begin{align}
p(C=c_2\mid X=x) &= \frac{1}{1 +  \exp\left(\beta_0 + \beta_1 \cdot x\right)} \\
p(C=c_1\mid X=x) &= \frac{\exp\left(\beta_0 + \beta_1 \cdot x\right)}{1 +  \exp\left(\beta_0 + \beta_1 \cdot x\right)}.
\end{align}
{{< /m >}}

{{< figure src="../assets/logistic-regression/logistic_regression_two_class_probs.png" title="The two conditional probabilities" caption="For simplicity, we are using $x'=\beta_0 + \beta_1 \cdot x$ in this figure." >}}

This is the {{< c "cards/machine-learning/neural-networks/activation-uni-polar-sigmoid.md" "sigmoid function" >}}

{{< message title="Limiting behavior" class="info" >}}

1. As $\beta_0 + \beta_1 \cdot x \to \infty$, we have $p(C=c_2\mid X=x) \to 0$ and $p(C=c_1\mid X=x)\to 1$.
2. As $\beta_0 + \beta_1 \cdot x \to 0$, we have $p(C=c_2\mid X=x) \to 0.5$ and $p(C=c_1\mid X=x)\to 0.5$.
3. As $\beta_0 + \beta_1 \cdot x \to -\infty$, we have $p(C=c_2\mid X=x) \to 1$ and $p(C=c_1\mid X=x)\to 0$.

{{< /message >}}

## Relation to Cross Entropy

For two classes, we can write down the likelihood as

{{< m >}}
\pi_{i=1}^{N} p^{y_i} p^{1-y_i},
{{< /m >}}

where $p$ is the probability of label $y_i=c_1$ and $1-p$ is probability of label $y_i=c_2$.

Taking the neglog, we find that

{{< m >}}
-l = sum_{i=1}^N ( -y_i \log p - (1-y_i)\log (1-p) ).
{{< /m >}}

This is the {{< c "cards/information/cross-entropy.md" "cross entropy" >}}


## Logistic Regression for $K$ Classes

It is easily generalized to problems with $K$ classes.

{{< m >}}
\begin{align}
p(C=c_K\mid X=x) &= \frac{1}{1 +  \sum_k\exp\left(\beta_{k0} + \beta_k \cdot x\right)} \\
p(C=c_k\mid X=x) &= \frac{\exp\left(\beta_{k0} + \beta_k \cdot x\right)}{1 +  \sum_k\exp\left(\beta_{k0} + \beta_k \cdot x\right)}
\end{align}
{{< /m >}}


## Why not non-linear

The log of the posterior ratio can be more complex than linear models. In general, we have[^friedman2000]

{{< m >}}
\log \frac{p(C=c_1\mid X=x) }{p(C=c_2\mid X=x)} = f(x),
{{< /m >}}

so that

{{< m >}}
p(C=c_1\mid X=x) = \frac{\exp(f(x))}{ 1 + \exp(f(x)) }.
{{< /m >}}

The logistic regression model we mentioned in the previous sections require

{{<m>}}
f(x) = \beta_0 + \beta_1 \cdot x.
{{</m>}}

A more general additive model is

{{<m>}}
f(x) = \sum_i f_i(x),
{{</m>}}

where we can apply algorithms such as local scoring to fit such models[^friedman2000].


[^friedman2000]: {{< cite key="friedman2000" >}}