---
title: "Bayesian Linear Regression"
excerpt: "Bayesian Linear Regression"
date: 2019-06-18
toc: true
category:
- 'Machine Learning::Bayesian'
tag:
- 'Machine Learning'
- 'Regression'
- 'Bayesian'
references:
- name: Introduction to Bayesian Linear Regression
  link: https://towardsdatascience.com/introduction-to-bayesian-linear-regression-e66e60791ea7
- name: "Linear Regression: A Bayesian Point of View"
  link: https://wiseodd.github.io/techblog/2017/01/05/bayesian-regression/
- name: zjost/bayesian-linear-regression
  link: https://github.com/zjost/bayesian-linear-regression
weight: 22
---

## Linear Regression and Likelihood

The linear estimator $y$ is

$$
\begin{equation}
y^n = \beta^m X_m^{\phantom{m}n}.
\label{eq-linear-model}
\end{equation}
$$

As usual, we have redefined our data to get rid of the intercept $\beta^0$.

In ordinary linear models, we find the error being the difference between the target $\hat y$ and the estimator $y$

$$
\epsilon = \hat y - y,
$$

which is required to have a minimum absolute value.

We could use least squares to solve the problem. However, instead of using a deterministic estimator $\beta^m X_m^{\phantom{m}n}$, we assume a Gaussian random estimator

$$
\begin{equation}
\mathcal{N}(\mu, \sigma^2) = \mathcal{N}(\beta^m X_m^{\phantom{m}n}, \sigma^2),
\end{equation}
$$

where we have used the knowledge of linear regression, that the mean of the estimator should be a linear model $\beta^m X_m^{\phantom{m}n}$. The likelihood becomes

$$
\begin{equation}
P(\hat y^n \mid [X_m^{\phantom{m}n}, \beta^m] ) = \frac{1}{\sqrt{2 \sigma^2 \pi}}  \exp \left( -\frac{(\hat{y^n} - \beta^m X_m^{\phantom{m}n})^2}{2 \sigma^2} \right)
\end{equation}
$$

It is not surprising that requiring the maximum likelihood will lead to the same result as least-squares due to log takes out exponential.


## Bayesian Linear Model

Applying Bayes' theorem to this problem,

$$
P( [X_m^{\phantom{m}n}, \beta^m] \mid \hat y^n  ) {\color{red}P(\hat y^n)} = P(\hat y^n \mid [X_m^{\phantom{m}n}, \beta^m] ) P([X_m^{\phantom{m}n}, \beta^m]).
$$

Since ${\color{red}P(\hat y^n)}$ doesn't depend on the parameters and is a constant, we will ignore it for the sake of optimization.

$$
P( [X_m^{\phantom{m}n}, \beta^m] \mid \hat y^n  ) \propto P(\hat y^n \mid [X_m^{\phantom{m}n}, \beta^m] ) P([X_m^{\phantom{m}n}, \beta^m]).
$$

> Fall back to Maximum Likelihood
>
> If $$P([X_m^{\phantom{m}n}, \beta^m]) = 1$$.


We will assume a least information model for $P([X_m^{\phantom{m}n}, \beta^m])$, that is

$$
P([X_m^{\phantom{m}n}, \beta^m]) = \mathcal{N} (0, \sigma_\beta^2) =   \frac{1}{\sqrt{2 \sigma_\beta^2 \pi}}  \exp \left( -\frac{(\beta^m )^2}{2 \sigma_\beta^2} \right).
$$

Our posterior becomes

$$
\log P( [X_m^{\phantom{m}n}, \beta^m] \mid \hat y^n  ) =  -\frac{(\hat{y^n} - \beta^m X_m^{\phantom{m}n})^2}{2 \sigma^2}  -\frac{(\beta^m )^2}{2 \sigma_\beta^2}  + \mathrm{Const.}
$$

This is nothing but Ridge loss with coefficient $\lambda$, where

$$
\frac{\sigma^2}{\sigma_\beta^2} = \lambda.
$$
