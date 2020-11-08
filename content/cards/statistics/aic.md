---
title: Akaike Information Criterion
references:
  - link: https://en.wikipedia.org/wiki/Akaike_information_criterion#:~:text=The%20Akaike%20information%20criterion%20(AIC,response%20to%20a%20training%20sample.
    name: Akaike Information Criterion @ Wikipedia
  - link:
    name: Vandekerckhove, J., & Matzke, D. (2015). Model comparison and the principle of parsimony. Oxford Library of Psychology.
links:
  - wiki/model-selection/goodness-of-fit.md
---

Suppose we have a model that describes the data generation process behind a dataset. The distribution by the model is denoted as $\hat f$. The actual data generation process is described by a distribution $f$.

We ask the question:

How good is the approximation using $\hat f$?

To be more precise, how much information is lost if we use our model dist $\hat f$ to substitute the actual data generation distribution $f$?

AIC defines this information loss as

$$
\mathrm{AIC} = - 2 \ln p(y|\hat\theta) + 2k
$$


- $y$: data set
- $\hat\theta$: parameter of the model that is estimated by maximum-likelihood
- $\ln p(y|\hat\theta)$: log maximum likelihood (the goodness-of-fit)
- $k$: number of adjustable model params; $+2k$ is then a penalty.

The first term represents the [goodness of fit](/wiki/model-selection/goodness-of-fit) and the second term is a penalty for the complexity.

The smaller AIC, the better the model is by the AIC.

Limiting behaviors:
- $k\to0$: $\mathrm{AIC}\to- 2 \ln p(y|\hat\theta)$, which makes sense since we estimated the parameters using maximum likelihood.
- $k\to\infty$: $\mathrm{AIC}\to\infty$. There is a problem with this. If we have a huge number of adjustable parameters, the data set will not be relevant for choosing a model anymore.

