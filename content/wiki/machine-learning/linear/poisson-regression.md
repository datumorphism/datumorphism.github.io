---
title: "Poisson Regression"
description: ""
date: 2021-05-07
categories:
  - "Machine Learning"
tags:
  - "Basics"
  - "Linear Models"
references:
  - name: "Fox J. Applied Regression Analysis and Generalized Linear Models. SAGE Publications; 2015. Available: https://play.google.com/store/books/details?id=cjB3BwAAQBAJ"
    link: "https://play.google.com/store/books/details?id=cjB3BwAAQBAJ"
  - name: "Rodríguez G, editor. Poisson Models for CountData. Generalized Linear Models. Available: https://data.princeton.edu/wws509/notes"
    link: "https://data.princeton.edu/wws509/notes"
  - name: "Chapter 19: Logistic and Poisson Regression by Marie Chesaniuk"
    link: "https://ademos.people.uic.edu/Chapter19.html"
  - name: "Poisson regression and non-normal loss (sklearn documentation)"
    link: "https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html"
  - name: "Beyond Multiple Linear Regression, Chapter 4 Poisson Regression"
    link: "https://bookdown.org/roback/bookdown-BeyondMLR/ch-poissonreg.html"
weight: 2
published: true
links:
  - "cards/statistics/poisson-process.md"
---

Poisson regression is a generalized linear model for count data.

To model a dataset that is generated from a {{< c "cards/statistics/poisson-process.md" "Poisson distribution" >}}, we only need to model the mean $\mu$ as it is the only parameters. The simplest model we can have for some given features $X$ is a linear model. However, for count data, the effects of the predictors are often multiplicative. The next simplest model we can have is

{{< m >}}
\mu = \exp\left(\beta X\right).
{{< /m >}}

The $\exp$ makes sure that the mean is positive as this is required for count data.
