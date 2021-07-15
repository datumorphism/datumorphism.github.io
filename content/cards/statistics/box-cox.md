---
title: "Box-Cox Transformation"
description: "The Box-Cox transformation transforms data into Gaussian data, which is especially useful in feature engineering, e.g., fixing irregularities in variances of a time series."
date: 2021-07-13
authors:
  - "LM"
categories:
  - "statistics"
tags:
  - "data"
  - "transformation"
  - "time series"
references:
  - name: "Box GEP, Cox DR. An analysis of transformations. J R Stat Soc. 1964;26: 211–243. doi:10.1111/j.2517-6161.1964.tb00553.x"
    link: "http://dx.doi.org/10.1111/j.2517-6161.1964.tb00553.x"
  - name: "Vélez JI, Correa JC, Marmolejo-Ramos F. A new approach to the Box–Cox transformation. Frontiers in Applied Mathematics and Statistics. 2015;1: 12. doi:10.3389/fams.2015.00012"
    link: "https://www.frontiersin.org/articles/10.3389/fams.2015.00012/full"
  - link: "https://machinelearningmastery.com/power-transform-time-series-forecast-data-python/"
    name: "How to Use Power Transforms for Time Series Forecast Data with Python"
weight:
links:
  - "wiki/time-series/predictions-time-series-data.md"
  - "wiki/time-series/autoregressive-model.md"
---


Box-Cox transformation is a power transformation that involves logs and powers. It transforms data into normal distributions.

The Box-Cox transformation is defined as

{{<m>}}
y_i^{(\lambda)} = \begin{cases}
\lambda ^{-1} (y_i^\lambda - 1) & \quad \text{if } \lambda \neq 0\\
\log(y_i) & \quad \text{if } \lambda = 0.
\end{cases}
{{</m>}}

By selecting a proper $\lambda$, we get a Guassian distributed data, with a variable mean. The transformation take $y$ to

{{<m>}}
\rho(y^{(\lambda)}) =\frac{ \exp{\left( -(y^{(\lambda)} - \beta X)^{T} (y^{(\lambda)} - \beta X)/(2\sigma^2) \right) }}{(\sqrt{2\pi \sigma^2})^n} \prod_{i=1}^n \left\lvert \frac{d y_i^{(\lambda )}}{ dy_i } \right\rvert.
{{</m>}}

The term

{{<m>}}
\prod_{i=1}^n \left\lvert \frac{d y_i^{(\lambda )}}{ dy_i } \right\rvert = \lvert J \rvert
{{</m>}}

is the Jacobian as we are establishing the relations between the pdf of the data before and after the transfomation.



{{< message title="Analysis of Variance" >}}

Note that in analysis of variance, the results is not affected by linear transformations, thus the analysis of variance results will be the same as

$$
y_i^{(\lambda)} = \begin{cases}
y_i^\lambda & \quad \text{if } \lambda \neq 0\\\\
\log(y_i) & \quad \text{if } \lambda = 0.
\end{cases}
$$

{{< /message >}}



To find the proper $\lambda$, we write down the likelihood and maximize it. The likelihood is determined by the Gaussian distribution

{{<m>}}
L(\lambda, \beta, \sigma) = \rho(y^{(\lambda)}).
{{</m>}}

